from src.domain.modules.customer_module.customer import Customer
from src.domain.modules.customer_module.customer_exceptions import CustomerExceptions
from src.domain.modules.factory_base import FactoryBase
from src.infra.crosscutting.common.doc_id_util import DocIdUtil
from src.infra.crosscutting.common.email_util import EmailUtil


class CustomerFactory(FactoryBase):

    @staticmethod
    def create(doc_id, name, email, _id=None):
        customer = Customer(doc_id=doc_id,
                            name=name,
                            email=email,
                            _id=_id)

        return customer if CustomerFactory.validate(customer) else None

    @staticmethod
    def create_from_db(entity_as_dict):
        return CustomerFactory.create(entity_as_dict['doc_id'],
                                      entity_as_dict['name'],
                                      entity_as_dict['email'],
                                      entity_as_dict['_id'])

    @staticmethod
    def validate(entity):
        messages = []
        if not entity.doc_id:
            messages.append("CPF obrigatório.")
        if not entity.name:
            messages.append("Nome obrigatório.")
        if not entity.email:
            messages.append("Email obrigatório.")

        if entity.name and len(entity.name) < 6:
            messages.append("Nome {} - muito curto.".format(entity.name))

        if not DocIdUtil.validate_cpf(entity.doc_id):
            messages.append("CPF {} inválido.".format(entity.doc_id))

        if not EmailUtil.is_valid(entity.email):
            messages.append("E-mail {} inválido.".format(entity.email))

        if len(messages) == 0:
            return True
        else:
            raise CustomerExceptions(messages)

