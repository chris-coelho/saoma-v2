

class ServicesCatalogExceptions(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class ServiceCategoryNotFoundException(Exception):
    def __init__(self, _id):
        if _id:
            message = "Categoria de Serviço {} não encontrada!".format(_id)
        else:
            message = "Agenda não encontrada!"
        super().__init__(message)

