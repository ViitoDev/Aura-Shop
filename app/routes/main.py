from flask import Blueprint, jsonify, request, current_app
from app.models.user import LoginPayload
from pydantic import ValidationError
from bson import ObjectId
from app.models.products import *
from app.decorators import token_required
from datetime import datetime, timedelta, timezone
import jwt

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
        return jsonify({"error": "Requisition error"}), 500

    if user_data.username == 'admin' and user_data.password == 'tricas':
        token = jwt.encode(
            {
                "user_id":user_data.username,
                "exp": datetime.now(timezone.utc) + timedelta(minutes=30)   
            },
            current_app.config['SECRET_KEY'],
            algorithm='HS256'
        )
        return jsonify({'acess_token': token}), 200
    return jsonify({"message" : "Invalid login"})


# Show the products
@main_bp.route('/products', methods=['GET'])
def products():
    products_cursor = current_app.db.products.find({})
    products_list = [ProductDBModel(**product).model_dump(by_alias=True, exclude_none=True) for product in products_cursor]
    return jsonify(products_list)


# Add products
@token_required
@main_bp.route('/products', methods=['POST'])
def create_product(token):
    try:
        product = Product(**request.get_json())
    except ValidationError as e:
        return jsonify({"message": f"Error {e}"})
    
    result = db.products.insert_one(product.model_dump())

    return jsonify({"message": "Route to add products", "id": str(result.inserted_id)}), 201


# Show a single product
@main_bp.route('/products/<string:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    try:
        oid = ObjectId(product_id)

    except Exception as e:
        return jsonify({"error": f"Error to find the product {product_id}: {e}"})
    
    product = current_app.db.products.find_one({'_id':oid})

    if product:
        products_model = ProductDBModel(**product).model_dump(by_alias=True, exclude_none=True)
        return jsonify(products_model)
    else:
        return jsonify({"error": "Error: Product not find"})
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