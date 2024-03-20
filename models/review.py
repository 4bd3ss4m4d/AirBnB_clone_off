#!/usr/bin/python3

'''
The Review class represents the review of a place
'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''
    The Review class represents the review of a place

    Attributes:
        place_id (str): The id of the place that the review is for
        user_id (str): The id of the user who wrote the review
        text (str): The text of the review
    '''
    place_id = ''
    user_id = ''
    text = ''
