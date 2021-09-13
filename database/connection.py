from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config import DB_SQLITE_NAME

print(DB_SQLITE_NAME)
engine = create_engine(f'sqlite:///{DB_SQLITE_NAME}', echo=True)
DBSession = sessionmaker(bind=engine)
Base = declarative_base()
