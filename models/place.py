#!/usr/bin/python3

'''
The Place class represents the place where a user can stay
'''

from models.base_model import BaseModel


class Place(BaseModel):
    '''
    The Place class represents the place where a user can stay

    Attributes:
        city_id (str): The id of the city where the place is located
        user_id (str): The id of the user who owns the place
        name (str): The name of the place
        description (str): The description of the place
        number_rooms (int): The number of rooms in the place
        number_bathrooms (int): The number of bathrooms in the place
        max_guest (int): The max number of guests that can stay in the place
        price_by_night (int): The price per night to stay in the place
        latitude (float): The latitude of the place
        longitude (float): The longitude of the place
        amenity_ids (list of str): The ids of the amenities that the place has
    '''
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
