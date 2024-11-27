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
session = Session(expire_on_commit=False) # This parameter can reduce unnecessary SQL calls in some cases


# Here we make a list of plane objects and "add_all" to the session
planes = [
    Plane(tailno='101', make='Boeing', model='757', capacity=200, mph=500),
    Plane(tailno='102', make='Boeing', model='757', capacity=200, mph=500),
    Plane(tailno='103', make='Boeing', model='757', capacity=200, mph=500),
    Plane(tailno='104', make='Boeing', model='757', capacity=200, mph=500),
    Plane(tailno='105', make='Airbus', model='A320', capacity=150, mph=450),
    Plane(tailno='106', make='Airbus', model='A320', capacity=150, mph=450),
    Plane(tailno='107', make='Airbus', model='A320', capacity=150, mph=450)
]
session.add_all(planes) # no sql required...

# same for passengers
passengers = [
    Passenger(first='John', middle='Doe', last='Smith', ssn=123456789),
    Passenger(first='Jane', middle='Doe', last='Smith', ssn=987654321),
    Passenger(first='Alice', middle='Wonderland', last='Smith', ssn=123123123),
    Passenger(first='Bob', middle='Apples', last='Smith', ssn=456456456)
]
session.add_all(passengers)

# Now flights
flights = [
    Flight(flight_no='101', dep_loc='JFK', dep_time='10:00', arr_loc='LAX', arr_time='14:00', tail_no='101'),
    Flight(flight_no='102', dep_loc='MIA', dep_time='11:00', arr_loc='LAX', arr_time='15:00', tail_no='102'),
    Flight(flight_no='103', dep_loc='TPA', dep_time='12:00', arr_loc='LAX', arr_time='16:00', tail_no='103')
]
session.add_all(flights)

# tickets
onboard_data = [
    Onboard(ssn=123456789, flight_no='101', seat='1A'),
    Onboard(ssn=987654321, flight_no='101', seat='1B'),
    Onboard(ssn=123123123, flight_no='102', seat='2A'),
    Onboard(ssn=456456456, flight_no='103', seat='3A')
]
session.add_all(onboard_data)

# Commit to db
session.commit()
