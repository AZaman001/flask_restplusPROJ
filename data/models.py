"""
Models for various data content I will use in the API
"""

from flask_restplus import fields, Model

animal = Model('Animal', {
    'name': fields.String(required=True, description='The name of the animal'),
    'quantity': fields.Integer(required=True, description='The quantify of this type of animal at the zoo')
})

employee = Model('Employee', {
    'f_name': fields.String(required=True, description='The first name of the employee'),
    'l_name': fields.String(required=True, description='The last name of the employee'),
    'email': fields.String(required=True, description='The email of the employee')
})
