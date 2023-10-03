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
        # Action Figures & Playsets
        {
            "category": "Action Figures & Playsets",
            "name": "Marvel Avengers Action Figure Set",
            "description": "A set of action figures featuring iconic Marvel Avengers characters for imaginative play and display.",
            "price": 34.99,
            "stock": 30,
        },
        {
            "category": "Action Figures & Playsets",
            "name": "LEGO Star Wars Millennium Falcon Set",
            "description": "A LEGO Star Wars Millennium Falcon set with minifigures and detailed interior, perfect for Star Wars fans.",
            "price": 149.95,
            "stock": 20,
        },
        # Board Games
        {
            "category": "Board Games",
            "name": "Settlers of Catan Board Game",
            "description": "A popular board game where players collect and trade resources to build roads, settlements, and cities.",
            "price": 39.99,
            "stock": 25,
        },
        {
            "category": "Board Games",
            "name": "Ticket to Ride Board Game",
            "description": "A strategy board game where players compete to complete train routes across North America.",
            "price": 44.95,
            "stock": 30,
        },
        # Outdoor Toys
        {
            "category": "Outdoor Toys",
            "name": "Nerf N-Strike Elite Disruptor Blaster",
            "description": "A Nerf blaster with quick-draw rotating barrels for action-packed outdoor play.",
            "price": 19.99,
            "stock": 40,
        },
        {
            "category": "Outdoor Toys",
            "name": "Frisbee Disc Golf Set",
            "description": "A disc golf set with everything you need to play this fun outdoor sport with friends and family.",
            "price": 34.95,
            "stock": 20,
        },
        # Puzzles
        {
            "category": "Puzzles",
            "name": "1000-Piece Jigsaw Puzzle: World Map",
            "description": "A challenging jigsaw puzzle featuring a detailed world map for hours of entertainment.",
            "price": 19.95,
            "stock": 15,
        },
        {
            "category": "Puzzles",
            "name": "3D Wooden Brain Teaser Puzzle Set",
            "description": "A set of brain-teasing wooden puzzles that test your problem-solving skills and creativity.",
            "price": 29.99,
            "stock": 25,
        },
        # Dolls & Accessories
        {
            "category": "Dolls & Accessories",
            "name": "Barbie Dreamhouse Playset",
            "description": "A deluxe Barbie Dreamhouse playset with multiple rooms and accessories for imaginative play.",
            "price": 169.99,
            "stock": 10,
        },
        {
            "category": "Dolls & Accessories",
            "name": "American Girl Doll: Grace Thomas",
            "description": "An American Girl doll named Grace Thomas, perfect for young collectors and fans.",
            "price": 129.00,
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