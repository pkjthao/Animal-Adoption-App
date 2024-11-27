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

# here, I'm just making a python object
myPlane = Plane(tailno='101', make='Boeing', model='757', capacity=200, mph=500)

# now I "add" it to the session
session.add(myPlane)

# now I "commit" the session
session.commit()

# now let's change the mph to 600
myPlane.mph = 600

# now commit
session.commit()

# let's confirm this is all working via sqlitestudio
# Pause here and check the database

# now lets delete it from the database
session.delete(myPlane)
session.commit()

# confirm again that it is working
