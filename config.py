from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create the engine
engine = create_engine('sqlite:///yourdatabase.db')  # Adjust to your database

# Create the session
Session = sessionmaker(bind=engine)

# Create a new Session instance
session = Session()

# Import Base
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
