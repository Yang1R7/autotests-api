from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "username": {"type": "string", "minLength": 5, "maxLength": 15}
    },
    "required": ["username"]
}

data = {
    "name": "Alice",
    "age": 30
}

validate(instance=data, schema=schema)
