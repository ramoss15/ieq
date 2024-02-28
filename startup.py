import logging
import uuid

import bcrypt

from db import get_db_client, db_name
from generate_dummy_products import dummy_products
from elasticsearch_client import create_index, create_index_data

db_client = get_db_client()
logging.info(f"db connected {db_client} {db_name}")
logging.info("database setting up...")


def generate_index(db, col: str, key: str, **conditions):
	if not conditions:
		conditions.update({'unique': True})
	db[col].create_index(key, **conditions)


collections_index_map: dict = {
	'users': 'email', 'products': 'id', 'orders': 'order_id', 'user_roles': 'id', 'product_categories': 'id',
	'order_statuses': 'id', "user_sessions": "session_id"
}

orders_status = [
	{'id': 1, 'name': 'Pending'}, {'id': 2, 'name': 'Processing'}, {'id': 3, 'name': 'Shipped'},
	{'id': 4, 'name': 'Delivered'}, {'id': 5, 'name': 'Cancelled'}, {'id': 6, 'name': 'Returned'},
	{'id': 7, 'name': 'Failed'}, {'id': 8, 'name': 'Refunded'}, {'id': 9, 'name': 'Partially Refunded'},
	{'id': 10, 'name': 'Refund Requested'}, {'id': 11, 'name': 'Refund Accepted'},
	{'id': 12, 'name': 'Refund Declined'}, {'id': 13, 'name': 'Refund Completed'}
]
user_roles = [
	{'id': 1, 'name': 'Admin'}, {'id': 2, 'name': 'User'}, {'id': 3, 'name': 'Guest'}
]
# db_client.drop_database(db_name)
dblist = db_client.list_database_names()

if db_name not in dblist:
	db = db_client[db_name]
	db_cols = db.list_collection_names()
	for col, key in collections_index_map.items():
		if col not in db_cols:
			db.create_collection(col)
			generate_index(db, col, key)
			if col == 'products':
				logging.info(f"Generating {col} collection")
				create_index(col)
				# Generate dummy products
				products, categories = dummy_products(1000)
				for product in products:
					product.update({'deleted': False})
					create_index_data(col, product)
				db.products.insert_many(products)
			elif col == 'product_categories':
				# Generate dummy product categories
				products, categories = dummy_products(0)
				db.product_categories.insert_many(categories)
			elif col == 'order_statuses':
				# Generate dummy order statuses
				db.order_statuses.insert_many(orders_status)
			elif col == 'user_roles':
				# Generate dummy user roles
				db.user_roles.insert_many(user_roles)
			elif col == "user_sessions":
				db[col].create_index('expire_at', expireAfterSeconds=86400)
			elif col == "users":
				user = {"id": uuid.uuid4().hex, "email": "admin@admin.com", "user_type": 1,
				        "password": bcrypt.hashpw('password'.encode('utf-8'), bcrypt.gensalt())}
				db.users.insert_one(user)
logging.info("database setting completed...")
