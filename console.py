#!/usr/bin/python3

'''AirBnB Clone - Command Line Interface (CLI) Module'''

import cmd
import shlex

from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    '''
    The HBNB command interpreter.

    Attributes:
        prompt (str): The custom prompt
    Methods:
        do_quit(self, line): Quit command to exit the program
        do_EOF(self): EOF command to exit the program when the user inputs EOF
        emptyline(self): An empty line + ENTER shouldn't execute anything
    '''
    class_names = {
        'BaseModel': BaseModel
    }

    prompt = '(hbnb) '

    def do_quit(self, line):
        '''Quit command to exit the program
        '''
        return True

    def do_EOF(self, line):
        '''EOF command to exit the program when the user inputs EOF (Ctrl+D)
        '''
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        '''An empty line + ENTER shouldn't execute anything
        '''
        pass

    def do_create(self, arg):
        '''Create a new instance of BaseModel, save it (to the JSON file) and
        print the id
        '''
        # Check if user didn't type anything
        if not arg:
            print('** class name missing **')
            return

        # Get the class name from the user input
        class_name = shlex.split(arg)[0]
        # Check if class_name is in the class_names dictionary
        if class_name not in self.class_names:
            print("** class doesn't exist **")
            return

        # Create a new instance of the class
        new_instance = self.class_names[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        '''Print the string representation of an instance based on the class
         name and id'''
        # Split the user input into a list of arguments
        args = shlex.split(line)

        # Check if user didn't type anything
        if not args:
            print('** class name missing **')
            return

        # Get the class name from the user input
        class_name = args[0]
        # Check if class_name is in the class_names dictionary
        if class_name not in self.class_names:
            print("** class doesn't exist **")
            return

        # Check if user didn't type the instance id
        if len(args) == 1:
            print('** instance id missing **')
            return

        # Get the instance id from the user input
        inst_id = args[1]
        # Create a key for the instance in the storage dictionary
        obj_key = '{}.{}'.format(class_name, inst_id)
        if obj_key not in storage.all():
            print('** no instance found **')
            return

        print(storage.all()[obj_key])

    def do_destroy(self, line):
        '''Delete an instance based on the class name and id (save the change
        into the JSON file)
        '''
        # Split the user input into a list of arguments
        args = shlex.split(line)

        # Check if user didn't type anything
        if not args:
            print('** class name missing **')
            return

        # Get the class name from the user input
        class_name = args[0]
        if class_name not in self.class_names:
            print("** class doesn't exist **")
            return

        # Check if user didn't type the instance id
        if len(args) == 1:
            print('** instance id missing **')
            return

        # Get the instance id from the user input
        inst_id = args[1]
        # Create a key for the instance in the storage dictionary
        obj_key = '{}.{}'.format(class_name, inst_id)
        if obj_key not in storage.all():
            print('** no instance found **')
            return

        objs = storage.all()
        del objs[obj_key]
        storage.save()

    def do_all(self, line):
        '''Print all string representation of all instances based or not on the
          class name'''
        # Split the user input into a list of arguments
        class_name = shlex.split(line)[0] if line else ''

        # Check if the user types a class name but it doesn't exist
        if class_name and class_name not in self.class_names:
            print("** class doesn't exist **")
            return

        # Create a list to store the string representation of the instances
        filtered_objs = []
        for key, obj in storage.all().items():
            # If the user didn't type a class name or the key starts with the
            # class name
            if not class_name or key.startswith(class_name + '.'):
                filtered_objs.append(obj.__str__())
        print(filtered_objs)

    def do_update(self, line):
        '''Update an instance based on the class name and id by adding or
         updating attribute (save the change into the JSON file)
        '''
        # Split the user input into a list of arguments
        args = shlex.split(line)

        # Check if user didn't type anything
        if not args:
            print('** class name missing **')
            return

        # Get the class name from the user input
        class_name = args[0]
        if class_name not in self.class_names:
            print("** class doesn't exist **")
            return

        # Check if user didn't type the instance id
        if len(args) == 1:
            print('** instance id missing **')
            return

        objs = storage.all()

        # Get the instance id from the user input
        inst_id = args[1]
        # Create a key for the instance in the storage dictionary
        obj_key = '{}.{}'.format(class_name, inst_id)
        if obj_key not in objs:
            print("** no instance found **")
            return

        # Check if user didn't type the attribute name
        if len(args) == 2:
            print('** attribute name missing **')
            return

        # Get the attribute name from the user input
        attr_name = args[2]

        # Check if user didn't type the attribute value
        if len(args) == 3:
            print('** value missing **')
            return

        # Get the attribute value from the user input
        attr_value = args[3]

        # If the user tries to update the id, created_at or updated_at
        # attributes don't do anything
        if attr_name in ['id', 'created_at', 'updated_at']:
            return

        obj = objs[obj_key]
        # Try to convert the attribute value to the same type as the attribute
        # in the instance
        try:
            attr_type = type(getattr(obj, attr_name))
            attr_value = attr_type(attr_value)
        # If an error occurs, don't do anything
        except (AttributeError, ValueError):
            pass

        # Set the attribute in the instance
        setattr(obj, attr_name, attr_value)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
