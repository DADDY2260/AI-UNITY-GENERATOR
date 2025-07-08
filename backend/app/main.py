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

# Import our modules
from .llm.game_enhancer import GameEnhancer
from .generators.unity_generator import UnityGenerator

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

class GenerateProjectResponse(BaseModel):
    project_url: str
    file_count: int
    main_scripts: List[str]

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
            request.selected_enhancements
        )
        
        return GenerateProjectResponse(
            project_url=project_info["download_url"],
            file_count=project_info["file_count"],
            main_scripts=project_info["main_scripts"]
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating project: {str(e)}")

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 