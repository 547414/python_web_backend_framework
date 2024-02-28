from basic.minio_client.minio_clent import MinioClient
from example_module.entity.example import ExampleEntity
from example_module.model.example_model import ExampleModel, ExampleCategoryEnum
from example_module.repository.example_repository import ExampleRepository


class ExampleService:
    def __init__(
            self,
            example_repository: ExampleRepository,
            minio_client: MinioClient
    ):
        self.__example_repository = example_repository
        self.__minio_client = minio_client

    def get_dog_list(self):
        data_list = self.__example_repository.get_dog_list()
        res_list = []
        for data in data_list:
            data.category = ExampleCategoryEnum[data.category].value
            res_list.append(data.model_dump())
        return res_list

    def get_detail(self, example_id: str):
        data = self.__example_repository.get_detail(
            example_id=example_id
        )
        data.category = ExampleCategoryEnum[data.category].value
        return data

    def upload(self, file, file_name: str):
        return self.__minio_client.put_object(
            file_name=file_name,
            data=file,
        )

    def add(self, example: ExampleModel):
        return self.__example_repository.add(
            model=example,
            entity=ExampleEntity,
        )
