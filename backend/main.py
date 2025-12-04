from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import auth, admin, chat
from backend.services.sqlite_client import init_db
from backend.services.langsmith_client import setup_langsmith
from backend.utils.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, specify domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    setup_langsmith()
    await init_db()
    
    # Setup LLM Cache
    try:
        from langchain_community.cache import SQLiteCache
        import os
        import langchain
        
        # Ensure directory exists if path contains directory
        cache_dir = os.path.dirname(settings.LLM_CACHE_PATH)
        if cache_dir and not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
            
        cache = SQLiteCache(database_path=settings.LLM_CACHE_PATH)
            
        try:
            # Try new way (LangChain >= 0.1.0)
            from langchain.globals import set_llm_cache
            set_llm_cache(cache)
        except ImportError:
            # Fallback to old way (LangChain < 0.1.0)
            langchain.llm_cache = cache
            
        print(f"LLM Cache initialized at {settings.LLM_CACHE_PATH}")
    except Exception as e:
        print(f"Failed to initialize LLM Cache: {e}")

app.include_router(auth.router, prefix=settings.API_V1_STR + "/auth")
app.include_router(admin.router, prefix=settings.API_V1_STR)
app.include_router(chat.router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    return {"message": "RAG Web API is running"}
