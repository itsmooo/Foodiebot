import os
import time
from typing import List, Dict
from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_pinecone import Pinecone
from langchain.schema import Document

# Load environment variables
load_dotenv()

# === CONFIG ===
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "somali-restaurant")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT", "us-east-1-aws")

if not OPENAI_API_KEY or not PINECONE_API_KEY:
    raise ValueError("Required environment variables OPENAI_API_KEY and PINECONE_API_KEY must be set")

# Initialize OpenAI embeddings
print("DEBUG: Starting initialization...", flush=True)
print(f"DEBUG: API key starts with: {PINECONE_API_KEY[:10]}...", flush=True)

print("Pinecone initialized successfully", flush=True)

# === CLASS ===
class RestaurantVectorDB:
    def __init__(self):
        print("DEBUG: Creating RestaurantVectorDB instance...", flush=True)
        
        # FIXED: Using text-embedding-3-small with 1024 dimensions to match Pinecone index
        self.embeddings = OpenAIEmbeddings(
            api_key=OPENAI_API_KEY,
            model="text-embedding-3-small",
            dimensions=1024  # This is the key fix!
        )

        # Initialize Langchain vectorstore
        self.vectorstore = Pinecone.from_existing_index(
            index_name=PINECONE_INDEX_NAME,
            embedding=self.embeddings,
            namespace="restaurant_data"
        )
        print("Langchain vectorstore initialized", flush=True)

    def process_restaurant_data(self, data_path: str) -> List[Document]:
        """Process restaurant data file and split into chunks"""
        print(f"DEBUG: Looking for data file at {data_path}", flush=True)
        
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Data file not found: {data_path}")
        
        print("DEBUG: Found data file", flush=True)
        
        with open(data_path, 'r', encoding='utf-8') as f:
            content = f.read()

        print("DEBUG: Processing restaurant data...", flush=True)
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )

        chunks = text_splitter.split_text(content)
        documents = [
            Document(
                page_content=chunk, 
                metadata={
                    "chunk_id": i,
                    "source": data_path,
                    "chunk_size": len(chunk)
                }
            )
            for i, chunk in enumerate(chunks)
        ]
        
        print(f"DEBUG: Created {len(documents)} document chunks", flush=True)
        return documents

    def upload_to_pinecone(self, documents: List[Document]):
        """Upload documents to Pinecone vector database"""
        print("DEBUG: Starting upload to Pinecone...", flush=True)
        
        try:
            # Upload in batches to avoid rate limits
            batch_size = 100
            for i in range(0, len(documents), batch_size):
                batch = documents[i:i + batch_size]
                print(f"DEBUG: Uploading batch {i//batch_size + 1}/{(len(documents) + batch_size - 1)//batch_size}", flush=True)
                
                self.vectorstore.add_documents(batch)
                
                # Small delay between batches
                if i + batch_size < len(documents):
                    time.sleep(1)
            
            print("✅ Successfully uploaded all documents to Pinecone", flush=True)
            
        except Exception as e:
            print(f"❌ Error uploading to Pinecone: {str(e)}", flush=True)
            raise

    def search_similar(self, query: str, k: int = 3) -> List[Dict]:
        """Search for similar documents in the vector database"""
        try:
            results = self.vectorstore.similarity_search_with_score(query, k=k)
            return [
                {
                    "content": doc.page_content,
                    "score": float(score),
                    "metadata": doc.metadata
                }
                for doc, score in results
            ]
        except Exception as e:
            print(f"❌ Error searching vectors: {str(e)}", flush=True)
            return []

    def test_connection(self):
        """Test the connection to Pinecone"""
        try:
            # Try a simple search to test connection
            test_results = self.vectorstore.similarity_search("test", k=1)
            print("✅ Pinecone connection test successful", flush=True)
            return True
        except Exception as e:
            print(f"❌ Pinecone connection test failed: {str(e)}", flush=True)
            return False

# === MAIN ===
if __name__ == "__main__":
    try:
        print("Script starting...", flush=True)
        print("DEBUG: Starting initialization...", flush=True)
        
        # Initialize vector database
        vector_db = RestaurantVectorDB()
        print("DEBUG: RestaurantVectorDB instance created", flush=True)
        
        # Test connection first
        if not vector_db.test_connection():
            print("❌ Failed to connect to Pinecone. Please check your configuration.", flush=True)
            exit(1)
        
        # Define data file path - try multiple possible locations
        possible_paths = [
            "rest.md",
            "data/rest.md", 
            "data/restaurant_data.txt",
            "restaurant_data.txt",
            "data/restaurant_info.md"
        ]
        
        data_path = None
        for path in possible_paths:
            if os.path.exists(path):
                data_path = path
                break
        
        if not data_path:
            print(f"❌ No data file found. Tried: {possible_paths}", flush=True)
            print("Please ensure your restaurant data file exists in one of these locations.", flush=True)
            exit(1)
        
        print(f"DEBUG: Using data file: {data_path}", flush=True)
        
        print("Processing documents...")
        docs = vector_db.process_restaurant_data(data_path)
        
        if not docs:
            print("❌ No documents were created from the data file", flush=True)
            exit(1)

        print("Uploading documents to Pinecone...")
        vector_db.upload_to_pinecone(docs)

        print("✅ Vector database setup completed successfully!")
        print(f"✅ Uploaded {len(docs)} document chunks to Pinecone", flush=True)
        
        # Test search functionality
        print("\n🔍 Testing search functionality...", flush=True)
        test_query = "restaurant menu"
        results = vector_db.search_similar(test_query, k=2)
        
        if results:
            print(f"✅ Search test successful! Found {len(results)} results for '{test_query}'", flush=True)
            for i, result in enumerate(results, 1):
                print(f"Result {i} (score: {result['score']:.4f}): {result['content'][:100]}...", flush=True)
        else:
            print("⚠️ Search test returned no results", flush=True)

    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()
