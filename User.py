from Order import Order
from datetime import datetime
import uuid
class User:
    def __init__(self, username, user_id, coordinates):
        self.__username = username
        self.__user_id = user_id
        self.__coordinates = coordinates

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_coordinates(self):
        return self.__coordinates

    def set_coordinates(self, coordinates):
        self.__coordinates = coordinates
    def make_order(self):
        item = input('Введите товар, который хотите заказать: ')
        count = int(input('Введите количество товара, который хотите заказать: '))
        order_id = int(uuid.uuid4())
        status = "created"
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_order = Order(order_id, status, [(item, count)], created_at, "", "", "")
        return new_order
        print(f"Статус заказа: {order.status}")

    def take_order_user(self):
        pass