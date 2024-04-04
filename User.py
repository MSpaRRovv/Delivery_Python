from Order import Order
from datetime import datetime
import uuid
class User:

    def __init__(self):
        self.__username = input("Введите имя пользователя: ")
        self.__user_id = str(uuid.uuid4())
        self.__x = input("Введите координаты X: ")
        self.__y = input("Введите координаты Y: ")
        self.__coordinates = (self.__x, self.__y)



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


    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def make_order(self):
        item: str = input('Введите товар, который хотите заказать: ')
        count = int(input('Введите количество товара, который хотите заказать: '))
        order_id = int(uuid.uuid4())
        status = "created"
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_order = Order(order_id, status, [(item, count)], created_at, "", "", "")
        return new_order
        print(f"Статус заказа: {order.status}")

    def take_order_user(self):
        pass