import uuid
import requests
from decouple import config

MP_ACCESS_TOKEN = config('MP_ACCESS_TOKEN')
BASE_URL = "https://api.mercadopago.com/v1/payments"

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {MP_ACCESS_TOKEN}',
    'X-Idempotency-Key': str(uuid.uuid4()),
}

payload = {
    'transaction_amount': 100,
    'description': 'Pagamento de teste com Pix',
    'payment_method_id': 'pix',
    'payer': {
        'email': 'test_user_123@testuser.com',
        'identification': {
            'type': 'CPF',
            'number': '95749019047'
        }
    }
}

response = requests.post(BASE_URL, json=payload, headers=headers)

print("Status code:", response.status_code)
print("Response:", response.text)
