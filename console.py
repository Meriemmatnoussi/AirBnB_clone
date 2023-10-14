#!/usr/bin/python3
"""Console Module"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User

classes = ["BaseModel", "User"]

class HBNBCommand(cmd.Cmd):
    """Project Console class"""
    prompt = "(hbnb) "

    def do_exit(self, line):
        """Quit command to exit the console"""
        return True

    def do_EOF(self, line):
        """Handle the End-Of-File (Ctrl + D) to exit the console"""
        return True

    def emptyline(self):
        """Empty line + ENTER shouldn't execute anything"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
            return
        try:
            obj = eval(line)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id
        """
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objects = storage.all()
        if key not in all_objects.keys():
            print("** no instance found **")
        else:
            print(all_objects[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        if not line:
            print("** class name missing **")
            return

        args = line.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if all_objs.get(key, None):
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based or
        not on the class name.
        Ex:
        $ all BaseModel
        or
        $ all.
        """
        all_objs = storage.all()
        if not line:
            print([str(obj) for obj in all_objs.values()])
        else:
            try:
                arg_cls = eval(line)
                filtered_objs = []
                for key, obj in all_objs.keys():
                    if key.split(".")[0] == line:
                        filtered_obj.append(str(obj))
                print(filtered_obj)
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file). 
        Ex: 
            $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        if not line:
            print("** class name missing **")

        args = line.split()
        if args[0] not in classes:
                print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in all_objects:
                print("** no instance found **")
                return

            if len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = storage.all()[key]
                attr_name = args[2]
                attr_value = args[3]
                setattr(obj, attr_name, attr_value)
                obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
