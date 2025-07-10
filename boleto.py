import uuid
import requests
from decouple import config

MP_ACCESS_TOKEN = config('MP_ACCESS_TOKEN')
BASE_URL = 'https://api.mercadopago.com/v1/payments'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {MP_ACCESS_TOKEN}',
    'X-Idempotency-Key': str(uuid.uuid4()),
}

payload = {
    'transaction_amount': 100,
    'description': 'Pagamento de teste com boleto',
    'payment_method_id': 'bolbradesco',
    'payer': {
        'first_name': 'Test',
		'last_name': 'Test',
        'email': 'test_user_123@testuser.com',
        'identification': {
            'type': 'CPF',
            'number': '95749019047'
        },
        'address': {
			'zip_code': '06233-200',
            'street_name': 'Av das Nacoes Unidas',
            'street_number': 3003,
            'city': 'Rio de Janeiro',
            'neighborhood': 'Copacabana',
            'federal_unit': 'RJ'
		},
    }
}

response = requests.post(BASE_URL, json=payload, headers=headers)

print('Status code:', response.status_code)
print('Response:', response.text)
