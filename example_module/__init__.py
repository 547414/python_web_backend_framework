from config import Config
from example_module.example_module_container import ExampleModuleContainer

example_module_container = ExampleModuleContainer()
example_module_container.config.from_dict(Config().model_dump())

example_module_container.wire(packages=[__name__])
