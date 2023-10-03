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
        # Fiction
        {
            "category": "Fiction",
            "name": "The Great Gatsby by F. Scott Fitzgerald",
            "description": "A classic novel set in the Roaring Twenties, exploring themes of wealth, love, and the American Dream.",
            "price": 14.99,
            "stock": 25,
        },
        {
            "category": "Fiction",
            "name": "To Kill a Mockingbird by Harper Lee",
            "description": "A Pulitzer Prize-winning novel that addresses issues of racial injustice and morality in the American South.",
            "price": 12.95,
            "stock": 30,
        },
        # Non-Fiction
        {
            "category": "Non-Fiction",
            "name": "Sapiens: A Brief History of Humankind by Yuval Noah Harari",
            "description": "A thought-provoking exploration of the history of Homo sapiens, from ancient times to the present day.",
            "price": 16.99,
            "stock": 20,
        },
        {
            "category": "Non-Fiction",
            "name": "Becoming by Michelle Obama",
            "description": "An intimate memoir by the former First Lady of the United States, sharing her life's journey and experiences.",
            "price": 18.95,
            "stock": 15,
        },
        # Textbooks
        {
            "category": "Textbooks",
            "name": "Introduction to Psychology (10th Edition)",
            "description": "A comprehensive textbook that provides an overview of key concepts in psychology.",
            "price": 89.99,
            "stock": 10,
        },
        {
            "category": "Textbooks",
            "name": "Calculus: Early Transcendentals (8th Edition)",
            "description": "A widely-used calculus textbook that covers fundamental mathematical concepts.",
            "price": 79.95,
            "stock": 8,
        },
        # Movies & TV Shows
        {
            "category": "Movies & TV Shows",
            "name": "The Shawshank Redemption (Blu-ray)",
            "description": "A critically acclaimed film based on Stephen King's novella, known for its powerful storytelling and performances.",
            "price": 14.99,
            "stock": 20,
        },
        {
            "category": "Movies & TV Shows",
            "name": "Stranger Things: Season 1 (DVD)",
            "description": "The first season of the popular Netflix series filled with supernatural mysteries and '80s nostalgia.",
            "price": 24.95,
            "stock": 25,
        },
        # Music
        {
            "category": "Music",
            "name": "The Beatles - Abbey Road (Vinyl LP)",
            "description": "A classic album by The Beatles, featuring iconic tracks like 'Come Together' and 'Here Comes the Sun.'",
            "price": 29.99,
            "stock": 15,
        },
        {
            "category": "Music",
            "name": "Billie Eilish - When We All Fall Asleep, Where Do We Go? (CD)",
            "description": "A Grammy-winning album by Billie Eilish, known for its unique sound and emotional depth.",
            "price": 12.99,
            "stock": 30,
        },
        # Magazines
        {
            "category": "Magazines",
            "name": "National Geographic (Annual Subscription)",
            "description": "A renowned magazine that covers topics related to science, nature, culture, and exploration.",
            "price": 39.99,
            "stock": 100,
        },
        {
            "category": "Magazines",
            "name": "Vogue (Monthly Issue)",
            "description": "A fashion and lifestyle magazine featuring the latest trends, celebrity interviews, and style inspiration.",
            "price": 5.99,
            "stock": 150,
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