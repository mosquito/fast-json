import base64
import json
from collections.abc import Iterator
from datetime import datetime
from functools import singledispatch
from types import MappingProxyType

import ujson


DictItems = type({}.items())
DictKeys = type({}.keys())
DictValues = type({}.values())


@singledispatch
def convert(obj):
    return str(obj)


@convert.register(bytes)
def _from_bytes(value: bytes):
    return base64.b64encode(value).decode()


@convert.register(datetime)
def _from_date(obj: datetime):
    return obj.isoformat()


@convert.register(DictKeys)
@convert.register(DictValues)
@convert.register(Iterator)
@convert.register(frozenset)
@convert.register(range)
@convert.register(set)
def _from_iterable(value):
    return [convert(item) for item in value]


@convert.register(DictItems)
@convert.register(MappingProxyType)
def _from_dict_items(obj: DictItems):
    return dict(obj)


@convert.register(bytearray)
@convert.register(memoryview)
def _from_views(value):
    return bytes(value)


def dumps(obj, *args, **kwargs):
    return json.dumps(
        obj, default=convert,
        *args, **kwargs
    )


def dump(obj, *args, **kwargs):
    return json.dump(
        obj, default=convert,
        *args, **kwargs
    )


loads = ujson.loads
load = ujson.load


__all__ = ('loads', 'load', 'dumps', 'dump')
