import sqlite3

con = sqlite3.connect("airlineTEST2.db")
cur = con.cursor()

# read the airline.sql DDL file
with open("airline.sql", "r") as f:
    ddl = f.read()

# execute the DDL file
cur.executescript(ddl)

# insert some data into the plane table (tailno, make, model, capacity, mph)
cur.execute("INSERT INTO plane VALUES (?, ?, ?, ?, ?)", ('101', 'Boeing', '757', '200', 500))
cur.execute("INSERT INTO plane VALUES (?, ?, ?, ?, ?)", ('102', 'Boeing', '757', 200, 500))
cur.execute("INSERT INTO plane VALUES (?, ?, ?, ?, ?)", ('103', 'Boeing', '757', 200, 500))
cur.execute("INSERT INTO plane VALUES (?, ?, ?, ?, ?)", ('104', 'Boeing', '757', 200, 500))
cur.execute("INSERT INTO plane VALUES (?, ?, ?, ?, ?)", ('105', 'Airbus', 'A320', 150, 450))
cur.execute("INSERT INTO plane VALUES (?, ?, ?, ?, ?)", ('106', 'Airbus', 'A320', 150, 450))
cur.execute("INSERT INTO plane VALUES (?, ?, ?, ?, ?)", ('107', 'Airbus', 'A320', 150, 450))

# insert some data into the passengers table (first, middle, last, ssn)
cur.execute("INSERT INTO passengers VALUES (?, ?, ?, ?)", ('John', 'Doe', 'Smith', 123456789))
cur.execute("INSERT INTO passengers VALUES (?, ?, ?, ?)", ('Jane', 'Doe', 'Smith', 987654321))
cur.execute("INSERT INTO passengers VALUES (?, ?, ?, ?)", ('Alice', 'Wonderland', 'Smith', 123123123))
cur.execute("INSERT INTO passengers VALUES (?, ?, ?, ?)", ('Bob', 'Apples', 'Smith', 456456456))

# insert some data into the flight table (flight_no, dep_loc, dep_time, arr_loc, arr_time, tail_no)
cur.execute("INSERT INTO flight VALUES (?, ?, ?, ?, ?, ?)", ('101', 'JFK', '10:00', 'LAX', '14:00', 101))
cur.execute("INSERT INTO flight VALUES (?, ?, ?, ?, ?, ?)", ('102', 'MIA', '11:00', 'LAX', '15:00', 102))
cur.execute("INSERT INTO flight VALUES (?, ?, ?, ?, ?, ?)", ('103', 'TPA', '12:00', 'LAX', '16:00', 103))

# insert some data into the onboard table (ssn, flight_no, seat)
cur.execute("INSERT INTO onboard VALUES (?, ?, ?)", (123456789, '101', '1A'))
cur.execute("INSERT INTO onboard VALUES (?, ?, ?)", (987654321, '101', '1B'))
cur.execute("INSERT INTO onboard VALUES (?, ?, ?)", (123123123, '102', '2A'))
cur.execute("INSERT INTO onboard VALUES (?, ?, ?)", (456456456, '103', '3A'))

# commit the changes
con.commit()

# close the connection
con.close()
