

class ScheduleExceptions(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class ScheduleNotFoundException(Exception):
    def __init__(self, _id):
        if _id:
            message = "Agenda não encontrada para o Id: {}".format(_id)
        else:
            message = "Agenda não encontrada!"
        super().__init__(message)


class ScheduleAlreadyExistsException(Exception):
    def __init__(self, entity):
        super().__init__("Já existe agenda: {}".format(entity))
