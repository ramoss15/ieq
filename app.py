import logging

from flask import Flask, render_template

from customers import customer
from orders import order
from products import product
import startup
from redis_helper import RedisCache

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
logging.info(f"redis connected: {RedisCache.redis_client.client()}")

app.register_blueprint(customer)
app.register_blueprint(order)
app.register_blueprint(product)

@app.route('/')
def index():
	return render_template("index.html")


if __name__ == '__main__':
	app.run()
