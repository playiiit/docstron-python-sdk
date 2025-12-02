"""
Test API Connection - Verify API key and connection
"""

from docstron import Docstron
from docstron.exceptions import DocstronError, AuthenticationError

# Test with your API key
api_key = 'dstr_WJokpkvGLJ3UNBmrDqvjc8HaN-1q1ssoQev-SAJa-gwKzVNzYleP'

print(f'Testing connection with API key: {api_key[:20]}...')
print(f'API Base URL: https://api.docstron.com/v1')
print()

client = Docstron(api_key=api_key)

# Test 1: Check usage (simplest GET request)
print('Test 1: Checking usage statistics...')
try:
    usage = client.usage.get()
    print('✅ Success! API connection working.')
    print(f'Plan: {usage["data"]["subscription"]["plan_name"]}')
    print(f'Documents this month: {usage["data"]["documents"]["monthly"]}')
    print()
except AuthenticationError as e:
    print(f'❌ Authentication failed: {e.message}')
    print(f'Response: {e.response}')
    print()
except DocstronError as e:
    print(f'❌ Error: {e.message}')
    print(f'Status code: {e.status_code}')
    print(f'Response: {e.response}')
    print()

# Test 2: List applications
print('Test 2: Listing applications...')
try:
    apps = client.applications.list()
    print(f'✅ Found {len(apps.get("data", []))} applications')
    for app in apps.get('data', [])[:3]:
        print(f'  - {app["name"]} ({app["app_id"]})')
    print()
except DocstronError as e:
    print(f'❌ Error: {e.message}')
    print(f'Status code: {e.status_code}')
    print()

# Test 3: Try quick generate with document_id response
print('Test 3: Quick generate (document_id response)...')
try:
    doc = client.documents.quick_generate(
        html='<h1>Test</h1>',
        response_type='document_id'
    )
    print(f'✅ Document generated: {doc.get("data", {}).get("document_id")}')
    print()
except DocstronError as e:
    print(f'❌ Error: {e.message}')
    print(f'Status code: {e.status_code}')
    print(f'Response: {e.response}')
    print()

print('=' * 60)
print('Connection test complete!')
