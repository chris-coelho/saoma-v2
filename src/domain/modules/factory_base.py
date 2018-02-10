from abc import ABCMeta, abstractmethod


class FactoryBase(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def create_from_db(record):
        pass

    @staticmethod
    @abstractmethod
    def validate(entity):
        pass
