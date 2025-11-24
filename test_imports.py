#!/usr/bin/env python
"""
Test script: verify all required packages are installed in the active Python environment.
Run this to confirm the .venv has all dependencies.
"""

import sys

required_packages = [
    'flask',
    'flask_cors',
    'requests',
    'beautifulsoup4',
    'lxml',
    'validators',
    'dotenv',
]

print(f"Testing with Python: {sys.executable}\n")
print(f"Python version: {sys.version}\n")

missing = []
installed = []

for pkg in required_packages:
    try:
        __import__(pkg.replace('-', '_').replace('flask_cors', 'flask_cors'))
        installed.append(pkg)
        print(f"✅ {pkg}")
    except ImportError:
        missing.append(pkg)
        print(f"❌ {pkg}")

print(f"\n✅ Installed: {len(installed)}/{len(required_packages)}")
if missing:
    print(f"❌ Missing: {', '.join(missing)}")
    print("\nRun: pip install -r requirements.txt")
    sys.exit(1)
else:
    print("✅ All packages installed!")
    sys.exit(0)
