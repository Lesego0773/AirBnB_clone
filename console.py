#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)' # Setting the prompt string

    def do_quit(self, arg):
        """quit command the program"""

        return True # Returning true will exit the command loop

    def do_EOF(self, arg):

        print("")
        return True

    def empty_line(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
