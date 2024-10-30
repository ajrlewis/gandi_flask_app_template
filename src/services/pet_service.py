from loguru import logger

from app import db
from models.pet import Pet


def get_all(filters: dict) -> list[Pet]:
    logger.debug(f"{filters = }")
    pets = db.session.query(Pet).filter_by(**filters).all()
    logger.debug(f"{pets = }")
    return pets


def add(data: dict) -> Pet:
    logger.debug(f"{data = }")
    pet = Pet(**data)
    db.session.add(pet)
    db.session.commit()
    return pet
