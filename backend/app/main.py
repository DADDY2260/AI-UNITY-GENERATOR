"""
AI Unity Game Prototype Generator - FastAPI Backend
Main application entry point

This module defines the FastAPI backend for the AI Unity Game Generator.
It provides endpoints for enhancing game ideas, generating Unity projects and assets,
chatting with an AI assistant, and managing a RAG (Retrieval-Augmented Generation) knowledge base.
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
    """Request model for submitting a game idea and genre."""
    description: str
    genre: str = "general"

class GameEnhancement(BaseModel):
    """Model for a single game enhancement category and its suggestions."""
    category: str  # e.g., "mechanics", "levels", "story"
    suggestions: List[str]
    description: str

class GameEnhancementResponse(BaseModel):
    """Response model for enhanced game idea suggestions."""
    original_idea: str
    enhancements: List[GameEnhancement]
    summary: str

class GenerateProjectRequest(BaseModel):
    """Request model for generating a Unity project from an idea and selected enhancements."""
    original_idea: str
    selected_enhancements: Dict[str, List[str]]  # category -> selected suggestions
    genre: str = "general"

class GenerateProjectResponse(BaseModel):
    """Response model for generated Unity project details."""
    project_url: str
    file_count: int
    main_scripts: List[str]

class GenerateAssetsRequest(BaseModel):
    """Request model for generating placeholder assets using AI models."""
    asset_types: list
    asset_descriptions: dict = {}
    models: list
    game_description: str
    genre: str = "general"
    project_folder_name: str = ""

class GenerateAssetsResponse(BaseModel):
    """Response model for generated asset files."""
    status: str
    message: str
    generated_files: list = []

class KnowledgeBaseRequest(BaseModel):
    """Request model for adding knowledge to the RAG knowledge base."""
    category: str
    subcategory: str
    content: List[str]

class KnowledgeBaseResponse(BaseModel):
    """Response model for RAG knowledge base operations."""
    status: str
    message: str
    stats: Dict[str, Any] = {}

class ChatRequest(BaseModel):
    """Request model for the chat endpoint."""
    message: str

class ChatResponse(BaseModel):
    """Response model for the chat endpoint."""
    response: str

@app.get("/")
async def root():
    """Health check endpoint for the API root."""
    return {
        "message": "AI Unity Game Generator API",
        "status": "running",
        "version": "1.0.0"
    }

@app.post("/enhance-idea", response_model=GameEnhancementResponse)
async def enhance_game_idea(request: GameIdeaRequest):
    """
    Enhance a game idea by suggesting improvements across various categories using LLM and RAG.
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
    Generate Unity project files based on the user's idea and selected enhancements.
    Returns a download URL and summary of generated scripts.
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
    Generate placeholder assets (e.g., images) using AI models like DALL·E or Stable Diffusion.
    """
    # Determine output directory for assets
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
        # Create a more structured prompt for Unity game development
        system_prompt = """You are an expert Unity game developer assistant. You help users with:
- Unity C# scripting
- Game mechanics and design
- Unity project structure
- Performance optimization
- Best practices for game development

Always provide practical, actionable advice with code examples when relevant.
Keep responses concise but helpful."""

        user_prompt = f"{system_prompt}\n\nUser question: {request.message}\n\nAssistant:"
        
        # Use the game_enhancer's LLM pipeline for generation
        response = game_enhancer.generator(user_prompt, max_new_tokens=256, temperature=0.7, do_sample=True)
        content = response[0]["generated_text"]
        
        # Extract just the assistant's response (remove the prompt)
        if "Assistant:" in content:
            content = content.split("Assistant:")[-1].strip()
        
        # Check for repetitive or poor quality responses
        if (len(content) < 20 or 
            "I don't know" in content.lower() or
            content.count("Unity C#") > 3 or
            content.count("Unity") > 5 or
            len(set(content.split())) < 5):  # Too few unique words
            
            # Provide a helpful default response based on the question
            question_lower = request.message.lower()
            
            if "player controller" in question_lower or "player" in question_lower:
                content = """Here's how to create a basic player controller in Unity:

```csharp
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public float speed = 5f;
    public float jumpForce = 5f;
    private Rigidbody2D rb;
    private bool isGrounded;

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
    }

    void Update()
    {
        // Horizontal movement
        float moveInput = Input.GetAxisRaw("Horizontal");
        rb.velocity = new Vector2(moveInput * speed, rb.velocity.y);

        // Jumping
        if (Input.GetKeyDown(KeyCode.Space) && isGrounded)
        {
            rb.AddForce(Vector2.up * jumpForce, ForceMode2D.Impulse);
            isGrounded = false;
        }
    }

    void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.CompareTag("Ground"))
        {
            isGrounded = true;
        }
    }
}
```

Key points:
• Use Rigidbody2D for physics-based movement
• Check for ground collision for jumping
• Use Input.GetAxisRaw for smooth movement
• Apply forces for jumping instead of directly setting velocity"""
                
            elif "collision" in question_lower or "collision detection" in question_lower:
                content = """Unity collision detection best practices:

**2D Collision:**
```csharp
void OnCollisionEnter2D(Collision2D collision)
{
    if (collision.gameObject.CompareTag("Enemy"))
    {
        // Handle enemy collision
    }
}
```

**Trigger Collision (for pickups):**
```csharp
void OnTriggerEnter2D(Collider2D other)
{
    if (other.CompareTag("Pickup"))
    {
        // Handle pickup
        Destroy(other.gameObject);
    }
}
```

**Tips:**
• Use tags to identify objects
• Use triggers for pickups, not solid collisions
• Check layer collision matrix in Project Settings
• Use Rigidbody2D for physics-based collisions"""
                
            elif "performance" in question_lower or "optimize" in question_lower:
                content = """Unity performance optimization tips:

**Code Optimization:**
• Use Object Pooling for frequently spawned objects
• Cache component references in Start()
• Use Update() sparingly, prefer events
• Avoid GetComponent() in Update()

**Rendering:**
• Use LOD (Level of Detail) for distant objects
• Minimize draw calls with batching
• Use occlusion culling for large scenes
• Optimize textures and models

**Memory:**
• Destroy unused objects
• Use object pooling for bullets/enemies
• Minimize garbage collection
• Profile with Unity Profiler

**Example Object Pooling:**
```csharp
public class ObjectPool : MonoBehaviour
{
    public GameObject prefab;
    public int poolSize = 20;
    private List<GameObject> pool;

    void Start()
    {
        pool = new List<GameObject>();
        for (int i = 0; i < poolSize; i++)
        {
            GameObject obj = Instantiate(prefab);
            obj.SetActive(false);
            pool.Add(obj);
        }
    }

    public GameObject GetPooledObject()
    {
        for (int i = 0; i < pool.Count; i++)
        {
            if (!pool[i].activeInHierarchy)
            {
                return pool[i];
            }
        }
        return null;
    }
}
```"""
                
            else:
                content = f"I understand you're asking about '{request.message}'. For Unity game development, here are some general tips:\n\n"
                content += "• Always use proper C# naming conventions (PascalCase for classes, camelCase for variables)\n"
                content += "• Consider performance when designing game mechanics\n"
                content += "• Use Unity's built-in components when possible\n"
                content += "• Test your code thoroughly before implementing\n"
                content += "• Use the Unity Profiler to identify performance bottlenecks\n\n"
                content += "Could you provide more specific details about what you're trying to achieve?"
        
        return ChatResponse(response=content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in chat: {str(e)}")

@app.get("/health")
async def health_check():
    """Detailed health check endpoint for backend and services."""
    return {
        "status": "healthy",
        "services": {
            "llm": "available" if os.getenv("OPENAI_API_KEY") else "missing_api_key",
            "unity_generator": "available"
        }
    }

@app.get("/download/{filename}")
def download_project(filename: str):
    """
    Serve the generated Unity project zip file for download.
    """
    from pathlib import Path
    generated_dir = Path("generated_projects")
    file_path = generated_dir / filename
    if file_path.exists():
        return FileResponse(str(file_path), filename=filename, media_type="application/zip")
    return {"error": f"File {filename} not found."}

# RAG Knowledge Base Management Endpoints
@app.get("/rag/stats")
async def get_rag_stats():
    """Get statistics about the RAG knowledge base."""
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
    """
    Add new knowledge to the RAG knowledge base.
    """
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
    """
    Search the RAG knowledge base for relevant information.
    """
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