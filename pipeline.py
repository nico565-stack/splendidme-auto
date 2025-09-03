
import os, requests, pandas as pd
from jinja2 import Template

SHOPIFY_DOMAIN = os.getenv("SHOPIFY_STORE_DOMAIN")
SHOPIFY_API_KEY = os.getenv("SHOPIFY_API_KEY")
SHOPIFY_PASSWORD = os.getenv("SHOPIFY_API_PASSWORD")
AMAZON_TAG = os.getenv("AMAZON_TAG")

def discover_trends():
    # Placeholder: usa le prime keyword dei prodotti
    df = pd.read_csv('products.csv')
    return df['keyword'].unique()[:3]

def generate_article(keyword):
    df = pd.read_csv('products.csv')
    products = df[df['keyword']==keyword].to_dict('records')
    with open('template_article.html') as f:
        template = Template(f.read())
    titleA = f"Migliori {keyword} 2025: top scelte"
    titleB = f"{keyword.capitalize()} efficaci: guida aggiornata"
    html = template.render(title=titleA, keyword=keyword, products=products)
    return {"titles":[titleA,titleB],"html":html}

def publish_to_shopify(title, html):
    url = f"https://{SHOPIFY_API_KEY}:{SHOPIFY_PASSWORD}@{SHOPIFY_DOMAIN}/admin/api/2024-07/blogs/1234567890/articles.json"
    data = {"article":{"title":title,"body_html":html}}
    r = requests.post(url,json=data)
    print("Shopify:",r.status_code, r.text)

def main():
    kws = discover_trends()
    for kw in kws:
        art = generate_article(kw)
        publish_to_shopify(art["titles"][0], art["html"])

if __name__ == "__main__":
    main()
