# Heroku Procfile for AI Unity Game Generator
# For Heroku deployment, you'll need to deploy backend and frontend separately
# or use a single dyno with both services

# Backend (FastAPI)
web: uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT

# Frontend (Streamlit) - Uncomment if deploying separately
# frontend: streamlit run frontend/app.py --server.port $PORT --server.address 0.0.0.0 --server.headless=true

