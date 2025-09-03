
import requests
import os

# Prende i dati dai secrets GitHub
SHOPIFY_STORE_DOMAIN = os.getenv("SHOPIFY_STORE_DOMAIN")
API_KEY = os.getenv("SHOPIFY_API_KEY")
PASSWORD = os.getenv("SHOPIFY_API_PASSWORD")

# Endpoint Shopify API
url = f"https://{API_KEY}:{PASSWORD}@{SHOPIFY_STORE_DOMAIN}/admin/api/2023-10/products.json"

# Nuovo prodotto da creare
data = {
    "product": {
        "title": "Prodotto Test SplendidMe",
        "body_html": "<strong>Creato automaticamente dal bot 🚀</strong>",
        "vendor": "SplendidMe",
        "product_type": "Automazione",
        "variants": [
            {"price": "19.99"}
        ]
    }
}

res = requests.post(url, json=data)

print("Status:", res.status_code)
print("Risposta:", res.json())
