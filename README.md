# 🧾 Checkout de Pagamentos com FastAPI e Mercado Pago

Este projeto é uma aplicação de checkout simples e funcional desenvolvida com **FastAPI**, **Tailwind CSS** e integração com a API do **Mercado Pago**.

## 🚀 Funcionalidades
- 💳 Pagamento com **Cartão de Crédito**
- 💸 Pagamento via **PIX** (com redirecionamento para QR Code)
- 🧾 Pagamento via **Boleto Bancário**
- 🧍‍♂️ Coleta de dados pessoais e endereço para boletos
- 🎯 Interface responsiva e leve com Tailwind CSS
- 🔒 Overlay de carregamento e feedback de status do pagamento

## ⚙️ Tecnologias
- [FastAPI](https://fastapi.tiangolo.com/) — Backend Python moderno
- [Tailwind CSS](https://tailwindcss.com/) — Estilização frontend
- [Mercado Pago](https://www.mercadopago.com.br/developers/pt/guides) — API de pagamento
- [Jinja2](https://jinja.palletsprojects.com/) — Template engine

## 📸 Screenshot
<img width="1208" height="1058" alt="Image" src="https://github.com/user-attachments/assets/f336e263-c2ef-4cd7-9ca8-a06dd17060a9" />

## 📂 Estrutura
```bash
.
├── app.py                # Servidor FastAPI e rotas
├── services/
│   └── mercado_pago.py   # Client com integração da API do Mercado Pago
├── templates/
│   └── checkout.html     # Template do checkout
├── requirements.txt      # Dependências
├── .env                  # Configurações secretas (tokens)
└── README.md             
```

## 📝 Requisitos
- Python 3.9+
- Conta de desenvolvedor no Mercado Pago
- Chaves de acesso (Access Token, Public Key)

## 🧪 Como usar
```bash
Clone o repositório:
git clone https://github.com/juniorsilvacc/payments.git
cd payments
```

```bash
Crie um ambiente virtual e instale as dependências:
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
```

```bash
Crie um arquivo .env com suas credenciais:
MP_BASE_API_URL=https://api.mercadopago.com
MP_ACCESS_TOKEN=seu_token_aqui
```

```bash
Inicie o servidor:
uvicorn main:app --reload
```

Acessar a aplicação http://localhost:8000
