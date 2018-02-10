from src.domain.modules.customer_module.customer_exceptions \
    import CustomerNotFoundException, CustomerAlreadyExistsException
from src.domain.modules.customer_module.customer_factory import CustomerFactory
from src.infra.data.saoma_repository import SaomaRepository


class CustomerRepository(SaomaRepository):
    def __init__(self):
        super().__init__(collection_name="customers",
                         factory=CustomerFactory,
                         entity_not_found_exception=CustomerNotFoundException,
                         entity_already_exists_exception=CustomerAlreadyExistsException)

    def get_by_doc_id(self, doc_id):
        customer = super().get_all(lambda x: x['doc_id'] == doc_id)
        if not customer:
            raise CustomerNotFoundException(doc_id)
        return customer[0]

    def get_by_name(self, name):
        return super().get_all(lambda x: x['name'].upper().find(name.upper()) >= 0)
