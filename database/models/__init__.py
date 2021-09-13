from database.connection import Base, engine
from database.models.career_result import CareerResult

Base.metadata.create_all(engine)
