#!/usr/bin/env python3
"""Task 11"""
from typing import Any, TypeVar, Mapping, Union, Optional
T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """Function defined in the project's last mandatory task"""
    if key in dct:
        return dct[key]
    else:
        return default
