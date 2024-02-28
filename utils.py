from functools import wraps

from flask import request, jsonify
from werkzeug.exceptions import BadRequest
from werkzeug.routing import ValidationError


def validate_json(f):
	@wraps(f)
	def wrapper(*args, **kw):
		try:
			request.json
		except BadRequest as e:
			msg = "payload must be a valid json"
			return jsonify({"error": msg}), 400, {'Content-Type': 'application/json'}
		return f(*args, **kw)
	
	return wrapper


def validate_schema(keys: dict):
	def decorator(f):
		@wraps(f)
		def wrapper(*args, **kw):
			try:
				data: dict = request.json
				for key, types in keys.items():
					if data.get(key) and not isinstance(data.get(key), types):
						return jsonify({"error": f"{key} must be {types}"}), 400
					elif not data.get(key):
						return jsonify({"error": f"{key} is required"}), 400
			except ValidationError as e:
				return jsonify({"error": e}), 400
			return f(*args, **kw)
		
		return wrapper
	
	return decorator
