# Start Backend Server
# Run this in PowerShell from the DevTrack directory

cd backend

# Check if virtual environment exists
if (-Not (Test-Path "venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& "venv\Scripts\Activate.ps1"

# Install requirements if not already installed
Write-Host "Installing dependencies..." -ForegroundColor Yellow
pip install -q -r ../requirements.txt

# Start Flask server
Write-Host "Starting Flask server on http://localhost:5000" -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
python app.py
