#!/usr/bin/python3

'''
The User class defines the attributes and methods for the User object
'''

from models.base_model import BaseModel


class User(BaseModel):
    '''
    The User class defines the attributes and methods for the User object

    Attributes:
        email (str): The user's email address
        password (str): The user's password
        first_name (str): The user's first name
        last_name (str): The user's last name
    '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
