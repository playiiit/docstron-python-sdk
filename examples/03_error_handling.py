"""
Example: Error Handling
"""

from docstron import Docstron
from docstron.exceptions import (
    AuthenticationError,
    NotFoundError,
    ValidationError,
    RateLimitError,
    DocstronError
)

# Initialize client
client = Docstron(api_key='your-api-key-here')

# Example 1: Handle authentication errors
try:
    invalid_client = Docstron(api_key='invalid-key')
    apps = invalid_client.applications.list()
except AuthenticationError as e:
    print(f'❌ Authentication failed: {e.message}')
    print(f'   Status code: {e.status_code}')

# Example 2: Handle not found errors
try:
    template = client.templates.get('non-existent-template-id')
except NotFoundError as e:
    print(f'❌ Resource not found: {e.message}')

# Example 3: Handle validation errors
try:
    # Missing required field
    template = client.templates.create(
        application_id='app-123',
        name='',  # Empty name will cause validation error
        content='<h1>Test</h1>'
    )
except ValidationError as e:
    print(f'❌ Validation error: {e.message}')
    print(f'   Response: {e.response}')

# Example 4: Handle rate limit errors
try:
    # If you exceed your rate limit
    for i in range(1000):
        client.documents.quick_generate(
            html='<h1>Test</h1>',
            response_type='pdf'
        )
except RateLimitError as e:
    print(f'❌ Rate limit exceeded: {e.message}')
    print('   Please wait before making more requests')

# Example 5: Catch all errors
try:
    doc = client.documents.generate(
        template_id='template-123',
        data={'test': 'data'}
    )
except DocstronError as e:
    print(f'❌ An error occurred: {e.message}')
    print(f'   Status code: {e.status_code}')
    print(f'   Full response: {e.response}')

# Example 6: Successful error recovery
def generate_pdf_with_retry(client, template_id, data, max_retries=3):
    """Generate PDF with retry logic"""
    for attempt in range(max_retries):
        try:
            pdf = client.documents.generate(
                template_id=template_id,
                data=data,
                response_type='pdf'
            )
            return pdf
        except RateLimitError:
            if attempt < max_retries - 1:
                import time
                wait_time = (attempt + 1) * 2  # Exponential backoff
                print(f'Rate limited. Waiting {wait_time} seconds...')
                time.sleep(wait_time)
            else:
                raise
        except NotFoundError as e:
            print(f'Template not found: {e.message}')
            raise
        except DocstronError as e:
            print(f'Error on attempt {attempt + 1}: {e.message}')
            if attempt == max_retries - 1:
                raise

# Usage
try:
    pdf = generate_pdf_with_retry(
        client,
        'template-123',
        {'name': 'Test'}
    )
    print('✅ PDF generated successfully with retry logic')
except DocstronError as e:
    print(f'❌ Failed after all retries: {e.message}')
