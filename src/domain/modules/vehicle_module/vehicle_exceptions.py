

class VehicleExceptions(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class VehicleNotFoundException(Exception):
    def __init__(self, _id):
        if _id:
            message = "Veículo não encontrado para o Id: {}".format(_id)
        else:
            message = "Veículo não encontrado!"
        super().__init__(message)


class VehicleAlreadyExistsException(Exception):
    def __init__(self, entity):
        super().__init__("Já existe veículo: {}".format(entity))
