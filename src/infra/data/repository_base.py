from abc import ABCMeta, abstractmethod


class RepositoryBase(metaclass=ABCMeta):

    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, entity):
        pass

    @abstractmethod
    def get_by_id(self, _id):
        pass

    @abstractmethod
    def search(self, query):
        pass
