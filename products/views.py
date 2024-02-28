from flask import Blueprint, jsonify, request

from customers import Auth
from elasticsearch_client import delete_index_data, create_index_data, search_product
from products import productDB, Error, Constants, NameSpace
from redis_helper import RedisCache
from utils import validate_schema, validate_json

product = Blueprint('product', __name__, url_prefix='/product')


@product.route('/', endpoint='get_all_product')
@Auth.authenticate
def get_all_products():
	try:
		limit = int(request.args.get('limit'))
	except:
		limit = 10
	try:
		offset = int(request.args.get('offset'))
	except:
		offset = 0
	products = productDB.get_all_products(limit, offset)
	if not products:
		return jsonify({"error": Error.NO_PRODUCTS_FOUND.value}), 404
	return jsonify(products), 200


@product.route('/product/<product_id>', endpoint='get_product')
@Auth.authenticate
def get_product(product_id):
	product = RedisCache.get_with_key(product_id, NameSpace.PRODUCTS.value)
	if not product:
		product = productDB.get_product(product_id)
		if not product:
			return jsonify({"error": Error.PRODUCT_NOT_FOUND.value}), 404
		RedisCache.key_with_ttl(product_id, product, 3600, NameSpace.PRODUCTS.value)
	return jsonify(product), 200


@product.route('/product/name/<name>', endpoint='get_all_product_by_name')
@Auth.authenticate
def get_product_by_name(name):
	product = RedisCache.get_with_key(name, NameSpace.PRODUCTS.value)
	if not product:
		product = productDB.get_product_by_name(name)
		if not product:
			return jsonify({"error": Error.PRODUCT_NOT_FOUND.value}), 404
		RedisCache.key_with_ttl(name, product, 3600, NameSpace.PRODUCTS.value)
	return jsonify(product), 200


@product.route('/product/category/<category>', endpoint='get_all_product_bycategory')
@Auth.authenticate
def get_products_by_category(category):
	products = productDB.get_products_by_category(category)
	if not products:
		return jsonify({"error": Error.PRODUCT_NOT_FOUND.value}), 404
	return jsonify(products), 200


@product.route('/product', methods=['POST'], endpoint='create_product')
@validate_json
@validate_schema(
	keys={'name': str, 'description': str, 'category': str, 'price': float, 'stock': int, 'image': str, 'rating': float,
	      'reviews': list})
@Auth.authenticate(user="Admin")
def create_product():
	data = request.json
	status, data = productDB.create_product(data)
	create_index_data(NameSpace.PRODUCTS.value, data)
	RedisCache.key_with_ttl(data.get('id'), product, 3600, NameSpace.PRODUCTS.value)
	if not status:
		return jsonify({"error": data}), 400
	return jsonify(data), 201


@product.route('/product', methods=['PATCH'], endpoint='update_product')
@validate_json
@validate_schema(keys={'id': int})
@Auth.authenticate(user="Admin")
def update_product():
	product_columens = ['name', 'description', 'category', 'price', 'stock', 'image', 'rating', 'reviews']
	data = request.json
	
	get_product = productDB.get_product(data.get('id'))
	if data.get('name') != get_product.get('name'):
		delete_index_data(NameSpace.PRODUCTS.value, data.get('id'))
	if not get_product:
		return jsonify({"error": Error.PRODUCT_NOT_FOUND.value}), 404
	get_product.update(data)
	for key in get_product:
		if key not in product_columens:
			get_product.pop(key)
	productDB.update_product(data.get('id'), data)
	create_index_data(NameSpace.PRODUCTS.value, get_product)
	return jsonify({"message": Constants.PRODUCT_UPDATED.value}), 201


@product.route('/product', methods=['DELETE'], endpoint='delete_product')
@validate_json
@validate_schema(keys={'id': int})
@Auth.authenticate(user="Admin")
def delete_product():
	data = request.json
	get_product = productDB.get_product(data.get('id'))
	if not get_product:
		return jsonify({"error": Error.PRODUCT_NOT_FOUND.value}), 404
	productDB.delete_product(data.get('id'))
	delete_index_data(NameSpace.PRODUCTS.value, data.get('id'))
	return jsonify({"message": Constants.PRODUCT_DELETED.value}), 200


@product.route('/products/searching', endpoint='product_searching')
@Auth.authenticate
def get_products_by_searching():
	term = request.args.get('term')
	if len(term) < 3:
		return jsonify({"error": Error.Short_term.value}), 400
	product_ids = search_product(NameSpace.PRODUCTS.value, term)
	if not product_ids:
		return jsonify({"error": Error.NO_PRODUCTS_FOUND.value}), 404
	products = productDB.get_product_by_ids(product_ids)
	if not products:
		return jsonify({"error": Error.NO_PRODUCTS_FOUND.value}), 404
	return jsonify({"products": products}), 200
