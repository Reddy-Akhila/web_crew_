#!/usr/bin/env python3
"""
Backend lifecycle manager - ensures clean backend state
"""
import subprocess
import time
import sys
import os

# Kill any existing Python processes
print("Cleaning up any existing Python processes...")
os.system("Stop-Process -Name python -Force -ErrorAction SilentlyContinue")
time.sleep(2)

# Start fresh backend
print("\nStarting fresh backend...")
subprocess.Popen([
    os.path.join(".venv", "Scripts", "python.exe"),
    "run_backend.py"
], cwd="C:\\Users\\Ankitha Nagaraj\\Downloads\\DevTrack")

# Wait for backend to start
print("Waiting 5 seconds for backend to initialize...")
time.sleep(5)

# Test the health endpoint
print("\nTesting backend health endpoint...")
import requests
try:
    response = requests.get("http://127.0.0.1:5000/api/health", timeout=5)
    if response.status_code == 200:
        print("✓ Backend is healthy and ready!")
        print(f"  Response: {response.json()}")
    else:
        print(f"✗ Backend returned status {response.status_code}")
except Exception as e:
    print(f"✗ Failed to connect to backend: {e}")
    sys.exit(1)
