# models.py
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from config import Base, session

class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    hometown = Column(String)
    
    concerts = relationship('Concert', back_populates='band')

    def __repr__(self):
        return f"<Band(name={self.name}, hometown={self.hometown})>"

    def get_concerts(self):
        return self.concerts

    def get_venues(self):
        return {concert.venue for concert in self.get_concerts()}

    def all_introductions(self):
        return [concert.introduction() for concert in self.get_concerts()]

    @classmethod
    def most_performances(cls):
        return max(session.query(cls).all(), key=lambda band: len(band.get_concerts()), default=None)

class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    city = Column(String)
    
    concerts = relationship('Concert', back_populates='venue')

    def __repr__(self):
        return f"<Venue(title={self.title}, city={self.city})>"

    def get_concerts(self):
        return self.concerts

    def get_bands(self):
        return {concert.band for concert in self.get_concerts()}

    def concert_on(self, date):
        return session.query(Concert).filter_by(venue=self, date=date).first()

    def most_frequent_band(self):
        bands = self.get_bands()
        if not bands:
            return None
        return max(bands, key=lambda band: len([c for c in self.get_concerts() if c.band == band]))

class Concert(Base):
    __tablename__ = 'concerts'

    id = Column(Integer, primary_key=True)
    date = Column(String)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))

    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')

    def __repr__(self):
        return f"<Concert(date={self.date}, band={self.band.name}, venue={self.venue.title})>"

    def get_band(self):
        return self.band

    def get_venue(self):
        return self.venue

    def hometown_show(self):
        return self.get_venue().city == self.get_band().hometown

    def introduction(self):
        return f"Hello {self.get_venue().city}!!!!! We are {self.get_band().name} and we're from {self.get_band().hometown}"

    def play_in_venue(self, venue, date):
        new_concert = Concert(band=self, venue=venue, date=date)
        session.add(new_concert)
        session.commit()
