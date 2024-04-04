from abc import ABC, abstractmethod
from Store import Store
import uuid
from datetime import datetime, timedelta


class Worker(ABC):
    def __init__(self, name, job_place):
        self.__name = name
        self.__job_place = job_place
        self.__id_w = str(uuid.uuid4())

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
    def __init__(self,  name, job_place):
        super().__init__(name, job_place)

    def get_order(self):
        pass

    def get_shift(self):
        pass


class Storekeeper(Worker):
    def __init__(self, name, job_place):
        super().__init__(name, job_place)

    def get_order(self, order, store):
       print("")

    def get_shift(self):
        shift_hours = int(input("Введите количество часов: "))
        shift_duration = timedelta(hours=shift_hours)
        current_time = datetime.now()
        end_of_shift = current_time + shift_duration
        return end_of_shift, current_time
