#!/usr/bin/python3

'''
The Amenity class represents the amenities that a place can have
'''

from models.base_model import BaseModel


class Amenity(BaseModel):
    '''
    The Amenity class represents the amenities that a place can have

    Attributes:
        name (str): The name of the amenity
    '''
    name = ''
