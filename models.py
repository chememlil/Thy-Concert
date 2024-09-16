from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Band model
class Band(Base):
    __tablename__ = 'bands'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hometown = Column(String)
    
    concerts = relationship('Concert', back_populates='band')
    
    def concerts(self):
        return self.concerts
    
    def venues(self):
        return [concert.venue for concert in self.concerts]

# Venue model
class Venue(Base):
    __tablename__ = 'venues'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    city = Column(String)
    
    concerts = relationship('Concert', back_populates='venue')
    
    def concerts(self):
        return self.concerts
    
    def bands(self):
        return [concert.band for concert in self.concerts]

# Concert model
class Concert(Base):
    __tablename__ = 'concerts'
    
    id = Column(Integer, primary_key=True)
    date = Column(String)  # Storing date as a string for simplicity
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))
    
    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')
    
    def band(self):
        return self.band
    
    def venue(self):
        return self.venue
    
    def hometown_show(self):
        return self.venue.city == self.band.hometown
    
    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
