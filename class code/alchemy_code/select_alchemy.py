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


# Query a specific plane
my_plane = session.query(Plane).filter(Plane.tailno == '101').first()


if my_plane:
    print("Plane:")
    print(f"Tail No: {my_plane.tailno}, Make: {my_plane.make}, Model: {my_plane.model}, Capacity: {my_plane.capacity}, MPH: {my_plane.mph}")

    # and lets see how we can get the "reverse" relationship
    print("Flights:")
    for flight in my_plane.flights: # note that this line actually ran a sql query
        print(f"Flight No: {flight.flight_no}, Departure: {flight.dep_loc} at {flight.dep_time}, Arrival: {flight.arr_loc} at {flight.arr_time}")

    # lets add a flight 
    new_flight = Flight(flight_no='104', dep_loc='JFK', dep_time='10:00', arr_loc='LAX', arr_time='14:00', tail_no='101')

    session.add(new_flight)

    session.commit()

    print("Flights:")

    for flight in my_plane.flights:
        print(f"Flight No: {flight.flight_no}, Departure: {flight.dep_loc} at {flight.dep_time}, Arrival: {flight.arr_loc} at {flight.arr_time}")

