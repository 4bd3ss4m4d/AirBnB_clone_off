#!/usr/bin/python3

'''
The City class represents the city where a place is located
'''

from models.base_model import BaseModel


class City(BaseModel):
    '''
    The City class represents the city where a place is located

    Attributes:
        state_id (str): The id of the state where the city is located
        name (str): The name of the city
    '''
    state_id = ''
    name = ''
