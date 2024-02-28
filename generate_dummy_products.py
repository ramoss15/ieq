import random

import string
import uuid

import logging

def generate_product_ids(pruduct_ids):
	product_id = f"prod_{random.randint(100000, 999999)}"
	if product_id in pruduct_ids:
		return generate_product_ids(pruduct_ids)
	else:
		pruduct_ids.append(product_id)
		return pruduct_ids, product_id


def dummy_products(number):
	logging.info(f"Generating {number} dummy products")
	
	# Define product categories
	categories = ["Electronics", "Clothing", "Home & Garden", "Beauty", "Sports & Outdoors"]
	product_categories:list[dict] = [{'id': uuid.uuid4().hex, 'category': category} for category in categories]
	
	# Generate dummy product data
	products = list()
	product_ids = []
	
	for idex,_ in enumerate(range(number)):
		product_category = random.choice(product_categories)
		product = {
			"id": idex+1,
			"name": f"Product {random.randint(1, 1000)}",
			"description": f"This is a description for product {random.randint(1, 1000)}. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
			"category": product_category.get('category'),
			"category_id": product_category.get('id'),
			"price": round(random.uniform(10.00, 10000.00), 2),
			"stock": random.randint(10, 100),
			"image": f"https://picsum.photos/200/200?random={random.randint(1, 1000)}",
			"rating": round(random.uniform(3.00, 5.00), 1),
			"reviews": []
		}
		products.append(product)
	return products, product_categories
