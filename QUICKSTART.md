# 🎯 QUICK START GUIDE

Welcome to the **Autonomous On-Page & Technical SEO Auditor**! 

This guide will help you get started in 5 minutes.

## ⚡ 5-Minute Setup

### Step 1: Install Dependencies (2 minutes)
```powershell
cd "c:\Users\Ankitha Nagaraj\Downloads\DevTrack"
pip install -r requirements.txt
cd frontend
npm install
cd ..
```

### Step 2: Start Backend (1 minute)
```powershell
# Open Terminal 1 (recommended: run from project root)
# Option A - run from project root (recommended):
cd "c:\Users\Ankitha Nagaraj\Downloads\DevTrack"
python run_backend.py

# Option B - run from backend folder (older method):
cd backend
python app.py
```
✅ Backend running on `http://localhost:5000`

### Step 3: Start Frontend (1 minute)
```powershell
# Open Terminal 2
cd frontend
npm start
```
✅ Frontend opens at `http://localhost:3000`

### Step 4: Run Your First Audit (1 minute)
1. Open http://localhost:3000
2. Click "New Audit"
3. Enter: `https://example.com`
4. Click "Start Audit"
5. Watch the results come in!

## 📚 Documentation Files

| Document | Purpose | Read Time |
|----------|---------|-----------|
| **README.md** | Project overview & features | 10 min |
| **INSTALL.md** | Detailed installation guide | 15 min |
| **API.md** | API endpoints & usage | 10 min |
| **ARCHITECTURE.md** | System design & structure | 15 min |
| **TESTING.md** | Testing procedures | 10 min |

## 🚀 Running via Scripts

### Option 1: Start Backend
```powershell
.\start-backend.ps1
```

### Option 0: Start Backend (project-root runner)
```powershell
python run_backend.py
```

### Option 2: Start Frontend
```powershell
.\start-frontend.ps1
```

### Option 3: Both (Recommended)
```powershell
# Terminal 1
.\start-backend.ps1

# Terminal 2
.\start-frontend.ps1
```

## 🎨 Application Features

### Dashboard
- Overview of all features
- Latest audit results
- Getting started guide

### New Audit
- Enter website URL
- Select crawl depth (1-4)
- Optional auto-fix
- Comprehensive analysis

### Results
- SEO score (0-100)
- Issues by severity
- Recommendations with code
- Impact simulation
- Export to PDF

### History
- All past audits
- Quick access to results
- Performance tracking

## 📊 What Gets Analyzed

✅ **On-Page SEO**
- Title tags & length
- Meta descriptions
- Headers (H1, H2, etc.)
- Image alt text
- Content quality

✅ **Technical SEO**
- Mobile responsiveness
- Canonical tags
- Schema markup
- Broken links
- Page speed
- Robots directives

✅ **Recommendations**
- Priority ranking
- Code snippets
- Time estimates
- Difficulty levels
- Impact projections

## 🧪 Test With These URLs

```
https://example.com
https://github.com
https://google.com
https://wikipedia.org
```

## 🔧 Troubleshooting

### Port 5000 Already in Use
```powershell
# Kill the process
Stop-Process -Name "python" -Force
```

### Port 3000 Already in Use
```powershell
# Kill Node process
Stop-Process -Name "node" -Force
```

### Missing Dependencies
```powershell
# Reinstall
pip install -r requirements.txt --force-reinstall
cd frontend && npm install --no-cache
```

### CORS Errors
- Check both servers are running
- Clear browser cache (Ctrl+Shift+Delete)
- Verify URLs in console

## 📝 API Testing

### Quick Test (PowerShell)
```powershell
# Health check
Invoke-WebRequest -Uri "http://localhost:5000/api/health"

# Run audit
$body = @{
    url = "https://example.com"
    depth = 1
    auto_fix = $false
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:5000/api/audit" `
  -Method POST `
  -Headers @{"Content-Type"="application/json"} `
  -Body $body | ConvertTo-Json
```

## 📱 Browser Support

- ✅ Chrome/Chromium
- ✅ Firefox
- ✅ Edge
- ✅ Safari

## 💡 Pro Tips

1. **Start with small sites** (depth 1) to test
2. **Use your own domain** for detailed audit
3. **Export PDF** for presentations
4. **Check history** to track improvements
5. **Auto-fix disabled by default** for safety

## 🎯 Next Steps

1. Run your first audit
2. Review the recommendations
3. Check code snippets provided
4. Implement suggested changes
5. Run audit again to verify

## 📖 More Information

- **Features**: See README.md
- **Installation**: See INSTALL.md
- **API Details**: See API.md
- **Architecture**: See ARCHITECTURE.md
- **Testing**: See TESTING.md

## ⚙️ Configuration

The application uses default settings but can be customized:

- **Crawl timeout**: `web_crawler/crawler.py` line 13
- **Scoring weights**: `seo_analyzer/analyzer.py` line 10
- **API port**: `backend/app.py` last line
- **React port**: `frontend/package.json` proxy setting

## 🆘 Getting Help

### Common Issues

| Issue | Solution |
|-------|----------|
| Port in use | `Stop-Process -Name python -Force` |
| ModuleNotFound | `pip install -r requirements.txt` |
| npm errors | `cd frontend && npm install` |
| CORS errors | Check backend is running |
| Slow crawl | Reduce depth or increase timeout |

### Debug Mode

**Backend**:
```powershell
# Already enabled in development
# Check terminal output for errors
```

**Frontend**:
```powershell
# Press F12 in browser
# Check Console tab for errors
# Check Network tab for API calls
```

## 🎓 Learning

Want to customize the application?

1. **Add new checks**: Edit `seo_analyzer/analyzer.py`
2. **Improve crawler**: Edit `web_crawler/crawler.py`
3. **Change UI**: Edit `frontend/src/components/`
4. **Add database**: Modify `backend/app.py`

## 📞 Support

If you encounter issues:

1. Check TROUBLESHOOTING section above
2. Review relevant documentation file
3. Check terminal/console for error messages
4. Verify all dependencies installed

## ✨ Features Coming Soon

- 📊 Historical trend analysis
- 🔔 Automated alerts
- 📈 Keyword ranking integration
- 🤖 ML-based recommendations
- 🔐 User authentication
- 💾 Database persistence
- 📱 Mobile app

---

## 🎉 You're Ready!

Your SEO Auditor is now set up and ready to use!

**Start the application and audit your first website now!**

```
Backend:  .\start-backend.ps1
Frontend: .\start-frontend.ps1
```

Happy auditing! 🚀

---

**Version**: 1.0.0  
**Last Updated**: 2024  
**Support**: Check documentation files above
