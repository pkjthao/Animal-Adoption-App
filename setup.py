import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('animal_shelter.db')
cursor = connection.cursor()


# Insert data into Staff
staff_data = [
    ("S001", "John", "Doe", "Manager", 1234567890, "john.doe@example.com", "2023-01-01", 50000, 1, "Active", "pass123"),
    ("S002", "Jane", "Smith", "Vet", 1234567891, "jane.smith@example.com", "2023-02-01", 45000, 2, "Active", "pass456"),
    ("S003", "Alice", "Brown", "Technician", 1234567892, "alice.brown@example.com", "2023-03-01", 40000, 1, "Active", "pass789"),
    ("S004", "Bob", "White", "Assistant", 1234567893, "bob.white@example.com", "2023-04-01", 35000, 2, "Active", "pass101"),
    ("S005", "Eve", "Green", "Coordinator", 1234567894, "eve.green@example.com", "2023-05-01", 30000, 1, "Active", "pass202"),
]

cursor.executemany("""
INSERT INTO Staff (staffID, firstName, lastName, position, phoneNumber, email, hireDate, salary, workLocation, status, password)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
""", staff_data)

# Insert data into Adopters
adopters_data = [
    ("A001", "Charlie", "Taylor", 9876543210, "charlie.taylor@example.com", "123 Maple St", "secure123"),
    ("A002", "Dana", "Wilson", 9876543211, "dana.wilson@example.com", "456 Oak St", "secure456"),
    ("A003", "Frank", "Thomas", 9876543212, "frank.thomas@example.com", "789 Pine St", "secure789"),
    ("A004", "Grace", "Harris", 9876543213, "grace.harris@example.com", "321 Birch St", "secure101"),
    ("A005", "Hank", "Walker", 9876543214, "hank.walker@example.com", "654 Elm St", "secure202"),
]

cursor.executemany("""
INSERT INTO Adopters (adopterID, firstName, lastName, phoneNumber, email, address, password)
VALUES (?, ?, ?, ?, ?, ?, ?);
""", adopters_data)

# Insert data into Animals
animals_data = [
    (1, "Buddy", "Dog", "Labrador", 3, "Male", "2023-01-15", 0, "Healthy", "Friendly dog", 1, "Stray"),
    (2, "Mittens", "Cat", "Siamese", 2, "Female", "2023-02-10", 0, "Healthy", "Playful cat", 2, "Surrendered"),
    (3, "Shadow", "Dog", "German Shepherd", 5, "Male", "2023-03-05", 1, "Healthy", "Loyal companion", 1, "Lost"),
    (4, "Bella", "Cat", "Persian", 4, "Female", "2023-04-20", 0, "Healthy", "Calm demeanor", 2, "Stray"),
    (5, "Max", "Dog", "Beagle", 1, "Male", "2023-05-25", 0, "Healthy", "Energetic puppy", 1, "Stray"),
]

cursor.executemany("""
INSERT INTO Animals (animalID, name, species, breed, age, gender, dateOfArrival, adoptedOrNot, healthStatus, description, locationID, reasonForIntake)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
""", animals_data)

# Insert data into Adoption_Requests
adoption_requests_data = [
    ("AR001", "A001", 3, "2023-03-15", 150, "Approved", "S001"),
    ("AR002", "A002", 1, "2023-04-01", 200, "Pending", "S002"),
    ("AR003", "A003", 2, "2023-04-20", 100, "Denied", "S003"),
    ("AR004", "A004", 4, None, 150, "Pending", "S004"),
    ("AR005", "A005", 5, None, 180, "Pending", "S005"),
]

cursor.executemany("""
INSERT INTO Adoption_Requests (adoptionID, adopterID, animalID, dateAdopted, adoptionFee, adoptionStatus, staffAdministrator)
VALUES (?, ?, ?, ?, ?, ?, ?);
""", adoption_requests_data)

# Insert data into Medical_Records
medical_records_data = [
    (1, 1, "S002", "Mild fever", "Antibiotics", "2023-01-20", "Recovered quickly"),
    (2, 2, "S003", "Minor wound", "Disinfection", "2023-02-15", "Healing well"),
    (3, 3, "S002", "Eye infection", "Eye drops", "2023-03-10", "Requires follow-up"),
    (4, 4, "S004", "Malnutrition", "Nutritional diet", "2023-04-25", "Improving"),
    (5, 5, "S003", "Healthy checkup", "None", "2023-05-30", "No issues"),
]

cursor.executemany("""
INSERT INTO Medical_Records (medicalID, animalID, staffID, diagnosis, treatment, date, note)
VALUES (?, ?, ?, ?, ?, ?, ?);
""", medical_records_data)

# Insert data into Shelter_Locations
shelter_locations_data = [
    (1, "Main Shelter", "123 Shelter Lane", 1234567899, 50, 45),
    (2, "East Shelter", "456 Rescue Road", 1234567888, 30, 28),
    (3, "West Shelter", "789 Haven Blvd", 1234567877, 40, 35),
    (4, "Downtown Shelter", "321 Care Way", 1234567866, 25, 20),
    (5, "Uptown Shelter", "654 Safe Street", 1234567855, 35, 33),
]

cursor.executemany("""
INSERT INTO Shelter_Locations (locationID, locationName, address, phoneNumber, capacity, currentOccupancy)
VALUES (?, ?, ?, ?, ?, ?);
""", shelter_locations_data)

# Insert data into Donations
donations_data = [
    (1, 1, 1, 500, "2023-01-15"),
    (2, 2, 2, 300, "2023-02-20"),
    (3, 3, 3, 700, "2023-05-28")
]

# Insert data into Paycheck
paycheck_data = [
    ("2023-01-31", "S001", 160, 4000),
    ("2023-01-31", "S002", 160, 3600),
    ("2023-01-31", "S003", 160, 3200),
    ("2023-01-31", "S004", 160, 2800),
    ("2023-01-31", "S005", 160, 2400),
    ("2023-02-28", "S001", 160, 4000),
    ("2023-02-28", "S002", 160, 3600),
    ("2023-02-28", "S003", 160, 3200),
    ("2023-02-28", "S004", 160, 2800),
    ("2023-02-28", "S005", 160, 2400),
]

cursor.executemany("""
INSERT INTO Paycheck (payDate, staffID, hoursWorked, amount)
VALUES (?, ?, ?, ?);
""", paycheck_data)

# Commit the transaction and close the connection
connection.commit()
connection.close()

print("Database has been successfully created and populated!")
