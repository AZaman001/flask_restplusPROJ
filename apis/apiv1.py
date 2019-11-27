"""
This is version 1 of the API, I've added the necessary docs & namespaces. 
This way we can preserve this version of the API, even as we create newer versions.
"""
from flask_restplus import Api

from namespaces.Animals import api as ns_animals
from namespaces.Employees import api as ns_employees

api = Api(
    title='Zoo API',
    version='1.0',
    description='Required operations for Zoo resources.',
)

api.add_namespace(ns_animals, path='/api/v1')
api.add_namespace(ns_employees, path='/api/v1')