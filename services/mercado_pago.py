import uuid
import requests
from decouple import config

class MercadoPago():
    
    BASE_URL = config('MP_BASE_API_URL')
    
    def __init__(self):
        self.__access_token = config('MP_ACCESS_TOKEN')
        self.__headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.__access_token}',
        }
    
    def __post(self, path: str, payload: dict) -> dict:
        url = f'{self.BASE_URL}{path}'
        headers = {**self.__headers, 'X-Idempotency-Key': str(uuid.uuid4())}
        response = requests.post(
            url=url,
            json=payload,
            headers=headers,
        )
        try:
            response.raise_for_status()
        except requests.HTTPError:
            try:
                error = response.json()
            except:
                error = response.text
            raise RuntimeError(f'Erro MP {response.status_code}: {error}')
        return response.json()