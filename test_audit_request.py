#!/usr/bin/env python3
"""
Simple script to test the /api/audit endpoint
"""
import requests
import json
import time

# Test a simple URL
test_url = "https://www.example.com"
depth = 1

print(f"Testing /api/audit with URL: {test_url}, depth: {depth}")
print("=" * 60)

try:
    response = requests.post(
        "http://127.0.0.1:5000/api/audit",
        json={
            "url": test_url,
            "depth": depth,
            "auto_fix": False
        },
        timeout=30
    )
    
    print(f"Status: {response.status_code}")
    print("\nResponse:")
    data = response.json()
    print(json.dumps(data, indent=2))
    
    # Show key metrics
    if 'crawl_summary' in data:
        print("\n" + "=" * 60)
        print(f"Total Pages: {data['crawl_summary']['total_pages']}")
        print(f"SEO Score: {data['seo_score']}")
        print(f"Issues Found: {len(data.get('issues', []))}")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
