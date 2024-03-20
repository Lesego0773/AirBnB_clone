#!/usr/bin/python3
import cmd
from BaseModel import BaseModel
import file_storage
import user
import place
import review
import state
import city
import amenity



class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB Clone"""
    prompt = "(hbnb)"
    __classes = {"User": user, "Place": place, "Review": review, "State": state, "City": city, "Amenity": amenity}

    def do_create(self, args):
        """Creating a new instance of the create class"""
        args = args.split()

        if len(args) < 1:
            print("**class name missing**")
            return
        class_name = args[0]

        if class_name not in self.__classes:
            print("**class name doesn't exist**")
            return
        new_instance = self.__classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Showing string representation of an instance"""

        args = args.split()

        if len(args) < 2:
            print("**instance is missing**")
            return
        class_name = args[0]
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        if key not in file_storage.all():
            print("**no instance is found**")
            return
        print(file_storage.all()[key])

    def do_update(self, args):
        """Updating an instance based on the class name and id"""
        args = args.split()
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
            if key not in file_storage.all():
                print("** no instance found **")
                return
            obj = file_storage.all()[key]
            setattr(obj, args[2], args[3])
            obj.save()
    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):

        print("")  # Printing newline before exiting
        return True

    def emptyline(self,args):
        """Called when an empty line is entered"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()







