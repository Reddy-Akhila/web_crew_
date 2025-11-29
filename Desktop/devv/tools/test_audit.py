import requests, json
url = 'http://127.0.0.1:5000/api/audit'
payload = {'url':'https://www.geeksforgeeks.org/','depth':1,'auto_fix':False}
try:
    r = requests.post(url, json=payload, timeout=60)
    print('Status:', r.status_code)
    try:
        print(json.dumps(r.json(), indent=2)[:2000])
    except Exception:
        print('Response text:', r.text[:2000])
except Exception as e:
    print('Request failed:', repr(e))
