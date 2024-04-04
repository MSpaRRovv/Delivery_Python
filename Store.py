from Order import Order

import uuid


class Store:
    def __init__(self, name):
        self.__id_s = str(uuid.uuid4())
        self.__name = name
        self.__x = input("Введите координаты магазина X: ")
        self.__y = input("Введите координаты магазина Y: ")
        self.__coordinates = (self.__x, self.__y)
        self.__items_store = {}

    def get_id_s(self):
        return self.__id_s

    def set_id_s(self, id_s):
        self.__id_s = id_s

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_coordinates(self):
        return self.__coordinates

    def set_coordinates(self, coordinates):
        self.__coordinates = coordinates

    def get_items_store(self):
        return self.__items_store

    def set_items_store(self, items_store):
        self.__items_store = items_store

    def get_x_store(self):
        return self.__x

    def set_x_store(self, x):
        self.__x = x

    def get_y_store(self):
        return self.__y

    def set_y_store(self, y):
        self.__y = y

    def add_item(self, item, count):
        self.__items_store[item] = count

    def send_request(self, item, provider, count):
        if item not in self.__items_store:
            print(f"Запрашиваем товар {item.name} у поставщика в кол-ве {count}")
            provider.send_order(item, count)

    def take_order(self, order):
        order.status = "processing"
        print(f"Статус заказа: {order.status}")




    def set_storekeeper(self,order):
        pass



    def set_courier(self):
        pass

    def get_worker(self):
        pass
