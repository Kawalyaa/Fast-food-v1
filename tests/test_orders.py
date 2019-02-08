from app import creat_app
import json
import unittest


class TestMyOrders(unittest.TestCase):
    """Class for testing the orders"""
    def setUp(self):
        app = creat_app('testing')
        app.testing = True
        self.client = app.test_client()
        self.data = {
            "order": "chicken",
            "price": 7000,
            "comment": "medium spiced",
            "delivery_time": "10:32"
        }
        self.updata = {
            "order": "Chips",
            "price": 5000,
            "comment": "crispy",
            "delivery_time": "11:12"
        }
        self.incomplet = {
            "order": "Chhips",
            "price": 5000,
            "comment": "crispy",
        }

    def tearDown(self):
        self.data.clear()
        self.incomplet.clear()

    def test_posting_orders(self):
        res = self.client.post('/api/v1/orders', data=json.dumps(self.data), content_type='application/json')
        self.assertTrue(b'reated' in res.data)
        self.assertEqual(res.status_code, 201)

    def test_if_not_json(self):
        res = self.client.post('api/v1/orders', data=json.dumps(self.data), content_type='text/plain')
        self.assertTrue(b'content_type should be json' in res.data)
        self.assertEqual(res.status_code, 200)

    def test_get_all_orders(self):
        res = self.client.get('/api/v1/orders', content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_get_one_order(self):
        res = self.client.post('api/v1/orders', data=json.dumps(self.data), content_type='application/json')
        res = self.client.get('/api/v1/orders/1', content_type='application/json')
        self.assertTrue(res.json['message'], 'ok')
        self.assertEqual(res.status_code, 200)

    def test_for_get_one_index_error(self):
        res = self.client.post('/api/v1/orders', data=json.dumps(self.data), content_type='application/json')
        res = self.client.get('/api/v1/orders/5', content_type='application/json')
        self.assertTrue(b'order_id not found' in res.data)

    def test_update_order(self):
        res = self.client.post('/api/v1/orders', data=json.dumps(self.data), content_type='application/json')
        res = self.client.put('/api/v1/orders/1', data=json.dumps(self.updata), content_type='application/json')
        self.assertTrue(res.json['message'], 'Updated')
        self.assertEqual(res.status_code, 200)

    def test_for_update_index_error(self):
        res = self.client.post('/api/v1/orders', data=json.dumps(self.data), content_type='application/json')
        res = self.client.put('/api/v1/orders/11', data=json.dumps(self.updata), content_type='application/json')
        self.assertTrue(b'Order id not found, create one using the post method' in res.data)

    def test_for_delete_orders(self):
        res = self.client.post('/api/v1/orders', data=json.dumps(self.data), content_type='application/json')
        res = self.client.delete('/api/v1/orders/1', content_type='application/josn')
        self.assertTrue(b'The order with id 1 is deleted' in res.data)
        self.assertEqual(res.status_code, 200)

    def test_for_delete_index_error(self):
        res = self.client.post('api/v1/orders', data=json.dumps(self.data), content_type='application/json')
        res = self.client.delete('/api/v1/orders/4', content_type='application/json')
        self.assertTrue(b'Id not found' in res.data)
        self.assertEqual(res.status_code, 404)

    if __name__ == '__main__':
        unittest.run()
