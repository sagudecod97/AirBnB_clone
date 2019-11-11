#!/usr/bin/python3
"""Module for HBNBCommand class."""
import cmd
import json
import sys, inspect
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
        arr_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        arg_split = arg.split(' ')
        if (arg_split[0] == ''):
            print("** class name missing **")
        else:
            for k in arr_classes:
                if arg_split[0] in k:
                    instance = eval(arg_split[0] + "()")
                    print((instance.__dict__)["id"])
                    instance.save()
                    flag = 0
                    break
                else:
                    flag = 1
            if flag:
                print("** class doesn't exist **")

    def do_show(self, arg):
        flag = 0
        arr_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        arg_split = arg.split(' ')
        if (arg_split[0] == ''):
            print("** class name missing **")
        else:
            for k in arr_classes:
                if arg_split[0] in k:
                    flag = 0
                    break
                else:
                    flag = 1
            if flag:
                print("** class doesn't exist **")
            elif flag == 0 and len(arg_split) == 1:
                print("** instance id missing **")

            if len(arg_split) > 1:
                for item in storage.all():
                    if arg_split[1] in item:
                        flag = 0
                        break
                    else:
                        flag = 1
                if flag:
                    print("** no instance found **")
                else:
                    for key,value in storage.all().items():
                        if arg_split[1] in key:
                            print(value)

    def do_destroy(self, arg):
        flag = 0
        arr_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        arg_split = arg.split(' ')
        if (arg_split[0] == ''):
            print("** class name missing **")
        else:
            for k in arr_classes:
                if arg_split[0] in k:
                    flag = 0
                    break
                else:
                    flag = 1
            if flag:
                print("** class doesn't exist **")
            elif flag == 0 and len(arg_split) == 1:
                print("** instance id missing **")

            if len(arg_split) > 1:
                for item in storage.all():
                    if arg_split[1] in item:
                        flag = 0
                        break
                    else:
                        flag = 1
                if flag:
                    print("** no instance found **")
                else:
                    copy_destroy = storage.all()
                    flag = 0
                    for key,value in copy_destroy.items():
                        if arg_split[1] in key:
                            flag = 1
                    if flag:
                        del copy_destroy[key]



def main():
    HBNBCommand().cmdloop()


main()
