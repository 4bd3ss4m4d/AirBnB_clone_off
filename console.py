#!/usr/bin/python3

'''AirBnB Clone - Command Line Interface (CLI) Module'''

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
