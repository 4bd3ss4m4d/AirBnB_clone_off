#!/usr/bin/python3

'''
This module initializes the FileStorage instance and loads any existing data
from the JSON file to populate the __objects dictionary
'''

from models.engine.file_storage import FileStorage


# Create a central FileStorage instance for data persistence
storage = FileStorage()

# Load any existing data from the JSON file to populate the __objects dict
storage.reload()
