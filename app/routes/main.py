from flask import Blueprint, jsonify, request
from app.models.user import LoginPayload
from pydantic import ValidationError


main_bp = Blueprint('main_bp', __name__)

# User auth
@main_bp.route('/login', methods=['POST'])
def login():
    try:
        raw_data = request.get_json()
        user_data = LoginPayload(**raw_data)

    except ValidationError as e:
        return jsonify({"Error": e.errors()}), 400
    
    except Exception as e:
        jsonify({"error": "Requisition error"}), 500

    if user_data.username == 'admin' and user_data.password == '123':
        return jsonify({"message" : "Sucessfuly login!"})

    else:
        return jsonify({"message" : "Invalid login"})

# Show the products
@main_bp.route('/products', methods=['GET'])
def products():
    return jsonify({"message": "View Products:"})

# Add products
@main_bp.route('/products', methods=['POST'])
def create_product():
    return jsonify({"message": "Route to add products"})

# Show product details
@main_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    return jsonify({"message": "Route to show the product details"})

# Update the product
@main_bp.route("/products/<int:product_id>", methods=['PUT'])
def update_product(product_id):
    return jsonify({"message": "Route to update the product"})

# Delete the product
@main_bp.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    return jsonify({"message": "Route to delete the product"})

# Upload sales
@main_bp.route("/sales/upload", methods=["POST"])
def upload_sales(product_id):
    return jsonify({"message": "Route to upload sales"})

# Main route
@main_bp.route('/')
def index():
    return jsonify({"message": "Welcome to AuraShop"})