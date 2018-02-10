

class VehicleExceptions(ValueError):
    def __init__(self, messages):
        if not isinstance(messages, list):
            messages = [messages]
        super().__init__(messages)


class VehicleNotFoundException(VehicleExceptions):
    def __init__(self, _id):
        if _id:
            message = "Veículo não encontrado para o Id: {}".format(_id)
        else:
            message = "Veículo não encontrado!"
        super().__init__(message)


class VehicleAlreadyExistsException(VehicleExceptions):
    def __init__(self, entity):
        super().__init__("Já existe veículo: {}".format(entity))
