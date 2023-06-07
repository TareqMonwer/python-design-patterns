from importlib import import_module
from inspect import getmembers, isclass, isabstract
from creational.factory_classic.factories.abs_factory import AbsFactory


def load_factory(factory_name):
    try:
        factory_module = import_module("creational.factory_classic.factories." + factory_name, package="creational")
    except ImportError:
        factory_module = import_module("creational.factory_classic.factories.nullcar_factory", package="creational")

    classes = getmembers(factory_module,
                         lambda m: isclass(m) and not isabstract(m))

    for _factory_class, _class in classes:
        if issubclass(_class, AbsFactory):
            return _class()
