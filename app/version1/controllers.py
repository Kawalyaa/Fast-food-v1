from flask import request, jsonify

from app.version1.models import Orders, orders_list


def creat_orders():
    req = request.get_json()
    try:
        data = {
            'order': req['order'],
            'comment': req['comment'],
            'price': req['price'],
            'delivery_time': req['delivery_time']

        }

        new_order = Orders(
            data['order'],
            data['comment'],
            data['price'],
            data['delivery_time']
        )
        orders_list.append(new_order.__dict__)
        return jsonify({
            "message": "Created",
            "order": new_order.__dict__
        })
    except ValueError:
        return jsonify({"message": "content should be json"})


def get_all():
    return jsonify({'orders_list': orders_list})


def get_one(order_id):
    for order in orders_list:
        if order['order_id'] == order_id:
            return jsonify({
                "order": order
            })
    return jsonify({
        "message": "order_id not found"

    })


def edit_order(order_id):
    for order in orders_list:
        if order['order_id'] == order_id:
            req = request.get_json()
            order['order'] = req['order']
            order["comment"] = req['comment']
            order['price'] = req['price']
            order['delivery_time'] = req['delivery_time']
            return jsonify({
                "message": "Updated",
                "order": order
            })
    return jsonify({
        "message": "Order id not found, create one using the post method"
    })


def delete_one(order_id):
    deleted = [order for order in orders_list if order['order_id'] == order_id]
    if len(deleted) == 0:
        return jsonify({"message": "Id not found"})
    orders_list.remove(deleted[0])
    return jsonify({
        "delete_order": "The order with id {} is deleted".format(deleted[0]['order_id'])
    })
