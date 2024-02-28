import logging

from flask import Blueprint, request, jsonify
from dependency_injector.wiring import inject, Provide

from app.containers import Container
from basic.api_response.api_response import ApiResponse
from basic.repository.unit_of_work import UnitOfWork
from example_module.model.example_model import ExampleModel
from example_module.service.example_service import ExampleService

bp = Blueprint('example', __name__)
logger = logging.getLogger('example')


@bp.route('/dog_list', methods=['GET'])
@inject
def route_get_dog_list(
        example_service: ExampleService = Provide[
            Container.example_module_container.example_service
        ],
):
    result = ApiResponse()

    try:
        dog_list = example_service.get_dog_list()
        result.data = dog_list

    except Exception as e:
        logger.error(str(e))
        result = ApiResponse(code=500, message=str(e))

    return jsonify(result.to_json())


@bp.route('/detail/<string:example_id>', methods=['GET'])
@inject
def route_get_detail(
        example_id: str,
        example_service: ExampleService = Provide[
            Container.example_module_container.example_service
        ],
):
    result = ApiResponse()

    try:
        detail = example_service.get_detail(
            example_id=example_id
        )
        detail.convert_names = False
        result.data = detail.model_dump()

    except Exception as e:
        logger.error(str(e))
        result = ApiResponse(code=500, message=str(e))

    return jsonify(result.to_json())


@bp.route('/upload', methods=['POST'])
@inject
def route_upload(
        example_service: ExampleService = Provide[
            Container.example_module_container.example_service
        ],
):
    result = ApiResponse()

    try:
        file = request.files['file']
        specify_name = request.form.get('specifyName', None)
        file_name = file.filename
        if specify_name:
            file_name = specify_name
        example_service.upload(
            file=file,
            file_name=file_name,
        )

    except Exception as e:
        logger.error(str(e))
        result = ApiResponse(code=500, message=str(e))

    return jsonify(result.to_json())


@bp.route('/add', methods=['POST'])
@inject
def route_add(
        uow: UnitOfWork = Provide[Container.example_module_container.unit_of_work],
        example_service: ExampleService = Provide[
            Container.example_module_container.example_service
        ],
):
    result = ApiResponse()

    try:
        params = request.get_json(silent=True)

        with uow:
            result.data = example_service.add(
                example=ExampleModel(**params)
            )
            uow.commit()

    except Exception as e:
        logger.error(str(e))
        result = ApiResponse(code=500, message=str(e))

    return jsonify(result.to_json())
