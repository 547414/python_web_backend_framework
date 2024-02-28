from dependency_injector import containers, providers
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from basic.minio_client.minio_clent import MinioClient
from basic.repository.unit_of_work import UnitOfWork
from example_module.repository.example_repository import ExampleRepository
from example_module.service.example_service import ExampleService


class ExampleModuleContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    # https://python-dependency-injector.ets-labs.org/examples/fastapi-sqlalchemy.html
    engine = providers.Singleton(create_engine, url=config.SQLALCHEMY_DATABASE_URI)
    Session = providers.ThreadLocalSingleton(sessionmaker, bind=engine)
    session = providers.Singleton(scoped_session, Session)

    # Minio 客户端配置
    minio_client = providers.Singleton(
        MinioClient,
        config=config
    )

    # 配置 UnitOfWork
    unit_of_work = providers.Factory(UnitOfWork, session_factory=session)

    example_repository = providers.Factory(
        ExampleRepository,
        session=session,
    )

    example_service = providers.Factory(
        ExampleService,
        example_repository=example_repository,
        minio_client=minio_client,
    )
