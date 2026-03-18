from flask import Blueprint, jsonify

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():
    return jsonify({"message": "Welcome to AuraShop"})

@main_bp.route('/products')
def products():
    return jsonify({"message": "View Products:"})

@main_bp.route('/login', methods=['POST'])
def login():
    return jsonify({"message": "Login"})