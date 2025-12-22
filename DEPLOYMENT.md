# 🚀 Deployment Guide - AI Unity Game Generator

This guide covers multiple deployment options for the AI Unity Game Generator. Choose the method that best fits your needs.

---

## 📋 Pre-Deployment Checklist

Before deploying, ensure you have:

- ✅ **OpenAI API Key** with sufficient credits
- ✅ **Git repository** with your code pushed
- ✅ **Environment variables** documented
- ✅ **Dependencies** listed in `requirements.txt`
- ✅ **Generated projects directory** configured for persistence

---

## 🐳 Option 1: Docker Deployment (Recommended)

Docker allows you to deploy the entire application in containers, making it portable and easy to manage.

### Prerequisites
- Docker installed ([Get Docker](https://www.docker.com/get-started))
- Docker Compose installed

### Steps

1. **Build and run with Docker Compose:**
   ```bash
   docker-compose up -d
   ```

2. **Access the application:**
   - Backend API: http://localhost:8000
   - Frontend UI: http://localhost:8501
   - API Docs: http://localhost:8000/docs

3. **View logs:**
   ```bash
   docker-compose logs -f
   ```

4. **Stop the application:**
   ```bash
   docker-compose down
   ```

### Environment Variables

Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### Production Docker Deployment

For production, you can deploy Docker containers to:
- **AWS ECS/Fargate**
- **Google Cloud Run**
- **Azure Container Instances**
- **DigitalOcean App Platform**

---

## ☁️ Option 2: Render Deployment

[Render](https://render.com) offers free tier hosting with automatic SSL and easy deployment.

### Deploy Backend

1. **Create a new Web Service** on Render
2. **Connect your GitHub repository**
3. **Configure the service:**
   - **Name**: `ai-unity-generator-backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT`
   - **Plan**: Free (or Starter for production)

4. **Add Environment Variables:**
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `PYTHON_VERSION`: `3.11.0`

5. **Add Persistent Disk** (for generated projects):
   - Name: `generated-projects`
   - Mount Path: `/opt/render/project/src/generated_projects`
   - Size: 10 GB

6. **Deploy!**

### Deploy Frontend

1. **Create a new Web Service** on Render
2. **Connect your GitHub repository**
3. **Configure the service:**
   - **Name**: `ai-unity-generator-frontend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run frontend/app.py --server.port $PORT --server.address 0.0.0.0 --server.headless=true`
   - **Plan**: Free

4. **Add Environment Variables:**
   - `BACKEND_URL`: `https://ai-unity-generator-backend.onrender.com` (your backend URL)
   - `PYTHON_VERSION`: `3.11.0`

5. **Deploy!**

### Using Render Blueprint

Alternatively, use the `render.yaml` file for automatic deployment:

1. Push `render.yaml` to your repository
2. Go to Render Dashboard → New → Blueprint
3. Connect your repository
4. Render will automatically detect and deploy both services

---

## 🚂 Option 3: Railway Deployment

[Railway](https://railway.app) offers simple deployment with automatic HTTPS.

### Steps

1. **Sign up** at [railway.app](https://railway.app)

2. **Create a new project** and connect your GitHub repository

3. **Add a new service** and select your repository

4. **Configure environment variables:**
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `PORT`: Railway sets this automatically

5. **Railway will auto-detect** Python and install dependencies

6. **For the frontend**, create a second service:
   - Set `BACKEND_URL` environment variable to your backend service URL
   - Railway provides service URLs automatically

### Using Railway CLI

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Deploy
railway up
```

---

## 🎯 Option 4: Heroku Deployment

Heroku is a popular platform for Python applications.

### Prerequisites
- Heroku account ([Sign up](https://heroku.com))
- Heroku CLI installed

### Deploy Backend

1. **Login to Heroku:**
   ```bash
   heroku login
   ```

2. **Create a new app:**
   ```bash
   heroku create ai-unity-generator-backend
   ```

3. **Set environment variables:**
   ```bash
   heroku config:set OPENAI_API_KEY=your_api_key
   ```

4. **Add persistent storage** (for generated projects):
   ```bash
   heroku addons:create heroku-postgresql:mini  # Or use Heroku Redis
   ```

5. **Deploy:**
   ```bash
   git push heroku main
   ```

### Deploy Frontend

1. **Create a second app:**
   ```bash
   heroku create ai-unity-generator-frontend
   ```

2. **Set environment variables:**
   ```bash
   heroku config:set BACKEND_URL=https://ai-unity-generator-backend.herokuapp.com
   ```

3. **Deploy:**
   ```bash
   git push heroku main
   ```

**Note:** Heroku free tier has been discontinued. Consider other options for free hosting.

---

## 🌐 Option 5: Vercel/Netlify (Frontend Only)

For a more modern frontend deployment, you can deploy the Streamlit app to Vercel or Netlify, but this requires additional configuration.

### Alternative: Deploy Frontend Separately

Consider rebuilding the frontend as a React/Vue app for better deployment options on Vercel/Netlify.

---

## 🔧 Option 6: Self-Hosted (VPS)

Deploy on your own server (DigitalOcean, Linode, AWS EC2, etc.)

### Steps

1. **SSH into your server:**
   ```bash
   ssh user@your-server-ip
   ```

2. **Install dependencies:**
   ```bash
   sudo apt update
   sudo apt install python3.11 python3-pip nginx
   ```

3. **Clone your repository:**
   ```bash
   git clone https://github.com/yourusername/ai-unity-generator.git
   cd ai-unity-generator
   ```

4. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

5. **Set up systemd service** for backend:
   ```bash
   sudo nano /etc/systemd/system/unity-generator-backend.service
   ```
   
   Add:
   ```ini
   [Unit]
   Description=AI Unity Generator Backend
   After=network.target

   [Service]
   User=your-username
   WorkingDirectory=/path/to/ai-unity-generator
   Environment="PATH=/path/to/ai-unity-generator/venv/bin"
   Environment="OPENAI_API_KEY=your_api_key"
   ExecStart=/path/to/ai-unity-generator/venv/bin/uvicorn backend.app.main:app --host 0.0.0.0 --port 8000
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

6. **Start the service:**
   ```bash
   sudo systemctl start unity-generator-backend
   sudo systemctl enable unity-generator-backend
   ```

7. **Configure Nginx** as reverse proxy:
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://localhost:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

8. **Set up SSL with Let's Encrypt:**
   ```bash
   sudo apt install certbot python3-certbot-nginx
   sudo certbot --nginx -d your-domain.com
   ```

---

## 🔐 Environment Variables

### Required Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | `sk-...` |

### Optional Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `BACKEND_URL` | Backend API URL (for frontend) | `http://localhost:8000` |
| `PORT` | Server port | `8000` (backend), `8501` (frontend) |
| `PYTHON_VERSION` | Python version | `3.11.0` |

---

## 📦 Storage Considerations

### Generated Projects

The application generates Unity projects that need persistent storage:

- **Local deployment**: Files stored in `generated_projects/` directory
- **Cloud deployment**: Use persistent volumes/disks
- **Docker**: Use volumes to persist data
- **Render**: Use persistent disks
- **Railway**: Use volumes or external storage (S3, etc.)

### Recommended: External Storage

For production, consider using:
- **AWS S3** for file storage
- **Google Cloud Storage**
- **Azure Blob Storage**
- **Cloudinary** for asset storage

---

## 🚨 Production Considerations

### Security

1. **API Keys**: Never commit API keys to Git
2. **CORS**: Configure CORS properly for production
3. **Rate Limiting**: Add rate limiting to prevent abuse
4. **HTTPS**: Always use HTTPS in production
5. **Environment Variables**: Use secure environment variable management

### Performance

1. **Caching**: Implement caching for API responses
2. **CDN**: Use CDN for static assets
3. **Database**: Consider adding a database for user sessions/projects
4. **Load Balancing**: Use load balancers for high traffic

### Monitoring

1. **Logging**: Set up proper logging (e.g., Sentry, LogRocket)
2. **Health Checks**: Monitor `/health` endpoint
3. **Metrics**: Track API usage and performance
4. **Alerts**: Set up alerts for errors and downtime

---

## 🧪 Testing Deployment

After deployment, test:

1. **Health Check**: `GET /health`
2. **API Docs**: Visit `/docs` endpoint
3. **Frontend**: Access the Streamlit UI
4. **Generate Project**: Test full workflow
5. **Download**: Verify file downloads work

---

## 📞 Troubleshooting

### Common Issues

**Backend won't start:**
- Check environment variables are set
- Verify OpenAI API key is valid
- Check logs for errors

**Frontend can't connect to backend:**
- Verify `BACKEND_URL` is correct
- Check CORS settings
- Ensure backend is running

**Generated projects not persisting:**
- Verify volume mounts are configured
- Check file permissions
- Ensure storage is writable

**Out of memory errors:**
- Upgrade to a larger instance
- Optimize model loading
- Use smaller models

---

## 🎉 Next Steps

After deployment:

1. **Set up a custom domain**
2. **Configure SSL certificates**
3. **Set up monitoring and alerts**
4. **Implement user authentication** (optional)
5. **Add analytics** (optional)
6. **Set up CI/CD** for automatic deployments

---

## 📚 Additional Resources

- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
- [Streamlit Cloud](https://streamlit.io/cloud)
- [Docker Documentation](https://docs.docker.com/)
- [Render Documentation](https://render.com/docs)
- [Railway Documentation](https://docs.railway.app/)

---

**Need help?** Open an issue on GitHub or check the project documentation!

