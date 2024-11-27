# import our models from the other file
from alchemyBase import Base, Plane, Passenger, Flight, Onboard
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# to show the sql that is running
import logging

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

# this is our "connection" to the database
engine = create_engine('sqlite:///airlineAlchemyExample.db')

# Now a session to start working with the database
Session = sessionmaker(bind=engine)
session = Session(expire_on_commit=True) # This parameter can reduce unnecessary SQL calls in some cases

all_planes = session.query(Plane).all()
print("Planes:")
for plane in all_planes:
    print(f"Tail No: {plane.tailno}, Make: {plane.make}, Model: {plane.model}, Capacity: {plane.capacity}, MPH: {plane.mph}")

# Query all passengers
all_passengers = session.query(Passenger).all()
print("\nPassengers:")
for passenger in all_passengers:
    print(f"SSN: {passenger.ssn}, Name: {passenger.first} {passenger.middle} {passenger.last}")

# Query all flights
all_flights = session.query(Flight).all()
print("\nFlights:")
for flight in all_flights:
    print(f"Flight No: {flight.flight_no}, Departure: {flight.dep_loc} at {flight.dep_time}, Arrival: {flight.arr_loc} at {flight.arr_time}, Tail No: {flight.tail_no}")

# Query all onboard data
all_onboard = session.query(Onboard).all()
print("\nOnboard:")
for onboard in all_onboard:
    print(f"SSN: {onboard.ssn}, Flight No: {onboard.flight_no}, Seat: {onboard.seat}")

# Close the session
session.close()
