# Start Frontend Development Server
# Run this in PowerShell from the DevTrack\frontend directory

cd frontend

Write-Host "Installing Node dependencies..." -ForegroundColor Yellow
npm install --quiet

Write-Host "Starting React development server on http://localhost:3000" -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host "The browser will open automatically" -ForegroundColor Cyan
npm start
