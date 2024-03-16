#!/usr/bin/python3

'''
Thee BaseModel class that defines the common attributes and methods for all
other classes
'''

from datetime import datetime
import uuid

DATE_ISO8601_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    '''
    The BaseModel class that defines the common attributes and methods for all
    other classes
    Attributes:
        id (str): The unique identifier for the instance
        created_at (datetime): The date and time the instance was created
        updated_at (datetime): The date and time the instance was last updated
    Methods:
        __init__(self, *args, **kwargs): Initializes a new BaseModel instance
        __str__(self): Returns a string representation of the instance
        save(self): Calls the FileStorage instance to serialize and persist the
                    object to the JSON file
        to_dict(self): Returns a dictionary representation of the instance
    '''
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
            # If the instance is being created from a dictionary representation
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                    if key in ('created_at', 'updated_at'):
                        value = datetime.strptime(value, DATE_ISO8601_FORMAT)
                    setattr(self, key, value)
        else:
            # If the instance is being created from scratch
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

            # Store the new instance in the storage
            from models import storage
            storage.new(self)

    def __str__(self):
        '''
        Returns a string representation of the instance
        Returns:
            str: A string representation of the instance'''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        '''
        Calls the FileStorage instance to serialize and persist the object to
        the JSON file.
        '''
        self.updated_at = datetime.now()

        # Serialize the object and save it to the JSON file
        from models import storage
        storage.save()

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
