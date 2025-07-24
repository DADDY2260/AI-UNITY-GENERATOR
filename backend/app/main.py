"""
AI Unity Game Prototype Generator - FastAPI Backend
Main application entry point
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
import os
from dotenv import load_dotenv
from fastapi.responses import FileResponse
import tempfile
from pathlib import Path
from openai import OpenAI
from PIL import Image
import base64

# Import our modules
from .llm.game_enhancer import GameEnhancer
from .generators.unity_generator import UnityGenerator
from .rag.rag_pipeline import RAGPipeline

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="AI Unity Game Generator",
    description="Generate Unity game prototypes from text descriptions",
    version="1.0.0"
)

# Add CORS middleware for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize our services
game_enhancer = GameEnhancer()
unity_generator = UnityGenerator()
rag_pipeline = RAGPipeline()

# Pydantic models for request/response
class GameIdeaRequest(BaseModel):
    description: str
    genre: str = "general"

class GameEnhancement(BaseModel):
    category: str  # "mechanics", "levels", "story"
    suggestions: List[str]
    description: str

class GameEnhancementResponse(BaseModel):
    original_idea: str
    enhancements: List[GameEnhancement]
    summary: str

class GenerateProjectRequest(BaseModel):
    original_idea: str
    selected_enhancements: Dict[str, List[str]]  # category -> selected suggestions
    genre: str = "general"

class GenerateProjectResponse(BaseModel):
    project_url: str
    file_count: int
    main_scripts: List[str]

class GenerateAssetsRequest(BaseModel):
    asset_types: list
    asset_descriptions: dict = {}
    models: list
    game_description: str
    genre: str = "general"
    project_folder_name: str = ""

class GenerateAssetsResponse(BaseModel):
    status: str
    message: str
    generated_files: list = []

class KnowledgeBaseRequest(BaseModel):
    category: str
    subcategory: str
    content: List[str]

class KnowledgeBaseResponse(BaseModel):
    status: str
    message: str
    stats: Dict[str, Any] = {}

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "AI Unity Game Generator API",
        "status": "running",
        "version": "1.0.0"
    }

@app.post("/enhance-idea", response_model=GameEnhancementResponse)
async def enhance_game_idea(request: GameIdeaRequest):
    """
    Take a game idea and suggest enhancements
    """
    try:
        # Use our LLM to enhance the game idea
        enhancements = await game_enhancer.enhance_idea(
            request.description, 
            request.genre
        )
        
        return GameEnhancementResponse(
            original_idea=request.description,
            enhancements=[e.dict() for e in enhancements],
            summary=f"Enhanced {request.description} with {len(enhancements)} categories of suggestions"
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error enhancing idea: {str(e)}")

@app.post("/generate-project", response_model=GenerateProjectResponse)
async def generate_unity_project(request: GenerateProjectRequest):
    """
    Generate Unity project files based on idea and selected enhancements
    """
    try:
        # Generate the Unity project
        project_info = await unity_generator.generate_project(
            request.original_idea,
            request.selected_enhancements,
            request.genre
        )
        
        return GenerateProjectResponse(
            project_url=project_info["download_url"],
            file_count=project_info["file_count"],
            main_scripts=project_info["main_scripts"]
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating project: {str(e)}")

@app.post("/generate-assets", response_model=GenerateAssetsResponse)
async def generate_assets(request: GenerateAssetsRequest):
    """
    Generate placeholder assets using AI (DALL·E, Stable Diffusion, etc.)
    """
    # Determine output directory
    if request.project_folder_name:
        output_dir = Path("generated_projects") / request.project_folder_name / "Assets" / "Textures"
    else:
        output_dir = Path("generated_projects/ai_assets")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Prepare OpenAI client
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return GenerateAssetsResponse(status="error", message="OPENAI_API_KEY not set", generated_files=[])
    openai_client = OpenAI(api_key=api_key)
    
    generated_files = []
    errors = []
    for asset_type in request.asset_types:
        # Use user-provided description if available
        user_prompt = request.asset_descriptions.get(asset_type, "").strip()
        if user_prompt:
            prompt = user_prompt
        else:
            prompt = f"A {asset_type.lower()} for a video game, game-ready, transparent background."
        if "DALL·E" in request.models:
            try:
                print(f"[DALL·E PROMPT] {prompt}")
                response = openai_client.images.generate(
                    model="dall-e-3",
                    prompt=prompt,
                    n=1,
                    size="1024x1024"
                )
                image_url = response.data[0].url
                # Download the image
                import requests as pyrequests
                img_data = pyrequests.get(image_url).content
                asset_filename = f"{asset_type.replace(' ', '_').lower()}_dalle.png"
                asset_path = output_dir / asset_filename
                with open(asset_path, "wb") as f:
                    f.write(img_data)
                # Return relative path from project root if project_folder_name is set
                if request.project_folder_name:
                    rel_path = str(Path("Assets") / "Textures" / asset_filename)
                else:
                    rel_path = str(asset_path)
                generated_files.append(rel_path)
            except Exception as e:
                print(f"[DALL·E ERROR] {e}")
                errors.append(f"DALL·E error for {asset_type}: {e}")
        if "Stable Diffusion" in request.models:
            # Stub for now
            errors.append(f"Stable Diffusion not yet implemented (asset: {asset_type})")
    msg = "Assets generated successfully." if generated_files else "No assets generated. "
    if errors:
        msg += " Errors: " + "; ".join(errors)
    return GenerateAssetsResponse(
        status="success" if generated_files else "error",
        message=msg,
        generated_files=generated_files
    )

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Simple chat endpoint for MVP: takes a user message and returns an LLM-generated response.
    """
    try:
        # For MVP, just echo the message through the LLM (could use RAG or a simple prompt)
        prompt = f"You are an expert Unity game developer assistant. Answer the following user request or question as helpfully as possible, with Unity/C# code if relevant.\nUser: {request.message}"
        # Use the game_enhancer's LLM pipeline for generation
        response = game_enhancer.generator(prompt, max_new_tokens=512, temperature=0.7, do_sample=True)
        content = response[0]["generated_text"]
        return ChatResponse(response=content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in chat: {str(e)}")

@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "services": {
            "llm": "available" if os.getenv("OPENAI_API_KEY") else "missing_api_key",
            "unity_generator": "available"
        }
    }

@app.get("/download/{filename}")
def download_project(filename: str):
    """Serve the generated Unity project zip file for download"""
    from pathlib import Path
    generated_dir = Path("generated_projects")
    file_path = generated_dir / filename
    if file_path.exists():
        return FileResponse(str(file_path), filename=filename, media_type="application/zip")
    return {"error": f"File {filename} not found."}

# RAG Knowledge Base Management Endpoints
@app.get("/rag/stats")
async def get_rag_stats():
    """Get statistics about the RAG knowledge base"""
    try:
        stats = rag_pipeline.get_knowledge_base_stats()
        return {
            "status": "success",
            "stats": stats
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting RAG stats: {str(e)}")

@app.post("/rag/add-knowledge", response_model=KnowledgeBaseResponse)
async def add_knowledge_to_rag(request: KnowledgeBaseRequest):
    """Add new knowledge to the RAG knowledge base"""
    try:
        rag_pipeline.add_to_knowledge_base(
            request.category,
            request.subcategory,
            request.content
        )
        
        stats = rag_pipeline.get_knowledge_base_stats()
        
        return KnowledgeBaseResponse(
            status="success",
            message=f"Added {len(request.content)} items to {request.category}/{request.subcategory}",
            stats=stats
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding knowledge: {str(e)}")

@app.get("/rag/search")
async def search_rag_knowledge(query: str, top_k: int = 5):
    """Search the RAG knowledge base"""
    try:
        results = rag_pipeline.retrieve_relevant_info(query, top_k)
        return {
            "status": "success",
            "query": query,
            "results": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error searching knowledge base: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 