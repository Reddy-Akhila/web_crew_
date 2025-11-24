# Testing Guide for SEO Auditor

## Testing Checklist

### 1. Backend API Tests

#### Health Check
```powershell
# Test 1: API Health Check
Invoke-WebRequest -Uri "http://localhost:5000/api/health" | ConvertTo-Json
```
Expected: `{ "status": "healthy", "timestamp": "..." }`

#### Quick Single Page Check
```powershell
# Test 2: Quick Page Check
$body = @{
    url = "https://example.com"
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:5000/api/quick-check" `
  -Method POST `
  -Headers @{"Content-Type"="application/json"} `
  -Body $body | ConvertTo-Json
```

#### Full Audit
```powershell
# Test 3: Run Full Audit
$body = @{
    url = "https://example.com"
    depth = 1
    auto_fix = $false
} | ConvertTo-Json

$response = Invoke-WebRequest -Uri "http://localhost:5000/api/audit" `
  -Method POST `
  -Headers @{"Content-Type"="application/json"} `
  -Body $body

$audit = $response.Content | ConvertFrom-Json
Write-Host "SEO Score: $($audit.seo_score)"
Write-Host "Pages Audited: $($audit.crawl_summary.total_pages)"
Write-Host "Issues Found: $($audit.issues.Count)"
```

#### Get Audit History
```powershell
# Test 4: Get History
Invoke-WebRequest -Uri "http://localhost:5000/api/audit-history" | ConvertTo-Json
```

### 2. Frontend Tests

#### Dashboard
- [ ] Page loads without errors
- [ ] Feature cards display correctly
- [ ] Getting Started section shows all 4 steps
- [ ] Navigation buttons work

#### New Audit
- [ ] Form loads with all fields
- [ ] URL validation works
- [ ] Depth selector has 4 options
- [ ] Checkbox for auto-fix visible
- [ ] Submit button triggers audit

#### Audit Results
- [ ] Score cards display correctly
- [ ] Issues section filters work (All/Critical/High)
- [ ] Recommendations cards show all data
- [ ] Impact chart displays metrics
- [ ] Export PDF button visible

#### Audit History
- [ ] Table displays all audits
- [ ] Pagination works (if implemented)
- [ ] Sorting works
- [ ] Data is formatted correctly

### 3. Integration Tests

#### Complete Audit Flow
1. Start backend server
2. Start frontend server
3. Open http://localhost:3000
4. Click "New Audit"
5. Enter test URL: `https://example.com`
6. Set depth to 1
7. Click "Start Audit"
8. Wait for results
9. Verify all sections appear
10. Click through tabs
11. Export PDF
12. Check Audit History

#### Error Handling
- [ ] Enter invalid URL → error message appears
- [ ] Enter non-existent site → graceful error
- [ ] Interrupt audit → handles gracefully
- [ ] Disconnect backend → shows error message

### 4. Performance Tests

#### Load Testing
```powershell
# Test with multiple concurrent audits
for ($i = 1; $i -le 3; $i++) {
    $body = @{
        url = "https://example.com"
        depth = 1
    } | ConvertTo-Json
    
    Invoke-WebRequest -Uri "http://localhost:5000/api/audit" `
      -Method POST `
      -Headers @{"Content-Type"="application/json"} `
      -Body $body -TimeoutSec 120
}
```

#### Browser Performance
- [ ] Check DevTools → Performance tab
- [ ] Measure Time to Interactive (TTI)
- [ ] Check for console errors/warnings
- [ ] Monitor memory usage

### 5. Data Validation Tests

#### Test URLs
- [ ] `https://example.com` - Standard site
- [ ] `https://github.com` - Large site
- [ ] `https://google.com` - Simple site
- [ ] `https://shopify.com` - E-commerce

#### Invalid Inputs
- [ ] Missing `http://` - should auto-add
- [ ] Non-existent domain - should return error
- [ ] IP addresses - should work or error gracefully
- [ ] Special characters - should validate

### 6. Browser Compatibility

- [ ] Chrome/Chromium
- [ ] Firefox
- [ ] Edge
- [ ] Safari (if available)

### 7. Responsive Design

- [ ] Desktop (1920x1080)
- [ ] Tablet (768x1024)
- [ ] Mobile (375x667)
- [ ] All elements visible
- [ ] Text readable
- [ ] Touch targets adequate

## Test Results Template

```
Test Date: ___________
Tester: _______________
Environment: Development/Production
Browser: _______________
OS: _______________

PASSED: [ ] FAILED: [ ] PARTIAL: [ ]

Issues Found:
1. ________________________
2. ________________________
3. ________________________

Notes:
_________________________
_________________________
```

## Automated Test Script

```python
# tests/test_api.py
import requests
import json

BASE_URL = "http://localhost:5000"

def test_health():
    response = requests.get(f"{BASE_URL}/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    print("✓ Health check passed")

def test_audit():
    payload = {
        "url": "https://example.com",
        "depth": 1,
        "auto_fix": False
    }
    response = requests.post(f"{BASE_URL}/api/audit", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "seo_score" in data
    assert "issues" in data
    print(f"✓ Audit test passed - Score: {data['seo_score']}")

def test_invalid_url():
    payload = {"url": "not-a-valid-url"}
    response = requests.post(f"{BASE_URL}/api/audit", json=payload)
    assert response.status_code in [400, 500]
    print("✓ Invalid URL handling passed")

if __name__ == "__main__":
    print("Running SEO Auditor Tests...")
    test_health()
    test_audit()
    test_invalid_url()
    print("\n✓ All tests passed!")
```

Run with: `python tests/test_api.py`

## Known Issues & Workarounds

1. **CORS Errors on Frontend**
   - Ensure backend is running on localhost:5000
   - Clear browser cache
   - Check CORS settings in app.py

2. **Port Already in Use**
   - Kill process: `Stop-Process -Name python -Force`
   - Use different port: `python app.py --port=5001`

3. **Module Not Found Errors**
   - Reinstall requirements: `pip install --force-reinstall -r requirements.txt`
   - Check Python path: `python -m pip list`

4. **Network Timeout During Crawl**
   - Increase timeout in crawler.py: `timeout=30`
   - Use smaller depth setting

## Useful Debug Commands

```powershell
# Check all dependencies
pip list

# Check Node modules
npm list

# Monitor network requests
# Open DevTools (F12) → Network tab

# Check server logs
# Check terminal output where server is running

# Test API directly
$response = Invoke-WebRequest -Uri "http://localhost:5000/api/health"
$response.Content | ConvertFrom-Json

# Performance monitoring
# Open DevTools → Performance → Record
```

---

**Last Updated**: 2024  
**Test Coverage**: API, Frontend, Integration, Performance
