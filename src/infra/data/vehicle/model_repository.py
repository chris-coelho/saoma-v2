from src.domain.modules.vehicle_module.model_exceptions import ModelNotFoundException, ModelAlreadyExistsException
from src.domain.modules.vehicle_module.model_factory import ModelFactory
from src.infra.data.saoma_repository import SaomaRepository
from src.infra.data.vehicle.brand_repository import BrandRepository


class ModelRepository(SaomaRepository):
    def __init__(self):
        super().__init__(collection_name="models",
                         factory=ModelFactory,
                         entity_not_found_exception=ModelNotFoundException,
                         entity_already_exists_exception=ModelAlreadyExistsException)
        self.__brand_repository = BrandRepository()

    def get_models_by_brand(self, brand_id):
        return super().get_all(lambda x: x['brand_id'] == brand_id)

    def _convert_to_entity(self, json):
        if not json:
            return None

        brand = self.__brand_repository.get_by_id(json['brand_id'])

        return ModelFactory.create_from_db({'name': json['name'],
                                            'brand': brand,
                                            '_id': json['_id']})

    def _as_record(self, entity):
        return {
            '_id': entity._id,
            'name': entity.name,
            'brand_id': entity.model.brand._id,
        }
