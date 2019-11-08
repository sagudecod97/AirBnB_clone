#!/usr/bin/python3
"""Module for HBNBCommand class."""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class."""
    prompt = '(hbnb) '

    # ------ basic commands ------
    def do_EOF(self, arg):
        """Handles EOF\n"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """anything when type ENTER"""
    pass

    # ------ Instance commands ------

    def do_create(self, arg):
        arg_split = arg.split(' ')
        if (arg_split[0] == ''):
            print("** class name missing **")
        else:
            try:
                instance = eval(arg_split[0] + "()")
                print((instance.__dict__)["id"])
                instance.save()
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, arg):
        arg_split = arg.split(' ')
        if (arg_split[0] == ''):
            print("** class name missing **")
        else:
            try:
                #with open(FileStorage.__path_file

def main():
    HBNBCommand().cmdloop()


main()
