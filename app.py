from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///concert.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Band, Venue, Concert  # Import your models

if __name__ == '__main__':
    app.run()

from models import Band, Venue, Concert
from config import Session, engine, Base

# Create the tables
Base.metadata.create_all(engine)

# Create a session
session = Session()

# Add data to the tables
band1 = Band(name="The Rolling Stones", hometown="London")
band2 = Band(name="Coldplay", hometown="London")

venue1 = Venue(title="Madison Square Garden", city="New York")
venue2 = Venue(title="Wembley Stadium", city="London")

concert1 = Concert(date="2024-10-10", band=band1, venue=venue1)
concert2 = Concert(date="2024-12-05", band=band1, venue=venue2)
concert3 = Concert(date="2024-08-20", band=band2, venue=venue2)

session.add_all([band1, band2, venue1, venue2, concert1, concert2, concert3])
session.commit()

# Test the methods
print(band1.venues())  # Should return the venues where band1 played
print(venue1.bands())  # Should return bands that played at venue1
print(concert1.introduction())  # Introduction for the concert
