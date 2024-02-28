import uuid

from db import get_db

db = get_db()
class OrderDB:
	@classmethod
	def get_all_orders(cls, limit, offset):
		agr = db.orders.aggregate([{
			'$limit': limit
		},
			{
				'$skip': offset
			},
			{
				'$match': {
					'deleted': False
				}
			},
			{'$lookup':
				{
					'from': 'order_statuses',
					"let": {"order_status": "$order_status"},
					'pipeline': [
						{"$match": {"$expr": {"$eq": ["$id", "$$order_status"]}}},
						{'$project': {
							'_id': 0,
							'name': 1
						}}
					],
					"as": "order_status"
				},
				
			}
		])
		return list(agr)
	
	@classmethod
	def get_order(cls, order_id, required_fields=['id', 'order_id', 'order_status', 'total', 'user_id']):
		project = dict(_id=0)
		for field in required_fields:
			project.update({field: 1})
		agr = db.orders.aggregate([{
			'$match': {
				'order_id': order_id,
				'deleted': False
			}
		},
			{'$lookup':
				{
					'from': 'order_statuses',
					"let": {"order_status": "$order_status"},
					'pipeline': [
						{"$match": {"$expr": {"$eq": ["$id", "$$order_status"]}}},
						{'$project': {
							'_id': 0,
							'name': 1
						}}
					],
					"as": "order_status"
				},
				
			},
			{"$project": project}
		])
		return list(agr)
	
	@classmethod
	def create_order(cls, data):
		data['deleted'] = False
		try:
			db.orders.insert_one(data)
		except Exception as e:
			return False, e
		data.pop('_id')
		return True, data
	
	@classmethod
	def update_order(cls, order_id, data):
		return db.orders.update_one({'order_id': order_id}, {'$set': data})
	
	@classmethod
	def delete_order(cls, order_id):
		return db.orders.update_one({'order_id': order_id}, {'$set': {'deleted': True}})
	
	@classmethod
	def get_order_statuses(cls, order_status):
		return db.order_statuses.find_one({'id': order_status}, {'_id': False})
