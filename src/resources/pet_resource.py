from flask.views import MethodView
from flask_smorest import Blueprint, abort

from app import token_auth
from schemas.pet_schema import PetSchema, PetQueryArgsSchema
from services import pet_service


pet_resource = Blueprint(
    "pets", "pets", url_prefix="/api/pets", description="Operations on pets"
)


@pet_resource.route("/")
class PetsResource(MethodView):
    @pet_resource.arguments(PetQueryArgsSchema, location="query")
    @pet_resource.response(200, PetSchema(many=True))
    @token_auth.login_required
    def get(self, args) -> list[dict]:
        """List all pets."""
        return pet_service.get_all(filters=args)

    @pet_resource.arguments(PetSchema)
    @pet_resource.response(201, PetSchema)
    def post(self, new_data: dict) -> dict:
        """Adds a new pet."""
        pet = pet_service.add(new_data)
        return pet
