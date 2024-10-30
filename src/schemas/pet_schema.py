import marshmallow as ma


class PetSchema(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    name = ma.fields.String()


class PetQueryArgsSchema(ma.Schema):
    name = ma.fields.String(metadata={"description": "The name of the pet to filter."})
