"""
Example: Generate Invoice PDF from Template
"""

from docstron import Docstron

# Initialize client
client = Docstron(api_key='your-api-key-here')

# Step 1: Create a template
print('Creating invoice template...')
template = client.templates.create(
    application_id='your-app-id-here',
    name='Invoice Template',
    content='''
        <html>
        <head>
            <style>
                body { 
                    font-family: Arial, sans-serif; 
                    max-width: 800px; 
                    margin: 0 auto;
                    padding: 20px;
                }
                .header { 
                    background: #1ee494; 
                    color: white; 
                    padding: 20px; 
                    border-radius: 5px;
                }
                .info { margin: 20px 0; }
                table { 
                    width: 100%; 
                    border-collapse: collapse; 
                    margin: 20px 0;
                }
                th, td { 
                    padding: 12px; 
                    text-align: left; 
                    border-bottom: 1px solid #ddd; 
                }
                th { background-color: #f2f2f2; }
                .total { 
                    text-align: right; 
                    font-size: 1.2em; 
                    font-weight: bold; 
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <div class="header">
                <h1>INVOICE</h1>
                <p>Invoice #{{invoice_number}}</p>
            </div>
            
            <div class="info">
                <p><strong>Date:</strong> {{invoice_date}}</p>
                <p><strong>Customer:</strong> {{customer_name}}</p>
                <p><strong>Email:</strong> {{customer_email}}</p>
            </div>
            
            <table>
                <thead>
                    <tr>
                        <th>Description</th>
                        <th>Quantity</th>
                        <th>Price</th>
                        <th>Total</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>{{item_description}}</td>
                        <td>{{item_quantity}}</td>
                        <td>{{item_price}}</td>
                        <td>{{item_total}}</td>
                    </tr>
                </tbody>
            </table>
            
            <div class="total">
                Total Amount: {{total_amount}}
            </div>
            
            <p style="margin-top: 40px; color: #666; font-size: 0.9em;">
                Thank you for your business!
            </p>
        </body>
        </html>
    ''',
    extra_css='''
        @page {
            margin: 2cm;
            @bottom-center {
                content: "Page " counter(page) " of " counter(pages);
                color: #666;
                font-size: 10pt;
            }
        }
    '''
)

template_id = template['data']['template_id']
print(f'✅ Template created: {template_id}')

# Step 2: Generate PDF from template
print('Generating invoice PDF...')
pdf_data = client.documents.generate(
    template_id=template_id,
    data={
        'invoice_number': 'INV-2024-001',
        'invoice_date': '2024-12-02',
        'customer_name': 'John Doe',
        'customer_email': 'john@example.com',
        'item_description': 'Professional Web Development Services',
        'item_quantity': '1',
        'item_price': '$2,500.00',
        'item_total': '$2,500.00',
        'total_amount': '$2,500.00'
    },
    response_type='pdf'
)

# Step 3: Save the PDF
with open('invoice.pdf', 'wb') as f:
    f.write(pdf_data)

print('✅ Invoice PDF generated: invoice.pdf')
