from dependency_injector import containers, providers

from example_module import ExampleModuleContainer


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    example_module_container = providers.Container(ExampleModuleContainer, config=config)
