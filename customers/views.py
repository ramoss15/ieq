import bcrypt
from flask import Blueprint, request, jsonify
from pymongo.errors import DuplicateKeyError

from customers import CustomerDB, Auth
from utils import validate_json, validate_schema

customer = Blueprint('customer', __name__, url_prefix='/customer')


@customer.route('/signup', methods=['POST'], endpoint='user_signup')
@validate_json
@validate_schema(keys=dict(name=str, email=str, password=str))
def user_signup():
	data = request.json
	status, data = CustomerDB.create_user(data)
	if not status:
		if isinstance(data, DuplicateKeyError):
			data = "user already exists"
		if isinstance(data, Exception):
			data = str(data)
		return jsonify({"error": data}), 400
	response = jsonify(data)
	encoded_jwt = Auth.authorize(data)
	response.headers.update({'Authorization': f'Bearer {encoded_jwt}', 'Content-Type': 'application/json'})
	return response

@customer.route('/login', methods=['POST'], endpoint='user_login')
@validate_json
@validate_schema(keys=dict(email=str, password=str))
def user_login():
	data = request.json
	get_user = list(CustomerDB.get_users(data.get('email'),  required_fields=['id', 'name', 'email', 'password']))
	if not get_user:
		return jsonify({"error": "user not found"}), 400
	password_hash = get_user[0].get('password')
	if not bcrypt.checkpw(data.get('password').encode('utf-8'), password_hash):
		return jsonify({"error": "invalid credentials"}), 400
	get_user[0].pop('password')
	encoded_jwt = Auth.authorize(get_user[0])
	response = jsonify(get_user)
	response.headers.update({'Authorization': f'Bearer {encoded_jwt}', 'Content-Type': 'application/json'})
	return response

@customer.route('/profile', methods=['GET'], endpoint='get_profile')
@Auth.authenticate
def get_profile():
	get_user = list(CustomerDB.get_users(request.email, required_fields=['id', 'name', 'email']))
	response = jsonify(get_user)
	return response

@customer.route('/update_profile', methods=['PATCH'], endpoint='update_profile')
@Auth.authenticate
@validate_json
@validate_schema(keys=dict(name=str))
def update_profile():
	data = request.json
	CustomerDB.update_profile(data, request.email)
	return jsonify(data), 200


@customer.route('/update_role', methods=['PATCH'], endpoint='update_role')
@Auth.authenticate(user="Admin")
@validate_json
@validate_schema(keys=dict(id=str, user_type=str))
def update_role():
	data = request.json
	user = CustomerDB.get_users(data.get('id'))
	if not user:
		return jsonify({"error": "user not found"}), 400
	CustomerDB.update_role(data)
	return jsonify(data), 200
