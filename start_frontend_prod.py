#!/usr/bin/env python3
"""
Production startup script for AI Unity Game Generator Frontend
Optimized for cloud deployment
"""

import os
import sys
import subprocess

def main():
    """Start the Streamlit frontend in production mode"""
    
    # Get port from environment (required for cloud platforms)
    port = int(os.getenv("PORT", 8501))
    host = os.getenv("HOST", "0.0.0.0")
    backend_url = os.getenv("BACKEND_URL", "http://localhost:8000")
    
    print("🎮 Starting AI Unity Game Generator Frontend (Production Mode)...")
    print(f"🌐 Frontend will be available at: http://{host}:{port}")
    print(f"🔗 Backend URL: {backend_url}")
    
    # Start Streamlit with production settings
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", 
            "frontend/app.py",
            "--server.port", str(port),
            "--server.address", host,
            "--server.headless", "true",
            "--browser.gatherUsageStats", "false",
            "--server.enableCORS", "false",
            "--server.enableXsrfProtection", "false"
        ])
    except KeyboardInterrupt:
        print("\n👋 Frontend stopped!")

if __name__ == "__main__":
    main()

