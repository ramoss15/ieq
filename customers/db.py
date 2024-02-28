import datetime
import uuid

from flask import jsonify
import bcrypt


from db import get_db

db = get_db()


class CustomerDB:
	@classmethod
	def get_users(cls, email, required_fields=['id', 'name', 'email', 'user_type', 'password']):
		project = dict(_id=0)
		for field in required_fields:
			project.update({field: 1})
		return db.users.aggregate([{
			'$match': {
				'email': email
			}
		},
			{'$lookup':
				{
					'from': 'user_roles',
					"let": {"userID": "$user_type"},
					'pipeline': [
						{"$match": {"$expr": {"$eq": ["$id", "$$userID"]}}},
						{'$project': {
							'_id': 0,
							'name': 1
						}}
					],
					"as": "user_roles"
				},
				
			},
			{"$project":project}
		])
	
	@classmethod
	def get_user_role(cls, user_type):
		return db.user_roles.find_one({'id': user_type}, {'_id': False})
	
	@classmethod
	def create_user(cls, user):
		if not user.get('id'):
			user['id'] = uuid.uuid4().hex
		user['user_type'] = 2
		password_hash = bcrypt.hashpw(user.get('password').encode('utf-8'), bcrypt.gensalt())
		user['password'] = password_hash
		try:
			db.users.insert_one(user)
		except Exception as e:
			return False, e
		user.pop('password')
		user.pop('_id')
		return True, user
	
	@classmethod
	def get_user_sessions(cls, session_id):
		return db.user_sessions.find_one({'session_id': session_id}, {'_id': False})
	
	@classmethod
	def create_user_session(cls, user, session_id):
		expired_at = datetime.datetime.now() + datetime.timedelta(minutes=5)
		return db.user_sessions.insert_one({'session_id': session_id, "user_id": user.get("id"), "expire_at": expired_at})
	
	@classmethod
	def update_role(cls, data):
		return db.users.update_one({'id': data.get('id')}, {'$set': {'user_type': data.get('user_type')}})
	
	@classmethod
	def update_profile(cls, data, email):
		return db.users.update_one({'email': email}, {'$set': data})
