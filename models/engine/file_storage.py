#!/usr/bin/python3

'''
This module defines the FileStorage class that manages file storage for the
application
'''

import json

from models.base_model import BaseModel


class FileStorage:
    '''
    The FileStorage class that manages file storage for the application

    Attributes:
        __file_path (str): The path to the JSON file
        __objects (dict): The dictionary that will store all the objects

    Methods:
        all(self): Returns the dictionary __objects
        new(self, obj): Sets in __objects the obj with key <obj class name>.id
        save(self): Serializes __objects to the JSON file
        reload(self): Deserializes the JSON file to __objects (only if the JSON
                      file exists)
    '''
    # The path to the JSON file
    __file_path = 'file.json'
    # The dictionary that will store all the objects
    __objects = {}

    def all(self):
        '''
        Returns the dictionary __objects
        Returns:
            dict: The dictionary __objects
        '''
        return self.__objects

    def new(self, obj):
        '''
        Sets in __objects the obj with key <obj class name>.id
        Args:
            obj: The object to be added to __objects
        Returns:
            None
        '''
        if obj:
            # Create a key for the object in the format <class name>.<id>
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        '''
        Serializes __objects to the JSON file (path: __file_path)
        Returns:
            None
        '''
        # Serialize the objects
        obj_args = {key: obj.to_dict() for key, obj in self.__objects.items()}
        # Save the serialized objects to the JSON file
        with open(self.__file_path, 'w', encoding='utf8') as file:
            json.dump(obj_args, file)

    def reload(self):
        '''
        Deserializes the JSON file to __objects (only if the JSON file exists)
        Returns:
            None
        Raises:
            FileNotFoundError: If the file does not exist
        '''
        try:
            # Deserialize the JSON file
            with open(self.__file_path, 'r', encoding='utf8') as json_file:
                data = json.load(json_file)

                for key, obj_args in data.items():
                    class_name = obj_args['__class__']
                    # Create an instance of the object from the dict
                    # representation
                    self.__objects[key] = globals()[class_name](**obj_args)

        except FileNotFoundError:
            pass
