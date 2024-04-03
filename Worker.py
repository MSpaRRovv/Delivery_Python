from abc import ABC, abstractmethod
import uuid

class Worker(ABC):
    def __init__(self, name):
        self.__id_w = str(uuid.uuid4())
        self.__name = name

    def get_worker_id(self):
        return self.__id_w

    def set_worker_id(self, id_w):
        self.__id_w = id_w

    def get_worker_name(self):
        return self.__name

    def set_worker_name(self, name):
        self.__name = name

    @abstractmethod
    def get_order(self):
        pass

    @abstractmethod
    def get_shift(self):
        pass


class Courier(Worker):
    def __init__(self, worker_id, name):
        super().__init__(worker_id, name)

    def get_order(self):
        pass

    def get_shift(self):
        pass


class Storekeeper(Worker):
    def __init__(self, worker_id, name):
        super().__init__(worker_id, name)

    def get_order(self):
        pass

    def get_shift(self):
        pass
