from functools import wraps

import jwt
from flask import request, jsonify
import bcrypt
from werkzeug.exceptions import BadRequest

from customers import CustomerDB


class Auth:
	
	@classmethod
	def authenticate(cls, user=None):
		def auth(f):
			"""
			A decorator to authenticate the function using the Authorization header.
			"""
			@wraps(f)
			def wrapper(*args, **kw):
				try:
					headers = request.headers
					if not headers.get('Authorization'):
						return jsonify({"error": "Authorization header not found"}), 401
					token = headers.get('Authorization').replace('Bearer ', '')
					if not token:
						return jsonify({"error": "Authorization header not found"}), 401
					get_user = CustomerDB.get_user_sessions(token)
					if not get_user:
						return jsonify({"error": "You are not authorized"}), 401
					if user:
						user_data = list(CustomerDB.get_users(get_user.get('user_id'), required_fields=['user_type']))
						user_role = CustomerDB.get_user_role(user_data[0].get('user_type'))
						if user != user_role.get('name'):
							return jsonify({"error": "You are not authorized"}), 401
				except BadRequest as e:
					msg = "payload must be a valid json"
					return jsonify({"error": msg}), 400, {'Content-Type': 'application/json'}
				request.email = get_user.get('email')
				return f(*args, **kw)
			
			return wrapper
		return auth
	
	@classmethod
	def authorize(cls, user: dict):
		get_session = CustomerDB.get_user_sessions_by_id(user.get('id'))
		if  get_session:
			return get_session.get('session_id')
		else:
			encoded_jwt = jwt.encode(user, 'secret', algorithm='HS256')
			CustomerDB.create_user_session(user, encoded_jwt)
		return encoded_jwt
