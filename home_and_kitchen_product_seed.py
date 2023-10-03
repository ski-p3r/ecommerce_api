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
        # Furniture
        {
            "category": "Furniture",
            "name": "3-Piece Living Room Set",
            "description": "A stylish and comfortable living room set including a sofa, loveseat, and coffee table.",
            "price": 899.99,
            "stock": 15,
        },
        {
            "category": "Furniture",
            "name": "Wooden Dining Table and Chairs",
            "description": "A durable wooden dining table with matching chairs, perfect for family gatherings and dinners.",
            "price": 449.00,
            "stock": 20,
        },
        # Kitchen Appliances
        {
            "category": "Kitchen Appliances",
            "name": "Stainless Steel Refrigerator",
            "description": "A spacious stainless steel refrigerator with advanced cooling technology and a sleek design.",
            "price": 1299.00,
            "stock": 10,
        },
        {
            "category": "Kitchen Appliances",
            "name": "Instant Pot Multi-Cooker",
            "description": "A versatile multi-cooker with various cooking functions, making meal preparation fast and easy.",
            "price": 99.95,
            "stock": 30,
        },
        # Home Decor
        {
            "category": "Home Decor",
            "name": "Decorative Throw Pillows (Set of 4)",
            "description": "A set of four decorative throw pillows with stylish patterns, perfect for enhancing your home decor.",
            "price": 34.99,
            "stock": 25,
        },
        {
            "category": "Home Decor",
            "name": "Modern Wall Art Canvas Prints",
            "description": "A collection of modern canvas prints to add an artistic touch to your living space.",
            "price": 79.99,
            "stock": 15,
        },
        # Bedding & Linens
        {
            "category": "Bedding & Linens",
            "name": "Queen-size Comforter Set",
            "description": "A cozy queen-size comforter set with matching shams and decorative pillows.",
            "price": 69.95,
            "stock": 20,
        },
        {
            "category": "Bedding & Linens",
            "name": "Luxury Egyptian Cotton Sheets",
            "description": "High-quality Egyptian cotton sheets for a comfortable and luxurious night's sleep.",
            "price": 129.00,
            "stock": 25,
        },
        # Cookware & Dining
        {
            "category": "Cookware & Dining",
            "name": "Non-Stick Cookware Set (10-Piece)",
            "description": "A 10-piece non-stick cookware set with pots, pans, and utensils for versatile cooking.",
            "price": 149.99,
            "stock": 12,
        },
        {
            "category": "Cookware & Dining",
            "name": "Fine China Dinnerware Set (Service for 8)",
            "description": "Elegant fine china dinnerware set with service for 8, perfect for special occasions.",
            "price": 249.00,
            "stock": 8,
        },
        # Cleaning Supplies
        {
            "category": "Cleaning Supplies",
            "name": "Robotic Vacuum Cleaner",
            "description": "A robotic vacuum cleaner with smart navigation and automatic cleaning modes for a tidy home.",
            "price": 299.00,
            "stock": 10,
        },
        {
            "category": "Cleaning Supplies",
            "name": "Multi-Surface Cleaning Spray (Pack of 3)",
            "description": "A pack of three multi-surface cleaning sprays for effective and convenient cleaning.",
            "price": 14.95,
            "stock": 50,
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