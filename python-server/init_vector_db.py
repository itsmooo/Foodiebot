import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.vector_store import RestaurantVectorDB
from utils.restaurant_data import RESTAURANT_INFO

# Load environment variables
load_dotenv()

def main():
    """Initialize the vector database with comprehensive restaurant data"""
    print("🚀 Initializing Vector Database with Comprehensive Restaurant Data")
    print("=" * 70)
    
    try:
        print("DEBUG: Starting initialization...", flush=True)
        
        # Initialize vector database
        vector_db = RestaurantVectorDB()
        print("DEBUG: RestaurantVectorDB instance created", flush=True)
        
        # Test connection first
        if not vector_db.test_connection():
            print("❌ Failed to connect to Pinecone. Please check your configuration.", flush=True)
            return
        
        # Create temporary data file from restaurant_data.py
        print("📄 Creating temporary data file from restaurant_data.py...")
        
        temp_data_path = "temp_restaurant_data.txt"
        
        with open(temp_data_path, 'w', encoding='utf-8') as f:
            f.write(RESTAURANT_INFO)
        
        print(f"✅ Created temporary data file: {temp_data_path}")
        print(f"📊 Data size: {len(RESTAURANT_INFO)} characters")
        
        # Process the restaurant data
        print("🔄 Processing restaurant data...")
        documents = vector_db.process_restaurant_data(temp_data_path)
        
        if not documents:
            print("❌ No documents were created from the data", flush=True)
            return
        
        print(f"📄 Processed {len(documents)} document chunks")
        
        # Show sample of what will be uploaded
        print("\n📋 Sample of content being uploaded:")
        for i, doc in enumerate(documents[:3]):
            print(f"Chunk {i+1}: {doc.page_content[:100]}...")
        
        # Upload to Pinecone
        print(f"\n🔄 Uploading {len(documents)} documents to Pinecone...")
        vector_db.upload_to_pinecone(documents)
        
        # Clean up temporary file
        os.remove(temp_data_path)
        print(f"🗑️ Cleaned up temporary file")
        
        print("✅ Vector database initialization completed successfully!", flush=True)
        print(f"✅ Uploaded {len(documents)} document chunks to Pinecone", flush=True)
        
        # Test search functionality with restaurant-specific queries
        print("\n🔍 Testing search functionality with restaurant queries...")
        
        test_queries = [
            "What's on the menu?",
            "Opening hours",
            "Bariis Iskukaris price",
            "Camel meat steak",
            "Delivery information",
            "Branch locations",
            "Special offers Monday",
            "Vegetarian options",
            "Desserts halwo",
            "Beverages and shakes",
            "Ladies night Thursday",
            "Contact phone number"
        ]
        
        successful_tests = 0
        
        for query in test_queries:
            print(f"\n🔎 Testing: '{query}'")
            results = vector_db.search_similar(query, k=2)
            
            if results:
                successful_tests += 1
                print(f"   ✅ Found {len(results)} results")
                for i, result in enumerate(results, 1):
                    print(f"   Result {i} (score: {result['score']:.4f}): {result['content'][:80]}...")
            else:
                print("   ⚠️ No results found")
        
        print(f"\n📊 Search Test Results: {successful_tests}/{len(test_queries)} successful")
        
        if successful_tests >= len(test_queries) * 0.8:
            print("🎉 Excellent! Vector database is working great!")
        else:
            print("⚠️ Some searches failed. You may need to check the data.")
        
        print("\n🎉 Comprehensive vector database setup completed!")
        print("Your chatbot now has access to:")
        print("- Complete menu with 60+ items and prices")
        print("- All 4 branch locations with details")
        print("- Opening hours and special events")
        print("- Services and special offers")
        print("- Restaurant history and awards")
        print("- Staff information and contact details")
        print("- Delivery zones and pricing")
        print("- Customer reviews and FAQs")
        print("- And much more!")
            
    except FileNotFoundError as e:
        print(f"❌ File not found: {str(e)}", flush=True)
        
    except ValueError as e:
        print(f"❌ Configuration error: {str(e)}", flush=True)
        print("Please check your environment variables in .env file.", flush=True)
        
    except Exception as e:
        print(f"❌ Error initializing vector database: {str(e)}", flush=True)
        print("\nDEBUG: Full error:", flush=True)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
