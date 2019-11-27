"""
 Module to handle all the operations required for Employee Management at the zoo 
"""

from flask_restplus import Resource, Api, Namespace
from data.models import employee
from data.content import EMPLOYEES

api = Namespace('employees', description= 'Operations for Employee managment.')
api.models[employee.name] = employee

@api.route('/employees')
class Employees(Resource):
    
    @api.marshal_list_with(employee)
    def get(self):
        """
        :return list of employees working at zoo
        """
        return EMPLOYEES

