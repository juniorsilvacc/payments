import uuid
import requests
from decouple import config

MP_ACCESS_TOKEN = config('MP_ACCESS_TOKEN')
BASE_URL = 'https://api.mercadopago.com'

headers_token = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {MP_ACCESS_TOKEN}',
}

card_data = {
    'card_number': '5031433215406351',
    'expiration_month': '11',
    'expiration_year': '2030',
    'security_code': '123',
    'cardholder': {
        'name': 'Teste user',
        'identification': {
            'type': 'CPF',
            'number': '12345678909'
        }
    }
}

token_response = requests.post(
    url=f'{BASE_URL}/v1/card_tokens',
    json=card_data,
    headers=headers_token
).json()

card_token = token_response.get('id')
print(card_token)

# headers = {
#     'Content-Type': 'application/json',
#     'Authorization': f'Bearer {MP_ACCESS_TOKEN}',
#     'X-Idempotency-Key': str(uuid.uuid4()),
# }

# payload = {
#     'transaction_amount': 100,
#     'description': 'Pagamento de teste com boleto',
#     'payment_method_id': 'bolbradesco',
#     'payer': {
#         'first_name': 'Test first name',
# 		'last_name': 'Test last name',
#         'email': 'test_user_123@testuser.com',
#         'identification': {
#             'type': 'CPF',
#             'number': '95749019047'
#         },
#         'address': {
# 			'zip_code': '06233-200',
#             'street_name': 'Av das Nacoes Unidas',
#             'street_number': 3003,
#             'city': 'Rio de Janeiro',
#             'neighborhood': 'Copacabana',
#             'federal_unit': 'RJ'
# 		},
#     }
# }

# response = requests.post(BASE_URL, json=payload, headers=headers)

# print('Status code:', response.status_code)
# print('Response:', response.text)
