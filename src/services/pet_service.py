from typing import Optional

from loguru import logger
from sqlalchemy.exc import IntegrityError

from app import db
from models.pet import Pet


def get(pet_id: int) -> Optional[Pet]:
    logger.debug(f"{pet_id = }")
    pet = db.session.get(Pet, pet_id)
    logger.debug(f"{pet = }")
    return pet


def get_all(filters: dict) -> list[Pet]:
    logger.debug(f"{filters = }")
    pets = db.session.query(Pet).filter_by(**filters).all()
    logger.debug(f"{pets = }")
    return pets


def add(data: dict) -> Optional[Pet]:
    logger.debug(f"{data = }")
    pet = Pet(**data)
    try:
        db.session.add(pet)
        db.session.commit()
    except IntegrityError as e:
        logger.error(f"unable to add pet to database: {e = }")
        db.session.rollback()
    else:
        logger.debug(f"{pet = }")
        return pet
