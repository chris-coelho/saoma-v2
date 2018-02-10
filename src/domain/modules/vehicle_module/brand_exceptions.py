

class BrandExceptions(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class BrandNotFoundException(Exception):
    def __init__(self, _id):
        if _id:
            message = "Marca não encontrada para o Id: {}".format(_id)
        else:
            message = "Marca não encontrada!"
        super().__init__(message)


class BrandAlreadyExistsException(Exception):
    def __init__(self, entity):
        super().__init__("Já existe marca: {}".format(entity))
