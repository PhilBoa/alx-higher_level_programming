#!/usr/bin/python3
import json
import csv

"""This module defines a class Base"""


class Base:
    """
    Base class.

    Attributes:
        __nb_objects (int): Private class attribute to keep track
        of the number of objects created.
        id (int): Public instance attribute representing the unique
        identifier for each object.
        If id is provided, assign it to the id attribute.
        Otherwise, increment __nb_objects and assign the new value
        to the id attribute.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the Base object.

        Args:
        id (int, optional): Unique identifier for the object.
        Defaults to None.
            If provided, it will be assigned to the id attribute.
            If not provided, __nb_objects will be incremented, and
            its value will be assigned to the id attribute.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances.

        Note:
            The filename is derived from the class name by appending
            '.json' to it.
        """

        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            file.write(cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of dictionaries from a JSON string.

        Args:
            json_string (str): JSON string representing a list of
            dictionaries.

        Returns:
            list: List of dictionaries represented by the JSON string.
        """

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set from a dictionary.

        Args:
            **dictionary (dict): Double pointer to a dictionary
            containing attribute names and values.

        Returns:
            Base: Instance of the class with attributes set from
            the dictionary.
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            raise ValueError("Invalid class name.")

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a JSON file.

        Returns:
            list: List of instances loaded from the JSON file.
        """

        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                dicts = cls.from_json_string(json_string)
                return [cls.create(**dictionary) for dictionary in dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize instances to a CSV file.

        Args:
            list_objs (list): List of instances to be serialized.
        """

        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            write = csv.writer(file)
            for obj in list_objs:
                write.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize instances from a CSV file.

        Returns:
            list: List of instances deserialized from the CSV file.
        """

        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                read = csv.reader(file)
                instances = []
                for row in read:
                    obj_dict = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                            }
                    instance = cls.create(**obj_dict)
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []
