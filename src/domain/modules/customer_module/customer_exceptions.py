

class CustomerExceptions(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class CustomerNotFoundException(Exception):
    def __init__(self, id):
        if id:
            message = "Cliente {} não encontrado!".format(id)
        else:
            message = "Cliente não encontrado!"
        super().__init__(message)


class CustomerAlreadyExistsException(Exception):
    def __init__(self, entity):
        super().__init__("Já existe cliente {}".format(entity))
