#!/usr/bin/python3
"""Console Module"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Project Console class"""
    def do_exit(self, line):
        """Exit the console"""
        return True

    def do_EOF(self, line):
        """Exit the console"""
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            bm = BaseModel()
            storage.new(bm)
            storage.save()
            print(bm.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = line.split(" ")
        if not line:
            print("** class name missing **")
        elif len(args) >= 1 and args[0] != "BaseModel":
                print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            obj_key = "BaseModel.{}".format(args[1])
            if all_objs.get(obj_key, None):
                print(all_objs[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        args = line.split(" ")
        if not line:
            print("** class name missing **")
        elif len(args) >= 1 and args[0] != "BaseModel":
                print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            obj_key = "BaseModel.{}".format(args[1])
            if all_objs.get(obj_key, None):
                del all_objs[obj_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based or
        not on the class name.
        Ex: $ all BaseModel or $ all.
        """
        if line and line != "BaseModel":
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            objs_list = []
            for key, obj in all_objs.items():
                objs_list.append(str(obj))
            print(objs_list)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
