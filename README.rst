fast-json
=========

Fast JSON serialization and deserialization with ujson.

.. code-block:: python

    import fast_json

    print(
        fast_json.dumps({
            "foo": "bar",
             "now": datetime.datetime.now()
        })
    )

Serializing custom type
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import fast_json
    from collections import namedtuple


    MyType = namedtuple("MyType", ["name", "value"])


    @fast_json.convert.register(MyType)
    def _(value):
        return "name={0.name} value={0.value}".format(value)


    print(
        fast_json.dumps({
            "one": MyType(name="foo", value="bar")
        })
    )
