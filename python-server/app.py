from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv
from openai import OpenAI
from utils.restaurant_data import RESTAURANT_INFO, MENU_ITEMS, OPENING_HOURS, BRANCHES
from utils.vector_store import RestaurantVectorDB

# Load environment variables
load_dotenv()

# Ensure API key is set
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Initialize vector database for enhanced search
try:
    vector_db = RestaurantVectorDB()
    print("✅ Vector database initialized successfully")
except Exception as e:
    print(f"⚠️ Vector database initialization failed: {e}")
    vector_db = None

app = FastAPI(title="Somali Restaurant Chatbot API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[ChatMessage]

class ChatResponse(BaseModel):
    response: str
    sources: Optional[List[dict]] = None

@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        # Get the latest user message for vector search
        user_messages = [msg for msg in request.messages if msg.role == "user"]
        latest_query = user_messages[-1].content if user_messages else ""
        
        # Enhanced context with vector search results
        context = {
            "menu_items": MENU_ITEMS,
            "opening_hours": OPENING_HOURS,
            "branches": BRANCHES,
            "full_info": RESTAURANT_INFO
        }
        
        # Add vector search results if available
        vector_results = []
        if vector_db and latest_query:
            try:
                vector_results = vector_db.search_similar(latest_query, k=3)
                print(f"🔍 Found {len(vector_results)} relevant documents for query: {latest_query}")
            except Exception as e:
                print(f"⚠️ Vector search failed: {e}")
        
        # Enhanced system message with vector search context
        vector_context = ""
        if vector_results:
            vector_context = "\n\nAdditional relevant information from our database:\n"
            for i, result in enumerate(vector_results, 1):
                vector_context += f"{i}. {result['content'][:300]}...\n"

        system_message = f"""You are a helpful assistant for **Geediga Dahabka Restaurant**. Here is the structured information about the restaurant:

        1. Menu Items:
        {context['menu_items']}

        2. Opening Hours:
        {context['opening_hours']}

        3. Branch Locations:
        {context['branches']}

        4. Additional Information:
        {context['full_info']}
        
        {vector_context}

        Instructions:
        1. Always be polite and professional
        2. Format restaurant name as **Geediga Dahabka Restaurant**
        3. Format prices with emphasis (_$XX_)
        4. For menu items, include both price and description
        5. When showing menu items, group them by category (Fast Food, Drinks, Main Dishes, etc.)
        6. For fast food items, emphasize quick preparation and combo options
        7. For drinks, mention if they are hot/cold and any customization options
        8. For opening hours, mention any special notes/events
        9. For locations, include relevant contact info and features
        10. If asked about something not in the data, politely say you don't have that specific information
        11. Recommend dishes based on customer preferences when asked
        12. Provide accurate branch information when location-specific questions are asked
        13. Include business hours and special events when relevant
        14. When showing prices, always use the format: **Item Name** - $XX _Description_
        15. Use the additional relevant information from the database to provide more detailed and accurate responses"""

        # Prepare messages with system context
        messages = [
            {"role": "system", "content": system_message}
        ] + [{"role": msg.role, "content": msg.content} for msg in request.messages]

        # Get response from OpenAI
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=0.7,  # Add some creativity while keeping responses factual
            max_tokens=800   # Increased for more detailed responses
        )
        
        # Prepare sources from vector search
        sources = []
        if vector_results:
            sources = [
                {
                    "content": result["content"][:200] + "...",
                    "score": result["score"],
                    "metadata": result["metadata"]
                }
                for result in vector_results
            ]
        
        return ChatResponse(
            response=response.choices[0].message.content,
            sources=sources
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "vector_db_status": "connected" if vector_db else "disconnected"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001)
