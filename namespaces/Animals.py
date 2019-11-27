"""
Module to handle all Animal related operations at the Zoo. 
"""

from flask_restplus import Resource, Api, Namespace, abort, reqparse
from data.models import animal
from data.content import ANIMALS

api = Namespace('animals', description= 'Operations for Animal managment.')
api.models[animal.name] = animal

@api.route('/animals')
class Animals(Resource):

    @api.marshal_list_with(animal)
    def get(self):
        """
         This will return all the animals registered at the zoo. 

         :return: list of all animals at zoo
        """
        return ANIMALS
 

@api.route('/animals/<string:name>')
class Animal(Resource):
    
    @api.marshal_list_with(animal)
    @api.doc(responses={400: 'Bad Request'})
    def get(self, name):
        """
         This will return the number of specified Animal that is registered with the zoo. 

         :param animal  type of animal to find
         :return:       number of that type of animal
        """
        for animal in ANIMALS:
            if animal['name'] == name:
                return animal
        abort(400, 'This animal cannot be found on the zoo list.', custom='400 BAD REQUEST')

    @api.expect(animal)
    def put(self, name):
        """
        This will give you the ability to update the count for specific animal
        """