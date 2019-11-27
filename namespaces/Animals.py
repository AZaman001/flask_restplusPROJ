"""
Module to handle all Animal related operations at the Zoo. 
"""

from flask_restplus import Resource, Api, Namespace, abort, reqparse
from data.models import animal
#from data.content import ANIMALS

api = Namespace('animals', description= 'Operations for Animal managment.')
api.models[animal.name] = animal


class AnimalsDAO(object):
    def __init__(self):
        self.ANIMALS = []

    def get(self, name):
        for animal in self.ANIMALS:
            if animal['name'] == name:
                return animal
        abort(400, 'This animal cannot be found on the zoo list.', custom='400 BAD REQUEST')

    def create(self, data):
        animal = data
        self.ANIMALS.append(animal)
        return animal

    def update(self, name, data):
        animal = self.get(name)
        animal.update(data)
        return animal

    def delete(self, name):
        animal = self.get(name)
        self.ANIMALS.remove(animal)

DAO = AnimalsDAO()
DAO.create({
                "name" : "monkey",
                "quantity": 4
           })
DAO.create({
                "name" : "elphant",
                "quantity": 2
           })

@api.route('/animals')
class AnimalList(Resource):

    @api.marshal_list_with(animal)
    def get(self):
        """
         This will return all the animals registered at the zoo. 

         :return: list of all animals at zoo
        """
        return DAO.ANIMALS
    
    @api.marshal_list_with(animal, code=201)
    @api.doc(responses={201: 'Created Successfully'})
    def post(self):
        """
        Allows you to add animal to the list

        :return: the added animal
        """

        return DAO.create(api.payload), 201

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
        
        return DAO.get(name)

    @api.expect(animal)
    @api.doc(responses={200: 'OK'})
    def put(self, name):
        """
        This will give you the ability to update the count for specific animal

        :return: the updated animal
        """

        return DAO.update(name, api.payload)