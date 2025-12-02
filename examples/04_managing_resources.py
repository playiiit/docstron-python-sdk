"""
Example: Managing Resources (Applications, Templates, Documents)
"""

from docstron import Docstron

# Initialize client
client = Docstron(api_key='your-api-key-here')

print('=' * 60)
print('APPLICATIONS')
print('=' * 60)

# List all applications
apps = client.applications.list()
print(f'\nFound {len(apps["data"])} applications:')
for app in apps['data']:
    print(f'  - {app["name"]} ({app["app_id"]})')
    print(f'    Active: {app["is_active"]}')
    print(f'    Created: {app["created_at"]}')

# Get specific application
if apps['data']:
    app_id = apps['data'][0]['app_id']
    app = client.applications.get(app_id)
    print(f'\nApplication details for {app_id}:')
    print(f'  Name: {app["data"]["name"]}')
    print(f'  Description: {app["data"]["description"]}')

print('\n' + '=' * 60)
print('TEMPLATES')
print('=' * 60)

# Create a new template
print('\nCreating new template...')
new_template = client.templates.create(
    application_id=app_id,  # Use the app_id from above
    name='Test Report Template',
    content='''
        <html>
        <body>
            <h1>{{report_title}}</h1>
            <p>Generated on: {{date}}</p>
            <p>{{content}}</p>
        </body>
        </html>
    ''',
    is_active=True
)
template_id = new_template['data']['template_id']
print(f'✅ Created template: {template_id}')

# List all templates
templates = client.templates.list()
print(f'\nFound {len(templates["data"])} templates:')
for tmpl in templates['data']:
    print(f'  - {tmpl["name"]} ({tmpl["template_id"]})')
    print(f'    Active: {tmpl["is_active"]}')

# Update template
print(f'\nUpdating template {template_id}...')
updated_template = client.templates.update(
    template_id=template_id,
    name='Updated Test Report Template',
    is_active=True
)
print(f'✅ Template updated: {updated_template["data"]["name"]}')

# Get specific template
template = client.templates.get(template_id)
print(f'\nTemplate details:')
print(f'  Name: {template["data"]["name"]}')
print(f'  Created: {template["data"]["created_at"]}')
print(f'  Updated: {template["data"]["updated_at"]}')

print('\n' + '=' * 60)
print('DOCUMENTS')
print('=' * 60)

# Generate a document
print('\nGenerating document...')
doc = client.documents.generate(
    template_id=template_id,
    data={
        'report_title': 'Monthly Sales Report',
        'date': '2024-12-02',
        'content': 'This report shows excellent growth in Q4.'
    },
    response_type='document_id'
)
document_id = doc['data']['document_id']
print(f'✅ Document generated: {document_id}')

# List all documents
documents = client.documents.list()
print(f'\nFound {len(documents["data"])} documents:')
for doc in documents['data'][:5]:  # Show first 5
    print(f'  - {doc["document_id"]}')
    print(f'    Template: {doc["template_id"]}')
    print(f'    Created: {doc["created_at"]}')

# Get specific document
document = client.documents.get(document_id)
print(f'\nDocument details:')
print(f'  ID: {document["data"]["document_id"]}')
print(f'  Attributes: {document["data"]["attributes"]}')

# Update document
print(f'\nUpdating document {document_id}...')
updated_doc = client.documents.update(
    document_id=document_id,
    data={
        'report_title': 'Updated Monthly Sales Report',
        'date': '2024-12-02',
        'content': 'This report shows exceptional growth in Q4!'
    }
)
print(f'✅ Document updated')

# Download document as PDF
print(f'\nDownloading document as PDF...')
client.documents.download(
    document_id=document_id,
    output_path='report.pdf'
)
print(f'✅ PDF downloaded: report.pdf')

print('\n' + '=' * 60)
print('USAGE STATISTICS')
print('=' * 60)

# Check usage
usage = client.usage.get()
usage_data = usage['data']

print(f'\nSubscription Plan: {usage_data["subscription"]["plan_name"]}')
print(f'API Rate Limit: {usage_data["subscription"]["api_rate_limit"]} req/sec')
print(f'Support Level: {usage_data["subscription"]["support_level"]}')

print('\nApplications:')
print(f'  Total: {usage_data["applications"]["total"]} / {usage_data["applications"]["limit"]}')
print(f'  Usage: {usage_data["applications"]["usage_percentage"]}%')

print('\nTemplates:')
print(f'  Total: {usage_data["templates"]["total"]} / {usage_data["templates"]["limit"]}')
print(f'  Usage: {usage_data["templates"]["usage_percentage"]}%')

print('\nDocuments:')
print(f'  Total: {usage_data["documents"]["total"]}')
print(f'  This month: {usage_data["documents"]["monthly"]} / {usage_data["documents"]["monthly_limit"]}')
print(f'  Usage: {usage_data["documents"]["usage_percentage"]}%')

print('\n' + '=' * 60)
print('CLEANUP')
print('=' * 60)

# Delete document
print(f'\nDeleting document {document_id}...')
client.documents.delete(document_id)
print('✅ Document deleted')

# Delete template
print(f'\nDeleting template {template_id}...')
client.templates.delete(template_id)
print('✅ Template deleted')

print('\n✅ Example completed successfully!')
