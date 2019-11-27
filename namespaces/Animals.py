"""
Module to handle all Animal related operations at the Zoo. 
"""

from flask_restplus import Resource, Api, Namespace, abort, reqparse
from data.models import animal as animal_model
from data.content import ANIMALS

api = Namespace('animals', description= 'Operations for Animal managment.')
api.models[animal_model.name] = animal_model


@api.route('/animals')
class Animals(Resource):

    @api.marshal_with(animal_model)
    def get(self):
        """
         This will return all the animals registered at the zoo. 

         :return: list of all animals at zoo
        """
        return ANIMALS
    
    @api.expect(animal_model, validate = True)
    @api.doc(responses={201: 'Created Successfully'})
    def post(self):
        """
        Allows you to add animal to the list

        :return: the added animal
        """
        data = api.payload
        ANIMALS.append(data)
        return data

@api.route('/animals/<string:name>')
class Animal(Resource):
    
  
    @api.doc(responses={400: 'Bad Request'})
    @api.marshal_list_with(animal_model)
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


    @api.expect(animal_model, validate = True)
    @api.doc(responses={400: 'Bad Request'})
    def put(self, name):
        """
        This will give you the ability to update the count for specific animal

        :return: the updated animal
        """

        for animal in ANIMALS:
            if animal['name'] == name:
                animal.update(api.payload)
                return animal, 200
        abort(400, 'This animal cannot be found on the zoo list.', custom='400 BAD REQUEST') 


    @api.doc(responses={202: 'Accepted'})
    @api.doc(responses={400: 'Bad Request'})
    @api.marshal_with(animal_model)
    def delete(self,name):
        """
        This will remove the specified animal from the zoo list.

        :return: 202 upon deletion, 404 upon error
        """

        for animal in ANIMALS:
            if animal['name'] == name:
                ANIMALS.remove(animal)
                return animal, 202
        abort(400, 'This animal cannot be found on the zoo list.', custom='400 BAD REQUEST')
