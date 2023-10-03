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

    categories_data = [
        {"name": "Electronics", "subcategories": ["Smartphones", "Laptops", "Headphones & Speakers", "Wearable Devices", "Cameras & Photography", "Accessories"]},
        {"name": "Clothing", "subcategories": ["Men's Clothing", "Women's Clothing", "Kids' Clothing", "Shoes & Footwear", "Sportswear", "Lingerie & Sleepwear"]},
        {"name": "Home & Kitchen", "subcategories": ["Furniture", "Kitchen Appliances", "Home Decor", "Bedding & Linens", "Cookware & Dining", "Cleaning Supplies"]},
        {"name": "Sports & Outdoors", "subcategories": ["Fitness Equipment", "Outdoor Gear", "Sports Apparel", "Biking", "Camping & Hiking", "Team Sports"]},
        {"name": "Books & Media", "subcategories": ["Fiction", "Non-Fiction", "Textbooks", "Movies & TV Shows", "Music", "Magazines"]},
        {"name": "Toys & Games", "subcategories": ["Action Figures & Playsets", "Board Games", "Outdoor Toys", "Puzzles", "Dolls & Accessories"]},
        {"name": "Beauty & Personal Care", "subcategories": ["Skincare", "Haircare", "Makeup", "Fragrances", "Personal Hygiene"]},
        {"name": "Automotive", "subcategories": ["Car Accessories", "Motorcycle Parts", "Car Care", "Tires & Wheels"]},
    ]
    m=1
    for items in categories_data:
        category = Category.objects.create(name=items["name"])
        print(f'{m} Creating {category.name} category')
        n=1
        for subitems in items["subcategories"]:
            cat = Category.objects.create(name=subitems, parent=category)
            print(f'{n} Creating {cat.name} subcategory')
            n+=1
        m+=1


if __name__ == '__main__':
    seed_data()
