import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Imprime los logs en tiempo real
logger = logging.getLogger()

from config import config

conn = create_engine(config.get("database"))

Session = sessionmaker(bind=conn)

session = Session()

Base = declarative_base()
