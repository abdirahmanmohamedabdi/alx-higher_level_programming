#!/usr/bin/python3
"""Checks if object is an instance of a class but
inherited from the specified class or not
"""


def inherits_from(obj, a_class):
    """Inherits true if object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise false
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
