# /home/chemelil/Thy-Concert/tests/test_models.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import engine, Base, session
from models import Band, Venue, Concert

def setup():
    """Create tables and add test data."""
    Base.metadata.create_all(engine)

def add_data():
    """Add sample data to the database."""
    # Clear previous data
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    band1 = Band(name="The Rockers", hometown="Nashville")
    band2 = Band(name="The Jazzers", hometown="New York")

    venue1 = Venue(title="Grand Hall", city="Nashville")
    venue2 = Venue(title="Jazz Club", city="New York")

    session.add_all([band1, band2, venue1, venue2])
    session.commit()

    concert1 = Concert(date="2024-09-30", band=band1, venue=venue1)
    concert2 = Concert(date="2024-10-01", band=band2, venue=venue2)
    
    session.add_all([concert1, concert2])
    session.commit()

def query_data():
    """Query and print data to verify functionality."""
    bands = session.query(Band).all()
    for band in bands:
        print(f"Band: {band}")
        print("Venues:", band.get_venues())
        print("Introductions:", band.all_introductions())

    venues = session.query(Venue).all()
    for venue in venues:
        print(f"Venue: {venue}")
        print("Bands:", venue.get_bands())
        print("Concert on 2024-09-30:", venue.concert_on("2024-09-30"))
        print("Most Frequent Band:", venue.most_frequent_band())

def main():
    setup()
    add_data()
    query_data()

if __name__ == "__main__":
    main()
