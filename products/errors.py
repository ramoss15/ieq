from enum import Enum


class Error(Enum):
	NO_PRODUCTS_FOUND = "No products found"
	PRODUCT_NOT_FOUND = "Product not found"
	PRODUCT_ALREADY_EXISTS = "Product already exists"
	Short_term = "Name must be at least 3 characters"
