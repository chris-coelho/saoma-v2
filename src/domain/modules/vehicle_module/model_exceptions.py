

class ModelExceptions(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class ModelNotFoundException(Exception):
    def __init__(self, _id):
        if _id:
            message = "Modelo não encontrado para o Id: {}".format(_id)
        else:
            message = "Modelo não encontrado!"
        super().__init__(message)


class ModelAlreadyExistsException(Exception):
    def __init__(self, entity):
        super().__init__("Já existe moddelo: {}".format(entity))
