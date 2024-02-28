import uuid

from db import get_db

db = get_db()


class productDB:
	@classmethod
	def get_all_products(cls, limit=10, offset=0):
		return list(db.products.find({}, {'_id': False}).limit(limit).skip(offset))
	
	@classmethod
	def get_product(cls, product_id: int):
		return db.products.find_one({'id': product_id}, {'_id': False})
	
	@classmethod
	def get_product_by_ids(cls, product_ids: list):
		return list(db.products.find({'id': {'$in': product_ids}}, {'_id': False}))
	
	@classmethod
	def get_product_by_name(cls, name: str):
		return db.products.find_one({'name': name}, {'_id': False})
	
	@classmethod
	def get_products_by_category(cls, category: str):
		return list(db.products.find({'category': category}, {'_id': False}))
	
	@classmethod
	def create_product(cls, product):
		last_product = db.products.find_one({}, sort={'_id': -1})
		product['id'] = last_product.get("id")+1
		category = db.categories.find_one({'category': product.get('category')})
		if not category:
			category_id = uuid.uuid4().hex
			db.categories.insert_one({'category': product.get('category'), 'id': category_id})
		else:
			category_id = category.get('id')
		product['category_id'] = category_id
		try:
			db.products.insert_one(product)
		except Exception as e:
			return False, e
		product.pop('_id')
		return True, product
	
	@classmethod
	def update_product(cls, product_id, product):
		return db.products.update_one({'id': product_id}, {'$set': product})
	
	@classmethod
	def delete_product(cls, product_id):
		return db.products.delete_one({'id': product_id})
	
	@classmethod
	def get_all_categories(cls):
		return list(db.categories.find({}, {'_id': False}))
	
	@classmethod
	def get_category(cls, category_id):
		return db.categories.find_one({'id': category_id}, {'_id': False})
	
	@classmethod
	def create_category(cls, category):
		try:
			db.categories.insert_one(category)
		except Exception as e:
			return False, e
		category.pop('_id')
		return True, category
	
	@classmethod
	def update_category(cls, category_id, category):
		return db.categories.update_one({'id': category_id}, {'$set': category})
	
	@classmethod
	def delete_category(cls, category_id):
		return db.categories.delete_one({'id': category_id})
