import sys
sys.path.append('/opt/package')
import json
import qrcode
from io import BytesIO
import base64

def lambda_handler(event, context):
    print("Event received:", json.dumps(event))
    
    cors_headers = {
        'Access-Control-Allow-Origin': '*', 
        'Access-Control-Allow-Methods': 'GET, OPTIONS', 
        'Access-Control-Allow-Headers': 'Content-Type, X-Amz-Date, Authorization, X-Api-Key, X-Amz-Security-Token', 
        'Content-Type': 'application/json', 
    }

    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'body': '',
            'headers': cors_headers 
        }

    if not event.get('queryStringParameters'):
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing queryStringParameters in the request.'}),
            'headers': cors_headers 
        }

    url = event['queryStringParameters'].get('url')
    if not url:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'URL parameter is missing in the request.'}),
            'headers': cors_headers 
        }

    try:
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

        return {
            'statusCode': 200,
            'body': json.dumps({'qr_code': img_base64}),
            'headers': cors_headers
        }

    except Exception as e:
        print("Error during QR code generation:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Failed to generate QR Code.'}),
            'headers': cors_headers
        }
