#!/usr/bin/env python3
"""
Startup script for AI Unity Game Generator Backend
"""

import os
import sys
import uvicorn
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    """Start the FastAPI backend server"""
    
    # Note: Using DistillGPT - no API key required
    print("ℹ️  Using DistillGPT - no API key required")
    
    print("🚀 Starting AI Unity Game Generator Backend...")
    print("📡 Server will be available at: http://localhost:8000")
    print("📚 API documentation at: http://localhost:8000/docs")
    print("🔧 Health check at: http://localhost:8000/health")
    print("\n⏹️  Press Ctrl+C to stop the server")
    print("-" * 50)
    
    # Start the server
    uvicorn.run(
        "backend.app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main() 