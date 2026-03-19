from flask import Blueprint, jsonify

main_bp = Blueprint('main_bp', __name__)

# User auth
@main_bp.route('/login', methods=['POST'])
def login():
    return jsonify({"message": "Login"})

# Show the products
@main_bp.route('/products', method=['GET'])
def products():
    return jsonify({"message": "View Products:"})

# Add products
@main_bp.route('/products', method=['POST'])
def create_product():
    return jsonify({"message": "Route to add products"})

# Show product details
@main_bp.route('/products/<int:product_id>', method=['GET'])
def get_product_by_id(product_id):
    return jsonify({"message": "Route to show the product details"})

# Update the product
@main_bp.route("products/<int:product_id>", method=['PUT'])
def update_product(product_id):
    return jsonify({"message": "Route to update the product"})

# Delete the product
@main_bp.route("/products/<int:product_id>", method=["DELETE"])
def delete_product(product_id):
    return jsonify({"message": "Route to delete the product"})

# Upload sales
@main_bp.route("/sales/upload", method=["POST"])
def upload_sales(product_id):
    return jsonify({"message": "Route to upload sales"})

# Main route
@main_bp.route('/')
def index():
    return jsonify({"message": "Welcome to AuraShop"})