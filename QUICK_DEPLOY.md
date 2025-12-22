# ⚡ Quick Deployment Guide

Choose your deployment method and follow the steps below.

---

## 🐳 Docker (Easiest - Recommended)

### Prerequisites
- Docker Desktop installed
- **Windows users:** See [DOCKER_SETUP_WINDOWS.md](DOCKER_SETUP_WINDOWS.md) for installation guide

### Steps

**Windows PowerShell:**
```powershell
# 1. Create .env file (copy from env.example)
Copy-Item env.example .env
# Edit .env and add your OPENAI_API_KEY (use: notepad .env)

# 2. Start services (try both commands if one doesn't work)
docker compose up -d
# OR
docker-compose up -d

# 3. Access
# Backend: http://localhost:8000
# Frontend: http://localhost:8501
```

**Linux/Mac:**
```bash
# 1. Create .env file (copy from env.example)
cp env.example .env
# Edit .env and add your OPENAI_API_KEY

# 2. Start services
docker compose up -d

# 3. Access
# Backend: http://localhost:8000
# Frontend: http://localhost:8501
```

---

## ☁️ Render (Free Tier Available)

> **Note**: For Render, you don't need a `.env` file. Set environment variables in the Render dashboard instead. See `env.example` for reference.

### Backend Deployment
1. Go to [render.com](https://render.com) → New → Web Service
2. Connect GitHub repository
3. Settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT`
   - **Environment**: Python 3
4. Add Environment Variable: `OPENAI_API_KEY` (see `env.example` for reference)
5. Add Persistent Disk: `generated_projects` (10GB)
6. Deploy!

### Frontend Deployment
1. New Web Service
2. Same repository
3. Settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run frontend/app.py --server.port $PORT --server.address 0.0.0.0 --server.headless=true`
4. Add Environment Variable: `BACKEND_URL=https://your-backend.onrender.com`
5. Deploy!

**Or use `render.yaml` for automatic deployment!**

---

## 🚂 Railway (Simplest)

1. Go to [railway.app](https://railway.app)
2. New Project → Deploy from GitHub
3. Select your repository
4. Add Environment Variable: `OPENAI_API_KEY`
5. Railway auto-detects and deploys!

For frontend, create a second service and set `BACKEND_URL`.

---

## 📝 Environment Variables

### Required
- `OPENAI_API_KEY` - Your OpenAI API key

### Optional
- `BACKEND_URL` - Backend URL (for frontend, default: `http://localhost:8000`)
- `PORT` - Server port (auto-set by cloud platforms)
- `ALLOWED_ORIGINS` - CORS origins (comma-separated, default: `*`)

---

## ✅ Post-Deployment Checklist

- [ ] Test health endpoint: `/health`
- [ ] Test API docs: `/docs`
- [ ] Test frontend UI
- [ ] Generate a test project
- [ ] Verify file downloads work
- [ ] Check logs for errors

---

## 🆘 Need Help?

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions and troubleshooting.

