
CREATE TABLE IF NOT EXISTS Staff (
    staffID TEXT PRIMARY KEY,
    firstName TEXT,
    lastName TEXT,
    position TEXT,
    phoneNumber INTEGER,
    email TEXT,
    hireDate TEXT,
    salary INTEGER,
    workLocation INTEGER,
    status TEXT,
    password TEXT
);

CREATE TABLE IF NOT EXISTS Adopters (
    adopterID TEXT PRIMARY KEY,
    firstName TEXT,
    lastName TEXT,
    phoneNumber INTEGER,
    email TEXT,
    address TEXT,
    password TEXT
);

CREATE TABLE IF NOT EXISTS Animals (
    animalID INTEGER PRIMARY KEY,
    name TEXT,
    species TEXT,
    breed TEXT,
    age INTEGER,
    gender TEXT,
    dateOfArrival TEXT,
    adoptedOrNot INTEGER,
    healthStatus TEXT,
    description TEXT,
    locationID INTEGER,
    reasonForIntake TEXT,
    adoptionFee INTEGER
);

CREATE TABLE IF NOT EXISTS Adoption_Requests (
    adoptionID TEXT PRIMARY KEY,
    adopterID TEXT,
    animalID INTEGER,
    dateAdopted TEXT,
    adoptionStatus TEXT,
    staffAdministrator TEXT,
    FOREIGN KEY (adopterID) REFERENCES Adopters(adopterID),
    FOREIGN KEY (animalID) REFERENCES Animals(animalID),
    FOREIGN KEY (staffAdministrator) REFERENCES Staff(staffID)
);

CREATE TABLE IF NOT EXISTS Medical_Records (
    medicalID INTEGER PRIMARY KEY,
    animalID INTEGER,
    staffID TEXT,
    diagnosis TEXT,
    treatment TEXT,
    date TEXT,
    note TEXT,
    FOREIGN KEY (animalID) REFERENCES Animals(animalID),
    FOREIGN KEY (staffID) REFERENCES Staff(staffID)
);

CREATE TABLE IF NOT EXISTS Shelter_Locations (
    locationID INTEGER PRIMARY KEY,
    locationName TEXT,
    address TEXT,
    phoneNumber INTEGER,
    capacity INTEGER,
    currentOccupancy INTEGER,
    funds INTEGER
);

CREATE TABLE IF NOT EXISTS Donations (
    donationID INTEGER PRIMARY KEY,
    locationID INTEGER,
    amount INTEGER,
    donationDate TEXT,
    donorName TEXT,
    donorPhoneNumber INTEGER,
    donorEmail TEXT,
    donorAddress TEXT,
    FOREIGN KEY (locationID) REFERENCES Shelter_Locations(locationID)
);

CREATE TABLE IF NOT EXISTS Paycheck (
    payDate TEXT,
    staffID TEXT,
    hoursWorked INTEGER,
    amount INTEGER,
    PRIMARY KEY (payDate, staffID),
    FOREIGN KEY (staffID) REFERENCES Staff(staffID)
);