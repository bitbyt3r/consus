from sqlalchemy import Column, Integer, String
from consus.database import Base

class FileObj(Base):
    __tablename__ = 'files'
    id =  Column(Integer, primary_key=True)

class Location(Base):
    __tablename__ = 'locations'
    id =  Column(Integer, primary_key=True)