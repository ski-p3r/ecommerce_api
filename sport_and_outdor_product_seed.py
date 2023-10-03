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
        # Fitness Equipment
        {
            "category": "Fitness Equipment",
            "name": "Treadmill with Incline",
            "description": "A high-quality treadmill with adjustable incline, perfect for cardio workouts at home.",
            "price": 899.99,
            "stock": 10,
        },
        {
            "category": "Fitness Equipment",
            "name": "Adjustable Dumbbell Set",
            "description": "An adjustable dumbbell set with various weight options for strength training.",
            "price": 199.95,
            "stock": 15,
        },
        # Outdoor Gear
        {
            "category": "Outdoor Gear",
            "name": "Camping Tent for 4 People",
            "description": "A spacious camping tent that accommodates up to 4 people, ideal for outdoor adventures.",
            "price": 149.00,
            "stock": 20,
        },
        {
            "category": "Outdoor Gear",
            "name": "Hiking Backpack with Hydration System",
            "description": "A comfortable hiking backpack with a built-in hydration system for long hikes.",
            "price": 79.99,
            "stock": 30,
        },
        # Sports Apparel
        {
            "category": "Sports Apparel",
            "name": "Men's Compression Leggings",
            "description": "Compression leggings for men, designed to enhance performance and reduce muscle fatigue during workouts.",
            "price": 39.95,
            "stock": 25,
        },
        {
            "category": "Sports Apparel",
            "name": "Women's Yoga Pants with Pockets",
            "description": "Yoga pants for women with convenient pockets, perfect for yoga sessions and active lifestyles.",
            "price": 29.99,
            "stock": 35,
        },
        # Biking
        {
            "category": "Biking",
            "name": "Mountain Bike with Full Suspension",
            "description": "A rugged mountain bike with full suspension, suitable for off-road biking adventures.",
            "price": 699.00,
            "stock": 8,
        },
        {
            "category": "Biking",
            "name": "Cycling Helmet with LED Lights",
            "description": "A cycling helmet with integrated LED lights for safety during night rides.",
            "price": 49.95,
            "stock": 15,
        },
        # Camping & Hiking
        {
            "category": "Camping & Hiking",
            "name": "Portable Camping Stove",
            "description": "A compact and portable camping stove for cooking meals outdoors.",
            "price": 34.99,
            "stock": 20,
        },
        {
            "category": "Camping & Hiking",
            "name": "Hiking Boots with Waterproof Membrane",
            "description": "Durable hiking boots with a waterproof membrane to keep your feet dry on wet trails.",
            "price": 89.95,
            "stock": 18,
        },
        # Team Sports
        {
            "category": "Team Sports",
            "name": "Soccer Ball (Size 5)",
            "description": "A regulation-size soccer ball suitable for practice and matches.",
            "price": 19.99,
            "stock": 40,
        },
        {
            "category": "Team Sports",
            "name": "Basketball Hoop with Adjustable Height",
            "description": "An adjustable-height basketball hoop for hours of outdoor fun and practice.",
            "price": 199.00,
            "stock": 12,
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