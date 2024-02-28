from sqlalchemy.orm import Session

from basic.repository.base_repository import BaseRepository
from example_module.entity.example import ExampleEntity
from example_module.model.example_model import ExampleModel, ExampleCategoryEnum


class ExampleRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session)

    def get_dog_list(self):
        return self.get_all_by_params(
            entity=ExampleEntity,
            model=ExampleModel,
            params={
                "category": ExampleCategoryEnum.DOG.name
            }
        )

    def get_detail(self, example_id: str):
        sql = """
        SELECT * FROM ct_example WHERE id = :example_id
        """
        return self.get_by_params(
            model=ExampleModel,
            sql=sql,
            params={
                "example_id": example_id
            }
        )
