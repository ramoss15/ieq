import uuid

from flask import Blueprint, request, jsonify

from customers import Auth
from products import productDB
from orders import OrderDB
from utils import validate_json, validate_schema

order = Blueprint('order', __name__, url_prefix='/order')


@order.route('/get_all_orders', endpoint='get_all_orders')
@Auth.authenticate()
def get_all_orders():
	user_id = request.user_id
	limit = 10
	offset = request.args.get('offset')
	offset = int(offset) if offset else 10
	orders = OrderDB.get_all_orders(user_id, limit, offset)
	return jsonify({"orders": orders}), 200


@order.route('/get_order/<order_id>', endpoint='get_order')
@Auth.authenticate()
def get_order(order_id):
	user_id = request.user_id
	order = OrderDB.get_order(order_id, user_id)
	if not order:
		return jsonify({"error": "order not found"}), 404
	return jsonify(order), 200


@order.route('/create_order', methods=['POST'], endpoint='create_order')
@validate_json
@validate_schema(keys=dict(products=list, address=str, phone=str))
@Auth.authenticate()
def create_order():
	data: dict = request.json
	if len(data.get('address')) < 10:
		return jsonify({"error": "address must be at least 10 characters"}), 400
	if len(data.get('phone')) != 10:
		return jsonify({"error": "phone must be 10 characters"}), 400
	total: int = 0
	product_ids: dict = dict()
	for product in data.get('products'):
		product_ids[(product.get('id'))] = product_ids.get(product.get('id'), 0) + product.get('count', 1)
	products = productDB.get_product_by_ids(list(product_ids.keys()))
	for product in products:
		if product.get('stock') < product_ids.get(product.get('id')):
			return jsonify({"error": "not enough stock"}), 400
		total += product.get('price') * product_ids.get(product.get('id'))
		product.update({'count': product_ids.get(product.get('id'))})
		product.update({'total': product.get('price') * product_ids.get(product.get('id'))})
		product_ids.pop(product.get('id'))
	if product_ids:
		return jsonify({"error": "Some invalid product ordered"}), 400
	
	data['products'] = products
	data['total'] = total
	data['order_status'] = 1
	if total == 0:
		return jsonify({"error": "total must be greater than 0"}), 400
	
	data['order_id'] = uuid.uuid4().hex
	data['user_id'] = request.user_id
	status, data = OrderDB.create_order(data)
	if not status:
		return jsonify({"error": data}), 400
	return jsonify(data), 201


@order.route('/update_order/<order_id>', methods=['PATCH'], endpoint='update_order')
@validate_json
@validate_schema(keys=dict(order_status=int))
@Auth.authenticate(user="Admin")
def update_order(order_id):
	data = request.json
	get_order_statuses = OrderDB.get_order_statuses(data.get('order_status'))
	if not get_order_statuses:
		return jsonify({"error": "order status not allowed"}), 404
	status, data = OrderDB.update_order(order_id, data)
	if not status:
		return jsonify({"error": data}), 400
	return jsonify(data), 200


@order.route('/delete_order/<order_id>', methods=['DELETE'], endpoint='delete_order')
@Auth.authenticate(user="Admin")
def delete_order(order_id):
	order = OrderDB.get_order(order_id)
	if not order:
		return jsonify({"error": "order not found"}), 404
	OrderDB.delete_order(order_id)
	return jsonify({"message": "order deleted"}), 200
