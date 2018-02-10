

class BrandExceptions(ValueError):
    def __init__(self, messages):
        if not isinstance(messages, list):
            messages = [messages]
        super().__init__(messages)


class BrandNotFoundException(BrandExceptions):
    def __init__(self, _id):
        if _id:
            message = "Marca não encontrada para o Id: {}".format(_id)
        else:
            message = "Marca não encontrada!"
        super().__init__(message)


class BrandAlreadyExistsException(BrandExceptions):
    def __init__(self, entity):
        super().__init__("Já existe marca: {}".format(entity))
