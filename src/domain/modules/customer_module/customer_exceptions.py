

class CustomerExceptions(ValueError):
    def __init__(self, messages):
        if not isinstance(messages, list):
            messages = [messages]
        super().__init__(messages)


class CustomerNotFoundException(CustomerExceptions):
    def __init__(self, id):
        if id:
            message = "Cliente {} não encontrado!".format(id)
        else:
            message = "Cliente não encontrado!"
        super().__init__(message)


class CustomerAlreadyExistsException(CustomerExceptions):
    def __init__(self, entity):
        super().__init__("Já existe cliente {}".format(entity))
