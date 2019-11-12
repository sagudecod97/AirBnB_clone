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
        arr_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
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

            if len(arg_split) == 2:
                for item in storage.all():
                    index_str = item.find(arg_split[1])
                    if index_str != -1 and len(item[index_str:]) == len(arg_split[1]):
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

    def do_destroy(self, arg):
        flag = 0
        arr_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
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
        arr_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)

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

    def do_update(self, arg):
        flag = 0
        arr_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)

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
                    flag  = 1
            if flag:
                print("** class doesn't exist **")
            elif flag == 0 and len(arg_split) == 1:
                print("** instance id missing **")

            if len(arg_split) >= 2:
                for item in storage.all():
                    index_str = item.find(arg_split[1])
                    if index_str != -1 and len(item[index_str:]) == len(arg_split[1]):
                        flag = 0
                        break
                    else:
                        flag = 1
                if flag:
                    print("** no instance found **")
                if len(arg_split) == 2:
                    print("** attribute name missing **")
                else:
                    for key, value in storage.all().items():
                        v_dict = value.to_dict()
                        print("Not in: {}".format(arg_split[2] not in v_dict))
                        print("v_dict[__class__]: {} ---- arg_split[0]: {}".format(v_dict["__class__"], arg_split[0]))
                        if arg_split[2] not in v_dict and v_dict["__class__"] is arg_split[0]:
                            print("** value missing **")




def main():
    HBNBCommand().cmdloop()


main()
