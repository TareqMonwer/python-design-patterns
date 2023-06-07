# loader.py
from importlib import import_module
from inspect import getmembers, isclass, isabstract

from creational.abs_factory.factories.furniture_factory import AbsFurnitureFactory


def load_factory(factory_name):
    factory_module = import_module(f"factories.{factory_name}_factory",
                                   package="creational")
    classes = getmembers(factory_module, lambda m: isclass(m) and not isabstract(m))

    for _, _class in classes:
        if issubclass(_class, AbsFurnitureFactory):
            return _class()
