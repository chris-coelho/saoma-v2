from src.domain.modules.vehicle_module.brand_exceptions import BrandNotFoundException, BrandAlreadyExistsException
from src.domain.modules.vehicle_module.brand_factory import BrandFactory
from src.infra.data.saoma_repository import SaomaRepository


class BrandRepository(SaomaRepository):

    def __init__(self):
        super().__init__(collection_name="brands",
                         factory=BrandFactory,
                         entity_not_found_exception=BrandNotFoundException,
                         entity_already_exists_exception=BrandAlreadyExistsException)
