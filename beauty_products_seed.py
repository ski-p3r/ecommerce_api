import os
import django

# Set up Django's settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
django.setup()

from django.db import transaction
from shop.models import Category, Product
from shop.models import Category 

@transaction.atomic
def seed_data():

    products_data = [
        # Skincare
        {
            "category": "Skincare",
            "name": "CeraVe Hydrating Cleanser",
            "description": "A gentle and hydrating facial cleanser that effectively removes dirt and makeup without over-drying the skin.",
            "price": 12.99,
            "stock": 40,
        },
        {
            "category": "Skincare",
            "name": "Neutrogena Hydro Boost Water Gel",
            "description": "A hydrating water gel moisturizer that provides long-lasting hydration and a refreshed feel to the skin.",
            "price": 16.99,
            "stock": 35,
        },
        # Haircare
        {
            "category": "Haircare",
            "name": "Moroccanoil Treatment Oil",
            "description": "A nourishing hair treatment oil that conditions, strengthens, and adds shine to all hair types.",
            "price": 34.95,
            "stock": 25,
        },
        {
            "category": "Haircare",
            "name": "Herbal Essences Bio:Renew Shampoo",
            "description": "A revitalizing shampoo with natural ingredients that cleanses and refreshes the hair and scalp.",
            "price": 7.99,
            "stock": 30,
        },
        # Makeup
        {
            "category": "Makeup",
            "name": "Urban Decay Naked3 Eyeshadow Palette",
            "description": "A popular eyeshadow palette with 12 rosy-hued neutral shades for versatile eye makeup looks.",
            "price": 54.00,
            "stock": 15,
        },
        {
            "category": "Makeup",
            "name": "Maybelline Instant Age Rewind Concealer",
            "description": "A concealer that helps cover dark circles, imperfections, and signs of aging for a refreshed look.",
            "price": 9.99,
            "stock": 40,
        },
        # Fragrances
        {
            "category": "Fragrances",
            "name": "Chanel Coco Mademoiselle Eau de Parfum",
            "description": "A timeless and elegant fragrance with floral and oriental notes, perfect for special occasions.",
            "price": 105.00,
            "stock": 10,
        },
        {
            "category": "Fragrances",
            "name": "Dolce & Gabbana Light Blue Eau de Toilette",
            "description": "A fresh and vibrant fragrance with notes of citrus and cedarwood, ideal for everyday wear.",
            "price": 64.00,
            "stock": 20,
        },
        # Personal Hygiene
        {
            "category": "Personal Hygiene",
            "name": "Oral-B Pro 1000 Electric Toothbrush",
            "description": "An electric toothbrush with a pressure sensor and daily clean mode for effective oral hygiene.",
            "price": 49.99,
            "stock": 30,
        },
        {
            "category": "Personal Hygiene",
            "name": "Dove Sensitive Skin Body Wash",
            "description": "A gentle and hypoallergenic body wash that nourishes and cleanses sensitive skin.",
            "price": 7.49,
            "stock": 45,
        },
    ]

    for product in products_data:
        category = Category.objects.get(name=product['category'])
        product = Product.objects.create(
            category=category,
            name=product['name'],
            description=product['description'],
            price=product['price'],
            stock=product['stock'],
        )
        print(f'Product {product.name} created')

if __name__ == '__main__':
    seed_data()