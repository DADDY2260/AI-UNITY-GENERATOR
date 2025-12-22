#!/usr/bin/env python3
"""
Test script for AI Unity Game Generator
Verifies that all components are properly installed and configured
"""

import sys
import os
import importlib
from pathlib import Path
import dotenv

def test_imports():
    """Test if all required packages can be imported"""
    print("🔍 Testing package imports...")
    
    required_packages = [
        "fastapi",
        "uvicorn", 
        "streamlit",
        "openai",
        "jinja2",
        "dotenv",
        "pydantic",
        "requests"
    ]
    
    failed_imports = []
    
    for package in required_packages:
        try:
            importlib.import_module(package)
            print(f"  ✅ {package}")
        except ImportError as e:
            print(f"  ❌ {package}: {e}")
            failed_imports.append(package)
    
    if failed_imports:
        print(f"\n❌ Failed to import: {', '.join(failed_imports)}")
        print("💡 Run: pip install -r requirements.txt")
        return False
    
    print("✅ All packages imported successfully!")
    return True

def test_environment():
    """Test environment configuration"""
    print("\n🔍 Testing environment configuration...")
    
    # Load environment variables
    try:
        from dotenv import load_dotenv
        load_dotenv()
        print("  ✅ .env file loaded")
    except Exception as e:
        print(f"  ❌ Failed to load .env: {e}")
        return False
    
    # Check OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("  ❌ OPENAI_API_KEY not found in environment")
        print("  💡 Create a .env file with your OpenAI API key")
        return False
    elif api_key == "your_openai_api_key_here":
        print("  ❌ OPENAI_API_KEY is still the placeholder value")
        print("  💡 Replace with your actual OpenAI API key")
        return False
    else:
        print("  ✅ OPENAI_API_KEY found")
    
    return True

def test_project_structure():
    """Test if all required files and directories exist"""
    print("\n🔍 Testing project structure...")
    
    required_files = [
        "backend/app/main.py",
        "backend/app/llm/game_enhancer.py", 
        "backend/app/generators/unity_generator.py",
        "backend/app/templates/PlayerController.cs.j2",
        "backend/app/templates/GameManager.cs.j2",
        "frontend/app.py",
        "requirements.txt",
        "start_backend.py",
        "start_frontend.py"
    ]
    
    missing_files = []
    
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"  ✅ {file_path}")
        else:
            print(f"  ❌ {file_path}")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n❌ Missing files: {', '.join(missing_files)}")
        return False
    
    print("✅ All required files found!")
    return True

def test_backend_imports():
    """Test if backend modules can be imported"""
    print("\n🔍 Testing backend imports...")
    
    try:
        # Add backend to path
        sys.path.insert(0, str(Path("backend")))
        
        # Test imports
        from app.llm.game_enhancer import GameEnhancer
        from app.generators.unity_generator import UnityGenerator
        from app.main import app
        
        print("  ✅ GameEnhancer imported")
        print("  ✅ UnityGenerator imported") 
        print("  ✅ FastAPI app imported")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Backend import failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 AI Unity Game Generator - Setup Test")
    print("=" * 50)
    
    tests = [
        ("Package Imports", test_imports),
        ("Environment Config", test_environment),
        ("Project Structure", test_project_structure),
        ("Backend Imports", test_backend_imports)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"  ❌ {test_name} failed with exception: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Test Results:")
    
    passed = 0
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {status} {test_name}")
        if result:
            passed += 1
    
    print(f"\n🎯 {passed}/{len(results)} tests passed")
    
    if passed == len(results):
        print("\n🎉 All tests passed! Your setup is ready to go!")
        print("\n🚀 Next steps:")
        print("  1. Start the backend: python start_backend.py")
        print("  2. Start the frontend: python start_frontend.py")
        print("  3. Open http://localhost:8501 in your browser")
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above before running the application.")
        print("\n💡 Common fixes:")
        print("  - Run: pip install -r requirements.txt")
        print("  - Create .env file with your OpenAI API key")
        print("  - Check that all project files are present")

if __name__ == "__main__":
    main() 