#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_create(self, arg):
        """Creating a new instance of BaseModel and saving it to JSON file, and print its id"""
        if not arg:
            print("** class name missing **")
        else:
            class_name = arg.split()[0]
            if class_name not in ["BaseModel"]:
                print("** class doesn't exist **")
            else:
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, arg):
        """Printing the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """Deleting an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Printing all string representation of all instances"""
        args = arg.split()
        instances = []
        if not arg or args[0] in ["BaseModel"]:
            for key, value in storage.all().items():
                instances.append(str(value))
            print(instances)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updating an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
                return
            obj = storage.all()[key]
            setattr(obj, args[2], args[3])
            obj.save()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        
        print("")  # Printing newline before exiting
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()

