#!/usr/bin/env python3
"""
Check the audit history to see what's stored
"""
import requests
import json

print("Getting audit history...")
print("=" * 60)

try:
    response = requests.get(
        "http://127.0.0.1:5000/api/audit-history",
        timeout=10
    )
    
    print(f"Status: {response.status_code}")
    data = response.json()
    
    print(f"\nTotal audits in history: {len(data)}")
    print("\n" + "=" * 60)
    
    for i, audit in enumerate(data, 1):
        print(f"\nAudit {i}:")
        print(f"  URL: {audit['url']}")
        print(f"  Pages Audited: {audit['pages_audited']}")
        print(f"  Issues Count: {audit['issues_count']}")
        print(f"  SEO Score: {audit['seo_score']}")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
