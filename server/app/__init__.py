# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.record_controller import api as record_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(record_ns, path='/record')