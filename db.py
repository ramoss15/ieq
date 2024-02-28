import pymongo

db_name = 'ieq_db'

CONNECTION_STRING ="mongodb://mongo_db:A1ym%25b521Or@127.0.0.1:1236/?directConnection=true"


def get_db():
	dbclient = get_db_client()
	db = dbclient[db_name]
	return db


def get_db_client():
	dbclient = pymongo.MongoClient(CONNECTION_STRING)
	return dbclient
