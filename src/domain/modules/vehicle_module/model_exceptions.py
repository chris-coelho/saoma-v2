

class ModelExceptions(ValueError):
    def __init__(self, messages):
        if not isinstance(messages, list):
            messages = [messages]
        super().__init__(messages)


class ModelNotFoundException(ModelExceptions):
    def __init__(self, _id):
        if _id:
            message = "Modelo não encontrado para o Id: {}".format(_id)
        else:
            message = "Modelo não encontrado!"
        super().__init__(message)


class ModelAlreadyExistsException(ModelExceptions):
    def __init__(self, entity):
        super().__init__("Já existe moddelo: {}".format(entity))
