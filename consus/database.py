import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Database:
    def __init__(self):
        self.db_uri = ""
        self.conn = None
        self.Session = None

    def connect(self, db_uri=None):
        """Starts a db connection and initializes the schema
        """
        if db_uri:
            self.db_uri = db_uri
        self.conn = sqlalchemy.create_engine(self.db_uri)
        self.Session = sessionmaker(bind=self.conn)
        Base.metadata.create_all(bind=self.conn.engine)