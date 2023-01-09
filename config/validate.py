from jsonschema import validate
schema = {
    "type": "object",
    "properties": {
        "year": {
            "type": "string",
            "pattern": "^[12][0-9]{3}$" #Years from 1000 to 2999


        },
        "city": {"type": "string"},
        "status": {
            "type": "string",
            "enum": ["pre_venta", "en_venta", "vendido"]
            },
    }
}

def validate_schema(query):
    validate(query, schema=schema)