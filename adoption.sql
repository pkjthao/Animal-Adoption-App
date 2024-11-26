
CREATE TABLE Staff (
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

CREATE TABLE Adopters (
    adopterID TEXT PRIMARY KEY,
    firstName TEXT,
    lastName TEXT,
    phoneNumber INTEGER,
    email TEXT,
    address TEXT,
    password TEXT
);

CREATE TABLE Animals (
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
    reasonForIntake TEXT
);

CREATE TABLE Adoption_Requests (
    adoptionID TEXT PRIMARY KEY,
    adopterID TEXT,
    animalID INTEGER,
    dateAdopted TEXT,
    adoptionFee INTEGER,
    adoptionStatus TEXT,
    staffAdministrator TEXT,
    FOREIGN KEY (adopterID) REFERENCES Adopters(adopterID),
    FOREIGN KEY (animalID) REFERENCES Animals(animalID),
    FOREIGN KEY (staffAdministrator) REFERENCES Staff(staffID)
);

CREATE TABLE Medical_Records (
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

CREATE TABLE Shelter_Locations (
    locationID INTEGER PRIMARY KEY,
    locationName TEXT,
    address TEXT,
    phoneNumber INTEGER,
    capacity INTEGER,
    currentOccupancy INTEGER
);

CREATE TABLE Donations (
    donationID INTEGER PRIMARY KEY,
    donorID INTEGER,
    locationID INTEGER,
    amount INTEGER,
    donationDate TEXT,
    FOREIGN KEY (locationID) REFERENCES Shelter_Locations(locationID)
);

CREATE TABLE Donors (
    donorID INTEGER PRIMARY KEY,
    name TEXT,
    phoneNumber INTEGER,
    email TEXT,
    address TEXT
);

CREATE TABLE Paycheck (
    payDate TEXT,
    staffID TEXT,
    hoursWorked INTEGER,
    amount INTEGER,
    PRIMARY KEY (payDate, staffID),
    FOREIGN KEY (staffID) REFERENCES Staff(staffID)
);