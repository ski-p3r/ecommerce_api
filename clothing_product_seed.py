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
        # Men's Clothing
        {
            "category": "Men's Clothing",
            "name": "Men's Slim-Fit Suit",
            "description": "A classic slim-fit suit for men, perfect for formal occasions and business meetings.",
            "price": 299.99,
            "stock": 20,
        },
        {
            "category": "Men's Clothing",
            "name": "Men's Casual Denim Jeans",
            "description": "Comfortable and stylish denim jeans for everyday wear, available in various washes.",
            "price": 49.95,
            "stock": 50,
        },
        # Women's Clothing
        {
            "category": "Women's Clothing",
            "name": "Women's Floral Print Maxi Dress",
            "description": "A beautiful floral print maxi dress for women, suitable for summer events and vacations.",
            "price": 79.99,
            "stock": 30,
        },
        {
            "category": "Women's Clothing",
            "name": "Women's Yoga Leggings",
            "description": "High-quality yoga leggings with moisture-wicking fabric and a comfortable fit, perfect for workouts and yoga sessions.",
            "price": 29.95,
            "stock": 60,
        },
        # Kids' Clothing
        {
            "category": "Kids' Clothing",
            "name": "Boys' Graphic T-Shirt",
            "description": "Fun and colorful graphic t-shirts for boys, featuring their favorite cartoon characters.",
            "price": 14.99,
            "stock": 80,
        },
        {
            "category": "Kids' Clothing",
            "name": "Girls' Tutu Dress",
            "description": "Adorable tutu dresses for girls, perfect for special occasions and dress-up play.",
            "price": 24.95,
            "stock": 40,
        },
        # Shoes & Footwear
        {
            "category": "Shoes & Footwear",
            "name": "Men's Leather Oxford Shoes",
            "description": "Classic leather oxford shoes for men, suitable for both formal and casual wear.",
            "price": 89.99,
            "stock": 25,
        },
        {
            "category": "Shoes & Footwear",
            "name": "Women's Running Shoes",
            "description": "High-performance running shoes for women, designed for comfort and support during workouts.",
            "price": 79.95,
            "stock": 30,
        },
        # Sportswear
        {
            "category": "Sportswear",
            "name": "Men's Compression Shorts",
            "description": "Compression shorts for men, ideal for sports activities and muscle support.",
            "price": 34.99,
            "stock": 35,
        },
        {
            "category": "Sportswear",
            "name": "Women's Athletic Leggings",
            "description": "Athletic leggings for women with moisture-wicking fabric, perfect for workouts and sports.",
            "price": 44.95,
            "stock": 40,
        },
        # Lingerie & Sleepwear
        {
            "category": "Lingerie & Sleepwear",
            "name": "Women's Lace Chemise Set",
            "description": "Elegant lace chemise set for women, perfect for a comfortable and stylish night's sleep.",
            "price": 29.99,
            "stock": 20,
        },
        {
            "category": "Lingerie & Sleepwear",
            "name": "Men's Cotton Pajama Set",
            "description": "Cozy and soft cotton pajama set for men, featuring a relaxed fit for a good night's rest.",
            "price": 39.95,
            "stock": 25,
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