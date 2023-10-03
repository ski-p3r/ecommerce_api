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
        # Car Accessories
        {
            "category": "Car Accessories",
            "name": "Anker Roav Dash Cam",
            "description": "A high-resolution dash cam that records clear footage of your drives and provides extra security on the road.",
            "price": 89.99,
            "stock": 25,
        },
        {
            "category": "Car Accessories",
            "name": "Motor Trend All Season Rubber Floor Mats",
            "description": "Heavy-duty rubber floor mats to protect your car's interior from dirt, spills, and wear.",
            "price": 29.95,
            "stock": 40,
        },
        # Motorcycle Parts
        {
            "category": "Motorcycle Parts",
            "name": "Yoshimura RS-5 Slip-On Exhaust",
            "description": "A performance-enhancing slip-on exhaust system designed for sport motorcycles.",
            "price": 349.00,
            "stock": 12,
        },
        {
            "category": "Motorcycle Parts",
            "name": "Biltwell Gringo S Helmet",
            "description": "A retro-style full-face motorcycle helmet with DOT safety certification and various color options.",
            "price": 169.95,
            "stock": 18,
        },
        # Car Care
        {
            "category": "Car Care",
            "name": "Meguiar's Ultimate Car Wash Kit",
            "description": "A comprehensive car wash kit that includes everything you need to keep your car clean and shiny.",
            "price": 39.99,
            "stock": 20,
        },
        {
            "category": "Car Care",
            "name": "Armor All Tire Foam",
            "description": "A tire foam that cleans, shines, and protects your car's tires with a long-lasting gloss finish.",
            "price": 7.99,
            "stock": 35,
        },
        # Tires & Wheels
        {
            "category": "Tires & Wheels",
            "name": "Michelin Defender T+H All-Season Tire",
            "description": "An all-season tire known for its durability, traction, and long-lasting performance.",
            "price": 129.00,
            "stock": 15,
        },
        {
            "category": "Tires & Wheels",
            "name": "Konig Hypergram Alloy Wheel",
            "description": "A lightweight alloy wheel with a stylish design, ideal for enhancing your vehicle's appearance.",
            "price": 169.95,
            "stock": 10,
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