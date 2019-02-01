import datetime
import time
orders_list = []


class Orders(object):
    """This class stores all our orders"""
    def __init__(self, order, comment, delivery_time):
        new_id = len(orders_list) + 1
        self.order_id = new_id
        self.order = order
        self.comment = comment
        self.deliver_time = delivery_time
        dt = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        self.date_and_time = dt
    
