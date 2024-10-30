from flask import Flask
from flask_httpauth import HTTPTokenAuth
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from loguru import logger

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy()
db.init_app(app)
token_auth = HTTPTokenAuth(scheme="Bearer")  # -H 'Authorization: Bearer Your-API-Key'


# authorization.py


# schemas.py
import marshmallow as ma


class PetSchema(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    name = ma.fields.String()


class PetQueryArgsSchema(ma.Schema):
    name = ma.fields.String(metadata={"description": "The name of the pet to filter."})


# resources.py
from flask.views import MethodView
from flask_smorest import Api, Blueprint, abort

blp = Blueprint("pets", "pets", url_prefix="/pets", description="Operations on pets")


@blp.route("/")
class Pets(MethodView):
    @blp.arguments(PetQueryArgsSchema, location="query")
    @blp.response(200, PetSchema(many=True))
    @token_auth.login_required
    def get(self, args):
        """List pets"""
        return get_pets(filters=args)

    @blp.arguments(PetSchema)
    @blp.response(201, PetSchema)
    def post(self, new_data):
        """Add a new pet"""
        pet = add_pet(**new_data)
        return pet


api = Api(app)
api.register_blueprint(blp)

with app.app_context():
    db.create_all()

    app.run(debug=True)
