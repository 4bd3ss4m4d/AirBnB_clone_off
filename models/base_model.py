#!/usr/bin/python3

'''
This module contains the BaseModel class
'''

from datetime import datetime
import uuid

class BaseModel:
    def __init__(self):
        '''
        Initializes a new instance of BaseModel
        
        Attributes:
            id (str): A unique identifier for the instance
            created_at (datetime): The date and time the instance was created
            updated_at (datetime): The date and time the instance was last updated
            
        Methods:
            save: Updates the updated_at attribute with the current date and time
            to_dict: Returns a dictionary representation of the instance

        Returns:
            None
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        '''
        Returns a string representation of the instance
        
        Returns:
            str: A string representation of the instance'''
        return f'[{self.__class__.__name__}] (<{self.id}>) <{self.__dict__}>'
    
    def save(self):
        '''
        Updates the updated_at attribute with the current date and time
        
        Returns:
            None
        '''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''
        Returns a dictionary representation of the instance
        
        Returns:
            dict: A dictionary representation of the instance
        '''
        instance_data = self.__dict__.copy()

        instance_data['created_at'] = self.created_at.isoformat()
        instance_data['updated_at'] = self.updated_at.isoformat()

        instance_data['__class__'] = self.__class__.__name__

        return instance_data


