from sqlalchemy import Column, Integer, String, Float
from database.connection import Base


class CareerResult(Base):
    __tablename__ = 'CAREER_RESULT'

    id    = Column(Integer, primary_key=True)
    code  = Column(String)
    names = Column(String)
    eap   = Column(String)
    score = Column(Float)
    merit = Column(Integer)
    obs   = Column(String)
