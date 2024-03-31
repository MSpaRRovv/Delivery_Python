
class Provider:
    def __init__(self, id_p: int, name: str):
        self.id_p = id_p
        self.name = name
        self.items = {}

    def send_order(self):
        pass

    def update_stocks(self):
        pass


class Worker:
    def __init__(self, id_w: int, name: str):
        self.id_w = id_w
        self.name = name

    def get_order(self):
        pass

    def get_shift(self):
        pass


class Courier(Worker):
    pass


class Storekeeper(Worker):
    pass





class User:
    pass
