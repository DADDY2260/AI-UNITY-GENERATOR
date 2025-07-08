#!/usr/bin/env python3
"""
Startup script for AI Unity Game Generator Frontend
"""

import os
import sys
import subprocess
import time
import requests

def check_backend():
    """Check if the backend is running"""
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        return response.status_code == 200
    except:
        return False

def main():
    """Start the Streamlit frontend"""
    
    print("🎮 Starting AI Unity Game Generator Frontend...")
    
    # Check if backend is running
    print("🔍 Checking if backend is running...")
    if not check_backend():
        print("❌ Backend server is not running!")
        print("📝 Please start the backend first:")
        print("   python start_backend.py")
        print("\n💡 Or in a separate terminal:")
        print("   cd backend")
        print("   uvicorn app.main:app --reload")
        sys.exit(1)
    
    print("✅ Backend is running!")
    print("🌐 Frontend will be available at: http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the server")
    print("-" * 50)
    
    # Start Streamlit
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", 
            "frontend/app.py",
            "--server.port", "8501",
            "--server.address", "localhost"
        ])
    except KeyboardInterrupt:
        print("\n👋 Frontend stopped!")

if __name__ == "__main__":
    main() 