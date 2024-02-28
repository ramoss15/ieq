from enum import Enum

class Constants(Enum):
	PRODUCT_UPDATED = "product updated successfully"
	PRODUCT_CREATED = "product created successfully"
	PRODUCT_DELETED = "product deleted successfully"

class NameSpace(Enum):
	PRODUCTS = "products"
	Category = "categories"
