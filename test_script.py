# Create a new band
band = Band(name="The Beatles", hometown="Liverpool")

# Create a new venue
venue = Venue(title="Wembley Stadium", city="London")

# Create a new concert
concert = Concert(date="2024-09-15", band=band, venue=venue)
session.add(concert)
session.commit()

# Test the methods
print(concert.introduction())  # Hello London!!!!! We are The Beatles and we're from Liverpool
print(concert.hometown_show())  # False
