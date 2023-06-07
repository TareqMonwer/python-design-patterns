from importlib import import_module
from inspect import getmembers, isclass, isabstract
from .factories import AbsFactory


def load_factory(factory_name):
    try:
        factory_module = import_module(".factories." + factory_name, package="factory_classic")
    except ImportError:
        factory_module = import_module(".factories.nullcar_factory", package="factory_classic")

    classes = getmembers(factory_module,
                         lambda m: isclass(m) and not isabstract(m))

    for _, _class in classes:
        if issubclass(_class, AbsFactory):
            return _class()
