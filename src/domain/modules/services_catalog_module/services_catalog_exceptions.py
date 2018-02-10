

class ServicesCatalogExceptions(ValueError):
    def __init__(self, messages):
        if not isinstance(messages, list):
            messages = [messages]
        super().__init__(messages)


class ServiceCategoryNotFoundException(ServicesCatalogExceptions):
    def __init__(self, _id):
        if _id:
            message = "Categoria de Serviço {} não encontrada!".format(_id)
        else:
            message = "Agenda não encontrada!"
        super().__init__(message)

