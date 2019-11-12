#!/usr/bin/python3
"""Module for HBNBCommand class."""
import cmd
import json
import sys
import inspect
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
        arr_classes = inspect.getmembers(sys.modules[__name__],
                                         inspect.isclass)
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
        arr_classes = inspect.getmembers(sys.modules[__name__],
                                         inspect.isclass)
        arg_split = arg.split(' ')
        if arg_split[0] == '':
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
                    for key, value in storage.all().items():
                        if key.find(arg_split[1]) != -1:
                            print(value)
                        else:
                            print("** no instance found **")

    def do_destroy(self, arg):
        flag = 0
        arr_classes = inspect.getmembers(sys.modules[__name__],
                                         inspect.isclass)
        arg_split = arg.split(' ')
        k = {}
        if arg_split[0] == '':
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
                    for key, value in copy_destroy.items():
                        if key.find(arg_split[1]) != -1:
                            k = key
                            flag = 1
                    if flag:
                        del copy_destroy[k]
                        storage.save()

    def do_all(self, arg):
        flag = 0
        ret_obj = {}
        arr_classes = inspect.getmembers(sys.modules[__name__],
                                         inspect.isclass)

        if arg != "":
            arg_split = arg.split(' ')
            for k in arr_classes:
                if arg_split[0] in k:
                    flag = 0
                    break
                else:
                    flag = 1
            if flag == 1:
                print("** class doesn't exist **")
            else:
                result = [str(obj) for key, obj in storage.all().items()
                          if type(obj).__name__ == arg_split[0]]
                print(result)
        else:
            result = [str(obj) for key, obj in storage.all().items()]
            print(result)




def main():
    HBNBCommand().cmdloop()


main()
