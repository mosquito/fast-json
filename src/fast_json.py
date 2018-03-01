import base64
import ujson
from functools import singledispatch
from types import GeneratorType
from typing import Any, Iterable

from datetime import datetime

DictItems = type({}.items())
DictKeys = type({}.keys())
DictValues = type({}.values())


@singledispatch
def convert(obj: Any):
    return str(obj)


@convert.register(str)
@convert.register(int)
@convert.register(float)
@convert.register(type(None))
@convert.register(bool)
def _bypass(value):
    return value


@convert.register(bytes)
def _from_bytes(value: bytes):
    return base64.b64encode(value)


@convert.register(dict)
def _from_dict(obj: dict):
    return {str(key): convert(value) for key, value in obj.items()}


@convert.register(DictItems)
def _from_dict_items(obj: DictItems):
    return {str(key): convert(value) for key, value in obj}


@convert.register(datetime)
def _from_date(obj: datetime):
    return obj.isoformat()


@convert.register(list)
@convert.register(tuple)
@convert.register(set)
@convert.register(frozenset)
@convert.register(GeneratorType)
@convert.register(DictKeys)
@convert.register(DictValues)
def _from_iterable(value: Iterable):
    return {convert(item) for item in value}


def dumps(obj, *args, **kwargs):
    return ujson.dumps(
        convert(obj),
        escape_forward_slashes=False,
        *args, **kwargs
    )


def dump(obj, *args, **kwargs):
    return ujson.dump(
        convert(obj),
        escape_forward_slashes=False,
        *args, **kwargs
    )


loads = ujson.loads
load = ujson.load


__all__ = ('loads', 'load', 'dumps', 'dump')
