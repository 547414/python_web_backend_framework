import os
import importlib

from basic import BaseEntity
import example_module.entity as entity_module
from example_module import example_module_container

if __name__ == '__main__':
    entity_module_path = os.path.dirname(entity_module.__file__)

    for filename in os.listdir(entity_module_path):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = f'example_module.entity.{filename[:-3]}'
            importlib.import_module(module_name)

    # 创建表
    BaseEntity.metadata.create_all(example_module_container.engine())
