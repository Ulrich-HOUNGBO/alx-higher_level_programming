#!/usr/bin/python3
import json
import csv


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            list_dictionaries = []

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        objc = []
        if list_objs is not None:
            for o in list_objs:
                objc.append(cls.to_dictionary(o))
                filename = cls.__name__ + ".json"
                with open(filename, "w") as f:
                    f.write(cls.to_json_string(objc))

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with attributes already set"""
        if cls.__name__ == "Square":
            dum = cls(1)
        if cls.__name__ == "Rectangle":
            dum = cls(1, 1)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        instance_list = []
        try:
            with open(filename, "r") as f:
                instances = cls.from_json_string(f.read())
            for i, dic in enumerate(instances):
                instance_list.append(cls.create(**instances[i]))
        except:
            pass
        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for o in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([o.id, o.width, o.height, o.x, o.y])
                if cls.__name__ == "Square":
                    writer.writerow([o.id, o.size, o.x, o.y])

    @classmethod
    def load_from_file_csv(cls):
        objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dic = {"id": int(row[0]),
                           "width": int(row[1]),
                           "height": int(row[2]),
                           "x": int(row[3]),
                           "y": int(row[4])}
                if cls.__name__ == "Square":
                    dic = {"id": int(row[0]),
                           "size": int(row[1]),
                           "x": int(row[2]),
                           "y": int(row[3])}
                o = cls.create(**dic)
                objs.append(o)
        return objs