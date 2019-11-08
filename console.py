#!/usr/bin/python3
"""Module for HBNBCommand class."""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class."""
    prompt = '(hbnb) '

    # ----- basic commands -----
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


def main():
    HBNBCommand().cmdloop()


main()
