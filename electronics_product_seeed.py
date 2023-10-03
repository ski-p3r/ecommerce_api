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
        {
            "category": "Smartphones",
            "name": "Apple iPhone 13 Pro Max",
            "description": "The latest flagship smartphone from Apple with a stunning Super Retina XDR display, A15 Bionic chip, and advanced camera system.",
            "price": 1099.00,
            "stock": 50,
        },
        {
            "category": "Smartphones",
            "name": "Samsung Galaxy S21 Ultra",
            "description": "Samsung's premium smartphone featuring a powerful Exynos processor, versatile camera setup, and a vibrant Dynamic AMOLED 2X screen.",
            "price": 1199.99,
            "stock": 45,
        },
        {
            "category": "Laptops",
            "name": "Dell XPS 13",
            "description": "An ultra-thin and lightweight laptop with an InfinityEdge display, Intel Core i7 processor, and exceptional build quality.",
            "price": 1299.99,
            "stock": 30,
        },
        {
            "category": "Laptops",
            "name": "MacBook Air M1",
            "description": "Apple's MacBook Air powered by the M1 chip, offering blazing-fast performance, silent operation, and all-day battery life.",
            "price": 999.00,
            "stock": 25,
        },
        {
            "category": "Headphones & Speakers",
            "name": "Sony WH-1000XM4 Noise-Canceling Headphones",
            "description": "High-quality over-ear headphones with industry-leading noise cancellation, superb sound quality, and long-lasting battery life.",
            "price": 349.99,
            "stock": 40,
        },
        {
            "category": "Headphones & Speakers",
            "name": "Bose SoundLink Revolve+ Bluetooth Speaker",
            "description": "A portable 360-degree Bluetooth speaker with deep, clear, and immersive sound for music on the go.",
            "price": 299.00,
            "stock": 20,
        },
        {
            "category": "Wearable Devices",
            "name": "Garmin Forerunner 945",
            "description": "A GPS smartwatch designed for serious athletes, featuring advanced training metrics, heart rate monitoring, and music storage.",
            "price": 599.99,
            "stock": 15,
        },
        {
            "category": "Wearable Devices",
            "name": "Fitbit Charge 5",
            "description": "A fitness and health tracker with an AMOLED display, stress management tools, and built-in GPS for outdoor workouts.",
            "price": 179.95,
            "stock": 35,
        },
        # Cameras & Photography
        {
            "category": "Cameras & Photography",
            "name": "Canon EOS 5D Mark IV",
            "description": "A professional-grade DSLR camera with a 30.4MP sensor, 4K video recording, and excellent low-light performance.",
            "price": 2499.00,
            "stock": 10,
        },
        {
            "category": "Cameras & Photography",
            "name": "Sony Alpha a6400 Mirrorless Camera",
            "description": "A compact mirrorless camera with fast autofocus, 4K video capabilities, and a tiltable touchscreen for vlogging.",
            "price": 899.99,
            "stock": 18,
        },
        # Accessories
        {
            "category": "Accessories",
            "name": "OtterBox Defender Series Phone Case",
            "description": "Rugged phone case with multi-layer defense against drops, dust, and scratches, designed for various smartphone models.",
            "price": 49.95,
            "stock": 100,
        },
        {
            "category": "Accessories",
            "name": "Samsonite Classic Business Laptop Bag",
            "description": "A durable and functional laptop bag with multiple compartments, perfect for professionals on the go.",
            "price": 59.99,
            "stock": 60,
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