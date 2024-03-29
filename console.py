#!/usr/bin/python3
"""Module for HBNBCommand class."""

import cmd
import json
import sys
import inspect
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class."""
    prompt = '(hbnb) '
    glob_class = [item[0] for item in inspect.getmembers(sys.modules[__name__],
                                                         inspect.isclass)]
    arr_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)

    # ------ basic commands ------
    def do_EOF(self, arg):
        """Handles EOF\n"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Does nothing when type ENTER alone"""
        pass

    # ------ Instance commands ------

    def do_create(self, arg):
        """ Create: creates an Instance of the class """
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
        """ Show: prints the string representation of the instance """
        flag = 0
        arg_split = arg.split(' ')
        if arg_split[0] == '':
            print("** class name missing **")
        else:
            for k in self.arr_classes:
                if arg_split[0] in k:
                    flag = 0
                    break
                else:
                    flag = 1
            if flag:
                print("** class doesn't exist **")
                return
            elif flag == 0 and len(arg_split) == 1:
                print("** instance id missing **")
            elif len(storage.all()) == 0:
                print("** no instance found **")

            if len(arg_split) >= 2:
                for item in storage.all():
                    index_str = item.find(arg_split[1])
                    if index_str != -1 and \
                            len(item[index_str:]) == len(arg_split[1]):
                        flag = 0
                        break
                    else:
                        flag = 1
                if flag:
                    print("** no instance found **")
                    return
                else:
                    for key, value in storage.all().items():
                        if key.find(arg_split[1]) != -1:
                            print(value)

    def do_destroy(self, arg):
        """ Destroy: Destroys an Instance """
        flag = 0
        arg_split = arg.split(' ')
        if len(arg_split) > 1:
            arg_id = arg_split[1]
        else:
            arg_id = "NOT AN ID"
        k = {}
        if arg_split[0] == '':
            print("** class name missing **")
        else:
            for k in self.arr_classes:
                if arg_split[0] in k:
                    flag = 0
                    break
                else:
                    flag = 1
            if flag:
                print("** class doesn't exist **")
                return
            elif flag == 0 and len(arg_split) == 1:
                print("** instance id missing **")
                return

            if len(arg_split) >= 1:
                for item in storage.all():
                    index_id = item.find(arg_id)
                    if index_id != -1 and len(item[index_id:]) == len(arg_id):
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
                        if key.find(arg_split[1]) != -1\
                                and arg_split[0] in key:
                            k = key
                            flag = 1
                    if flag:
                        del copy_destroy[k]
                        storage.save()
                    else:
                        print("** no instance found **")

    def do_all(self, arg):
        """ All: Prints all the instances """
        flag = 0
        ret_obj = {}
        if arg != "":
            arg_split = arg.split(' ')
            for k in self.arr_classes:
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
        """ Update: Updates an Instance """
        flag = 0
        arg_split = arg.split(' ')
        if len(arg_split) > 1:
            arg_id = arg_split[1]
        else:
            arg_id = "NOT AN ID"

        if arg_id[0] == '"':
            arg_id = arg_id[1:-1]
        k = {}
        if arg_split[0] == '':
            print("** class name missing **")
        else:
            for k in self.arr_classes:
                if arg_split[0] in k:
                    flag = 0
                    break
                else:
                    flag = 1
            if flag:
                print("** class doesn't exist **")
                return
            elif flag == 0 and len(arg_split) == 1:
                print("** instance id missing **")
                return

            if len(arg_split) >= 2:
                for item in storage.all():
                    index_str = item.find(arg_id)
                    if index_str != -1 and \
                            len(item[index_str:]) == len(arg_id):
                        flag = 0
                        break
                    else:
                        flag = 1
                if flag:
                    print("** no instance found **")
                    return
                if len(arg_split) == 2:
                    print("** attribute name missing **")
                elif len(arg_split) == 3:
                    print("** value missing **")
                else:
                    with open("file.json", 'r+', encoding="utf-8") as f:
                        dic_read = json.loads(f.read())
                        key = str(arg_split[0]+"."+arg_split[1])
                        dic_kwargs = dic_read[key].copy()
                        store = storage.all()
                        arg_spl = arg_split[3]
                        arg_attr = arg_split[2]
                        arr_not_simple = ["id", "created_at", "updated_at"]

                        if arg_attr[0] == '"':
                            arg_attr = arg_attr[1:-1]
                        if arg_spl[0] == '"':
                            arg_spl = arg_spl[1:-1]

                        if arg_attr not in arr_not_simple:
                            if arg_spl.isdigit():
                                dic_kwargs[arg_attr] = int(arg_spl)
                            elif '.' in arg_spl:
                                dic_kwargs[arg_attr] = float(arg_spl)
                            else:
                                dic_kwargs[arg_attr] = arg_spl

                        obj_val = eval(str(arg_split[0]+"(**dic_kwargs)"))
                        dic_read[key] = dict(dic_kwargs)
                        store[key] = obj_val
                        f.seek(0)
                        f.write(json.dumps(dic_read))
                        f.truncate()

    def default(self, arg):
        """Counts the instances of a class.
        """
        self.precmd(arg)

    def precmd(self, arg):
        """Transform commands for class.syntax()"""

        cmd_match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", arg)
        if not cmd_match:
            return arg
        cname = cmd_match.group(1)
        method = cmd_match.group(2)
        args = cmd_match.group(3)
        get_id_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if get_id_and_args:
            cid = get_id_and_args.group(1)
            attr_or_dict = get_id_and_args.group(2)
        else:
            cid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            upt_dict = re.search('^({.*})$', attr_or_dict)
            if upt_dict:
                self.update_dict(cname, cid, upt_dict.group(1))
                return ""
            get_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if get_attr_and_value:
                attr_and_value = (get_attr_and_value.group(
                    1) or "") + " " + (get_attr_and_value.group(2) or "")
        command = method + " " + cname + " " + cid + " " + attr_and_value
        return command

    def update_dict(self, classname, cid, attr_dict):
        """method for update() with a dictionary."""
        s_dict = attr_dict.replace("'", '"')
        j_dict = json.loads(s_dict)
        if not classname:
            print("** class name missing **")
        elif classname not in self.glob_class:
            print("** class doesn't exist **")
        elif cid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, cid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attr = inspect.getmembers(classname, lambda a:
                                          not (inspect.isroutine(a)))
                for attribute, value in j_dict.items():
                    if attribute in attr:
                        value = attr[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_count(self, arg):
        """ Count: counts the number of instances """
        arg_split = arg.split(' ')
        if not arg_split[0]:
            print("** class name missing **")
        elif arg_split[0] not in self.glob_class:
            print("** class doesn't exist **")
        else:
            count = [key for key in storage.all()
                     if key.startswith(arg_split[0] + '.')]
            print(len(count))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
