import sqlite3

# connect to the database
con = sqlite3.connect("airlineTEST.db")
cur = con.cursor()

# query all planes from the plane table
cur.execute("SELECT * FROM plane")
planes = cur.fetchall()  # fetch all rows as a list of tuples
print("Planes:", planes)

# query all passengers from the passengers table
cur.execute("SELECT * FROM passengers")
passengers = cur.fetchall()
print("Passengers:", passengers)

# query all flights from the flight table
cur.execute("SELECT * FROM flight")
flights = cur.fetchall()
print("Flights:", flights)

# query all onboard data from the onboard table
cur.execute("SELECT * FROM onboard")
onboard = cur.fetchall()
print("Onboard:", onboard)

# query a specific flight by flight_no and return it as a dictionary
flight_no = '101'
cur.execute("SELECT * FROM flight WHERE flight_no = ?", (flight_no,))
specific_flight = cur.fetchone()  # fetch one row
if specific_flight:
    flight_dict = {
        "flight_no": specific_flight[0],
        "dep_loc": specific_flight[1],
        "dep_time": specific_flight[2],
        "arr_loc": specific_flight[3],
        "arr_time": specific_flight[4],
        "tail_no": specific_flight[5]
    }
    print("Specific Flight:", flight_dict)

# close the connection
con.close()
