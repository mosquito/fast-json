import base64
import json
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


@convert.register(bytes)
def _from_bytes(value: bytes):
    return base64.b64encode(value).decode()


@convert.register(DictItems)
def _from_dict_items(obj: DictItems):
    return dict(obj)


@convert.register(datetime)
def _from_date(obj: datetime):
    return obj.isoformat()


@convert.register(GeneratorType)
@convert.register(DictKeys)
@convert.register(DictValues)
def _from_iterable(value: Iterable):
    return [convert(item) for item in value]


def dumps(obj, *args, **kwargs):
    return json.dumps(
        convert(obj),
        *args, **kwargs
    )


def dump(obj, *args, **kwargs):
    return json.dump(
        convert(obj),
        *args, **kwargs
    )


loads = ujson.loads
load = ujson.load


__all__ = ('loads', 'load', 'dumps', 'dump')
