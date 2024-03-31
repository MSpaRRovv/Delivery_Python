class Provider:
    def __init__(self, id_p: int, name: str):
        self.id_p = id_p
        self.name = name
        self.items = {}

    def send_order(self):
        pass

    def update_stocks(self):
        pass
