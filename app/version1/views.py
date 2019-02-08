from flask import Blueprint
from app.version1.controllers import creat_orders, get_all, get_one, edit_order, delete_one


food_app = Blueprint('food_app', __name__)


@food_app.route('/orders', methods=['POST'])
def creat_new():
        create = creat_orders()
        return create


@food_app.route('/orders', methods=['GET'])
def get_all_orders():
    all_orders = get_all()
    return all_orders


@food_app.route('/orders/<int:order_id>', methods=['GET'])
def get_single_order(order_id):
    one_order = get_one(order_id)
    return one_order


@food_app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    updater = edit_order(order_id)
    return updater


@food_app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    deleter = delete_one(order_id)
    return deleter
