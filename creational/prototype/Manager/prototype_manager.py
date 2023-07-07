from typing import Any
from abs_prototype import AbsPrototype


class PrototypeManager(dict):
    def __setitem__(self, __key: Any, __prototype: Any) -> None:
        if issubclass(__prototype, AbsPrototype):
            dict.__setitem__(self, __key, __prototype)