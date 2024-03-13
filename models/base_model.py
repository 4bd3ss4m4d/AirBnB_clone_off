#!/usr/bin/python3

'''
This module contains the BaseModel class
'''

from datetime import datetime
import uuid

DATE_ISO8601_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    def __init__(self, *args, **kwargs):
        '''
        Initializes a new BaseModel instance

        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments

        Returns:
            None
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                    if key in ('created_at', 'updated_at'):
                        value = datetime.strptime(value, DATE_ISO8601_FORMAT)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        '''
        Returns a string representation of the instance
        
        Returns:
            str: A string representation of the instance'''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__) 
    
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

