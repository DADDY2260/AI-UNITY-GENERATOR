#!/usr/bin/env python3
"""
Production startup script for AI Unity Game Generator Backend
Optimized for cloud deployment
"""

import os
import uvicorn
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    """Start the FastAPI backend server in production mode"""
    
    # Get port from environment (required for cloud platforms)
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    
    # Check for required environment variables
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Warning: OPENAI_API_KEY not set. Some features may not work.")
    
    print("🚀 Starting AI Unity Game Generator Backend (Production Mode)...")
    print(f"📡 Server will be available at: http://{host}:{port}")
    print(f"📚 API documentation at: http://{host}:{port}/docs")
    print(f"🔧 Health check at: http://{host}:{port}/health")
    
    # Start the server with production settings
    uvicorn.run(
        "backend.app.main:app",
        host=host,
        port=port,
        reload=False,  # Disable reload in production
        log_level=os.getenv("LOG_LEVEL", "info"),
        workers=1,  # For cloud platforms, use 1 worker (or set via env var)
        access_log=True
    )

if __name__ == "__main__":
    main()

