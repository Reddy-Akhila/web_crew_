# Installation & Setup Guide

## Quick Start (5 minutes)

### Option 1: Windows PowerShell

```powershell
# Clone/Navigate to project
cd "c:\Users\Ankitha Nagaraj\Downloads\DevTrack"

# Install Python dependencies
pip install -r requirements.txt

# Start Backend (Terminal 1)
cd backend; python app.py

# In another terminal, start Frontend (Terminal 2)
cd frontend; npm install; npm start
```

### Option 2: Manual Setup

#### Backend Setup
1. Open PowerShell as Administrator
2. Navigate to project: `cd c:\Users\Ankitha Nagaraj\Downloads\DevTrack`
3. Create virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
4. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
5. Run Flask server:
   ```powershell
   cd backend
   python app.py
   ```
   Backend runs on: `http://localhost:5000`

#### Frontend Setup
1. Open new PowerShell window
2. Navigate to frontend: `cd c:\Users\Ankitha Nagaraj\Downloads\DevTrack\frontend`
3. Install Node packages:
   ```powershell
   npm install
   ```
4. Start React development server:
   ```powershell
   npm start
   ```
   Frontend opens at: `http://localhost:3000`

## Prerequisites Check

### Required Software
- Python 3.8+ → [Download](https://www.python.org/downloads/)
- Node.js 14+ → [Download](https://nodejs.org/)
- Git (optional) → [Download](https://git-scm.com/)

### Verify Installation
```powershell
# Check Python
python --version

# Check Node.js
node --version
npm --version
```

## Troubleshooting

### Port Already in Use
If ports 5000 or 3000 are in use:

```powershell
# Find process using port 5000
Get-Process | Where-Object {$_.ProcessName -like "*python*"}

# Kill the process
Stop-Process -Name "python" -Force
```

### Permission Denied (Module Installation)
```powershell
# Run as Administrator or use:
pip install --user -r requirements.txt
```

### CORS Errors
- Ensure backend is running on http://localhost:5000
- Check `app.py` CORS configuration
- Clear browser cache: Ctrl+Shift+Delete

### Dependencies Not Installing
```powershell
# Upgrade pip
python -m pip install --upgrade pip

# Try installation again
pip install -r requirements.txt --no-cache-dir
```

## Configuration

### Create .env file
```powershell
# In project root directory
$content = @"
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=dev-secret-key-change-in-production
API_PORT=5000
"@

$content | Out-File -FilePath ".env" -Encoding UTF8
```

## API Testing

### Using PowerShell (Invoke-WebRequest)
```powershell
# Health check
Invoke-WebRequest -Uri "http://localhost:5000/api/health" -Method GET

# Run audit
$body = @{
    url = "https://example.com"
    depth = 2
    auto_fix = $false
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:5000/api/audit" `
  -Method POST `
  -Headers @{"Content-Type"="application/json"} `
  -Body $body
```

## Development Tools

### VS Code Extensions (Recommended)
- Python
- Pylance
- ES7+ React/Redux/React-Native
- Prettier - Code formatter
- REST Client

### Launch Configuration
Use built-in VS Code debugger:
1. Open `.vscode/launch.json`
2. Press F5 to start debugging

## Building for Production

### Backend
```powershell
# Set environment
$env:FLASK_ENV = "production"

# Use production server (gunicorn)
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Frontend
```powershell
cd frontend
npm run build

# This creates optimized build in 'build/' folder
```

## Project File Structure
```
DevTrack/
├── backend/
│   └── app.py
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
├── web_crawler/
│   ├── __init__.py
│   └── crawler.py
├── seo_analyzer/
│   ├── __init__.py
│   ├── analyzer.py
│   └── recommendations.py
├── requirements.txt
├── README.md
└── INSTALL.md (this file)
```

## Next Steps

1. **Test the Application**
   - Open http://localhost:3000 in browser
   - Navigate to "New Audit"
   - Enter a test URL (e.g., https://example.com)
   - Review audit results

2. **Explore Features**
   - Dashboard: Overview of features
   - Audit Results: Detailed analysis
   - History: Past audits

3. **Customize**
   - Modify scoring weights in `seo_analyzer/analyzer.py`
   - Add more checks in `web_crawler/crawler.py`
   - Enhance UI components in `frontend/src/components/`

## Support & Documentation

- **Backend Docs**: See `backend/app.py` for API details
- **Frontend Code**: Check component files for feature implementation
- **Main README**: `README.md` for overview

## Security Notes

⚠️ **For Development Only**:
- Use strong `SECRET_KEY` in production
- Enable HTTPS
- Add authentication
- Implement rate limiting
- Sanitize user inputs

---

**Last Updated**: 2024  
**Version**: 1.0.0
