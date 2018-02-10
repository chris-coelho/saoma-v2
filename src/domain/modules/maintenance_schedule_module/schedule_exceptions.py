

class ScheduleExceptions(ValueError):
    def __init__(self, messages):
        if not isinstance(messages, list):
            messages = [messages]
        super().__init__(messages)


class ScheduleNotFoundException(ScheduleExceptions):
    def __init__(self, _id):
        if _id:
            message = "Agenda não encontrada para o Id: {}".format(_id)
        else:
            message = "Agenda não encontrada!"
        super().__init__(message)


class ScheduleAlreadyExistsException(ScheduleExceptions):
    def __init__(self, entity):
        super().__init__("Já existe agenda: {}".format(entity))
