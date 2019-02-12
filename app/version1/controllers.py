from flask import request, jsonify

from app.version1.models import Orders, orders_list


# def check(new_order):
#    """This faction validates the new order input"""
#        # keys should have values
#        if not value:
#            return "{} is is empty. The value is required".format(key)
#        if key == "order" or key == "comment":
#            if len(value) < 3 or value == int:
#                return "The value provided on {} is too short or ValueError".format(key)
#        if key == "price" or key == "delivery_time":
#            if value == str:
#                return "On the {} value should be an integer".format(key)

#        if key == "delivery_time":
#            if value == int:
#                return "On the {} value should be a string".format(key)


def creat_orders():
    req = request.get_json()
    try:
        data = {
            "order": req['order'],
            "price": req['price'],
            "comment": req['comment'],
            "delivery_time": req['delivery_time']
        }

        new_order = Orders(data['order'], data['price'], data['comment'], data['delivery_time'])

        orders_list.append(new_order.__dict__)
        return jsonify({
            "message": "Created",
            "order": new_order.__dict__
        }), 201
    except TypeError:
                return jsonify({"message": "content_type should be json"})


def get_all():
    return jsonify({'orders_list': orders_list}), 200


def get_one(order_id):
        one_order = [order for order in orders_list if order['order_id'] == order_id]
        if len(one_order) == 0:
            return jsonify({
                "message": "order_id not found"

            })
        return jsonify({
            "message": "ok",
            "order": one_order[0]
        }), 200


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
                }), 200
        return jsonify({
            "message": "Order id not found, create one using the post method"
        })


def delete_one(order_id):
    try:
        deleted = [order for order in orders_list if order['order_id'] == order_id]
        # if len(deleted) == 0:
        #    return jsonify({"message": "Id not found"}), 404
        orders_list.remove(deleted[0])
        return jsonify({
            "message": "ok",
            "delete_order": "The order with id {} is deleted".format(deleted[0]['order_id'])
        }), 200
    except IndexError:
            return jsonify({"message": "Id not found"}), 404
