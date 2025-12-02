"""
Example: Quick Start with Debug - Generate a simple PDF
"""

from docstron import Docstron
from docstron.exceptions import DocstronError

# Initialize client with your API key
client = Docstron(api_key='your-api-key-here')

try:
    # Quick generate a PDF without creating a template
    pdf_data = client.documents.quick_generate(
        html='<h1>Hello {{name}}!</h1><p>This is a PDF generated from the Docstron Python SDK.</p>',
        data={'name': 'World'},
        response_type='pdf'
    )

    # Save the PDF to a file
    with open('hello.pdf', 'wb') as f:
        f.write(pdf_data)

    print('✅ PDF generated successfully: hello.pdf')
    
except DocstronError as e:
    print(f'❌ Error: {e.message}')
    print(f'Status code: {e.status_code}')
    print(f'Full response: {e.response}')
