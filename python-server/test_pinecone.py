"""
Test script to verify vector database functionality
"""
import os
import sys
from dotenv import load_dotenv

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.vector_store import RestaurantVectorDB

load_dotenv()

def test_search():
    """Test the vector search functionality"""
    print("🔍 Testing Vector Search Functionality", flush=True)
    print("=" * 50, flush=True)
    
    try:
        # Initialize vector database
        vector_db = RestaurantVectorDB()
        
        # Test queries
        test_queries = [
            "What Somali dishes do you have?",
            "vegetarian options",
            "spicy food",
            "rice dishes",
            "traditional Somali cuisine"
        ]
        
        for query in test_queries:
            print(f"\n🔎 Query: '{query}'", flush=True)
            print("-" * 30, flush=True)
            
            results = vector_db.search_similar(query, k=3)
            
            if results:
                for i, result in enumerate(results, 1):
                    print(f"Result {i} (Score: {result['score']:.4f}):", flush=True)
                    print(f"Content: {result['content'][:200]}...", flush=True)
                    print(f"Metadata: {result['metadata']}", flush=True)
                    print()
            else:
                print("No results found", flush=True)
        
        print("✅ Vector search test completed!", flush=True)
        
    except Exception as e:
        print(f"❌ Error during search test: {str(e)}", flush=True)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_search()
