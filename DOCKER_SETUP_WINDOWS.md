# 🐳 Docker Setup Guide for Windows

## Step 1: Install Docker Desktop

1. **Download Docker Desktop for Windows:**
   - Go to: https://www.docker.com/products/docker-desktop/
   - Click "Download for Windows"
   - The installer will be `Docker Desktop Installer.exe`

2. **Install Docker Desktop:**
   - Run the installer
   - Follow the installation wizard
   - **Important:** Make sure "Use WSL 2 instead of Hyper-V" is checked (if available)
   - Restart your computer when prompted

3. **Start Docker Desktop:**
   - Launch Docker Desktop from the Start menu
   - Wait for Docker to start (you'll see a whale icon in the system tray)
   - Docker Desktop may ask you to enable WSL 2 - follow the prompts

4. **Verify Installation:**
   Open PowerShell and run:
   ```powershell
   docker --version
   docker compose version
   ```
   
   You should see version numbers for both commands.

## Step 2: Deploy Your Project

Once Docker is installed, follow these steps:

1. **Make sure you have a `.env` file:**
   ```powershell
   # Copy the example file
   Copy-Item env.example .env
   
   # Edit .env and add your OpenAI API key
   notepad .env
   ```

2. **Build and start the containers:**
   ```powershell
   docker compose up -d
   ```
   
   **Note:** On newer Docker versions, use `docker compose` (with space) instead of `docker-compose` (with hyphen).

3. **Check if containers are running:**
   ```powershell
   docker compose ps
   ```

4. **View logs:**
   ```powershell
   docker compose logs -f
   ```

5. **Access your application:**
   - Backend API: http://localhost:8000
   - Frontend UI: http://localhost:8501
   - API Docs: http://localhost:8000/docs

6. **Stop the containers:**
   ```powershell
   docker compose down
   ```

## Troubleshooting

### If `docker compose` doesn't work, try:
```powershell
docker-compose up -d
```

### If you get permission errors:
- Make sure Docker Desktop is running
- Right-click Docker Desktop → Settings → General → Enable "Use the WSL 2 based engine"

### If ports are already in use:
- Stop any local servers running on ports 8000 or 8501
- Or modify `docker-compose.yml` to use different ports

### Check Docker Desktop status:
- Look for the Docker whale icon in your system tray
- Right-click → "Open Docker Desktop" to see the dashboard

## Next Steps

Once Docker is running, you can:
- Deploy to cloud platforms (Render, Railway, etc.)
- Scale your application
- Use Docker for production deployments

