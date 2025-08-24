import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('MNC.db')
cursor = connection.cursor()

# Use executescript for multiple SQL statements
cursor.executescript('''
------------------------------------------------
-- Master table: MNC Information
------------------------------------------------
CREATE TABLE IF NOT EXISTS MNC (
    mnc_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    headquarters TEXT,
    founded_year INTEGER,
    industry TEXT,
    revenue_billion REAL
);

INSERT INTO MNC (name, headquarters, founded_year, industry, revenue_billion)
VALUES ('GlobalTech Corp', 'New York, USA', 1985, 'Information Technology', 120.50);

------------------------------------------------
-- Regions Table
------------------------------------------------
CREATE TABLE IF NOT EXISTS Regions (
    region_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mnc_id INTEGER,
    region_name TEXT,
    head_office TEXT,
    FOREIGN KEY (mnc_id) REFERENCES MNC(mnc_id)
);

INSERT INTO Regions (mnc_id, region_name, head_office)
VALUES 
(1, 'North America', 'New York, USA'),
(1, 'Europe', 'Berlin, Germany'),
(1, 'Asia-Pacific', 'Singapore'),
(1, 'India', 'Bengaluru, India');

------------------------------------------------
-- Organizations in North America
------------------------------------------------
CREATE TABLE IF NOT EXISTS NorthAmerica_Organizations (
    org_id INTEGER PRIMARY KEY AUTOINCREMENT,
    region_id INTEGER,
    org_name TEXT,
    location TEXT,
    established_year INTEGER,
    num_employees INTEGER,
    FOREIGN KEY (region_id) REFERENCES Regions(region_id)
);

INSERT INTO NorthAmerica_Organizations (region_id, org_name, location, established_year, num_employees)
VALUES
(1, 'GlobalTech US Headquarters', 'New York, USA', 1985, 8000),
(1, 'GlobalTech Canada Ltd', 'Toronto, Canada', 2000, 3000);

------------------------------------------------
-- Organizations in Europe
------------------------------------------------
CREATE TABLE IF NOT EXISTS Europe_Organizations (
    org_id INTEGER PRIMARY KEY AUTOINCREMENT,
    region_id INTEGER,
    org_name TEXT,
    location TEXT,
    established_year INTEGER,
    num_employees INTEGER,
    FOREIGN KEY (region_id) REFERENCES Regions(region_id)
);

INSERT INTO Europe_Organizations (region_id, org_name, location, established_year, num_employees)
VALUES
(2, 'GlobalTech Europe GmbH', 'Berlin, Germany', 1998, 4000),
(2, 'GlobalTech UK Ltd', 'London, UK', 2005, 2500),
(2, 'GlobalTech France SARL', 'Paris, France', 2010, 2000);

------------------------------------------------
-- Organizations in Asia-Pacific
------------------------------------------------
CREATE TABLE IF NOT EXISTS AsiaPacific_Organizations (
    org_id INTEGER PRIMARY KEY AUTOINCREMENT,
    region_id INTEGER,
    org_name TEXT,
    location TEXT,
    established_year INTEGER,
    num_employees INTEGER,
    FOREIGN KEY (region_id) REFERENCES Regions(region_id)
);

INSERT INTO AsiaPacific_Organizations (region_id, org_name, location, established_year, num_employees)
VALUES
(3, 'GlobalTech Singapore Pte Ltd', 'Singapore', 2001, 3500),
(3, 'GlobalTech Australia Pty Ltd', 'Sydney, Australia', 2008, 2800),
(3, 'GlobalTech Japan KK', 'Tokyo, Japan', 2012, 2200);

------------------------------------------------
-- Organizations in India
------------------------------------------------
CREATE TABLE IF NOT EXISTS India_Organizations (
    org_id INTEGER PRIMARY KEY AUTOINCREMENT,
    region_id INTEGER,
    org_name TEXT,
    location TEXT,
    established_year INTEGER,
    num_employees INTEGER,
    FOREIGN KEY (region_id) REFERENCES Regions(region_id)
);

INSERT INTO India_Organizations (region_id, org_name, location, established_year, num_employees)
VALUES
(4, 'GlobalTech Solutions India Pvt Ltd', 'Bengaluru, Karnataka', 2002, 5000),
(4, 'GlobalTech Research Labs', 'Hyderabad, Telangana', 2010, 2000),
(4, 'GlobalTech Customer Support', 'Chennai, Tamil Nadu', 2015, 3000);

------------------------------------------------
-- Employees Table
------------------------------------------------
CREATE TABLE IF NOT EXISTS Employees (
    emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    region_id INTEGER,
    org_id INTEGER,
    org_table TEXT,
    name TEXT,
    gender CHAR(1),
    designation TEXT,
    department TEXT,
    salary REAL,
    join_date TEXT,
    hire_type TEXT CHECK(hire_type IN ('Full-Time', 'Contract', 'Intern')),
    performance_rating REAL,
    bonus REAL,
    FOREIGN KEY (region_id) REFERENCES Regions(region_id)
);

INSERT INTO Employees (region_id, org_id, org_table, name, gender, designation, department, salary, join_date, hire_type, performance_rating, bonus)
VALUES
(1, 1, 'NorthAmerica_Organizations', 'John Miller', 'M', 'Director', 'Management', 200000, '2010-03-12', 'Full-Time', 4.8, 25000),
(1, 2, 'NorthAmerica_Organizations', 'Sophia Lee', 'F', 'Software Engineer', 'Development', 120000, '2019-07-22', 'Full-Time', 4.5, 10000),
(2, 1, 'Europe_Organizations', 'Hans Schmidt', 'M', 'Project Manager', 'Operations', 95000, '2016-02-15', 'Full-Time', 4.2, 8000),
(2, 3, 'Europe_Organizations', 'Claire Dubois', 'F', 'Data Scientist', 'Research', 85000, '2020-11-01', 'Contract', 4.7, 7000),
(3, 1, 'AsiaPacific_Organizations', 'Kenji Tanaka', 'M', 'AI Engineer', 'Research', 110000, '2018-08-19', 'Full-Time', 4.6, 12000),
(3, 2, 'AsiaPacific_Organizations', 'Emily Brown', 'F', 'Business Analyst', 'Sales', 75000, '2021-04-11', 'Intern', 4.1, 2000),
(4, 1, 'India_Organizations', 'Ravi Kumar', 'M', 'Senior Engineer', 'Development', 1200000, '2018-06-15', 'Full-Time', 4.5, 150000),
(4, 2, 'India_Organizations', 'Ananya Sharma', 'F', 'Data Scientist', 'Research', 1500000, '2020-01-10', 'Full-Time', 4.9, 200000),
(4, 3, 'India_Organizations', 'Vikram Singh', 'M', 'Manager', 'Customer Support', 900000, '2019-11-01', 'Contract', 4.0, 50000);

------------------------------------------------
-- Sales Table
------------------------------------------------
CREATE TABLE IF NOT EXISTS Sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    region_id INTEGER,
    org_id INTEGER,
    org_table TEXT,
    year INTEGER,
    revenue_million REAL,
    profit_million REAL,
    customer_count INTEGER,
    yoy_growth_percent REAL,
    FOREIGN KEY (region_id) REFERENCES Regions(region_id)
);

INSERT INTO Sales (region_id, org_id, org_table, year, revenue_million, profit_million, customer_count, yoy_growth_percent)
VALUES
(1, 1, 'NorthAmerica_Organizations', 2023, 1200.50, 400.25, 15000, 6.5),
(1, 2, 'NorthAmerica_Organizations', 2023, 650.20, 210.30, 8000, 5.2),
(2, 1, 'Europe_Organizations', 2023, 900.10, 280.40, 12000, 4.8),
(2, 2, 'Europe_Organizations', 2023, 720.60, 190.50, 9500, 5.5),
(2, 3, 'Europe_Organizations', 2023, 550.75, 160.20, 7000, 6.0),
(3, 1, 'AsiaPacific_Organizations', 2023, 800.30, 240.15, 11000, 5.9),
(3, 2, 'AsiaPacific_Organizations', 2023, 600.45, 170.20, 9000, 4.6),
(3, 3, 'AsiaPacific_Organizations', 2023, 480.75, 150.10, 6500, 4.2),
(4, 1, 'India_Organizations', 2023, 540.60, 130.10, 7000, 7.5),
(4, 2, 'India_Organizations', 2023, 350.20, 95.15, 4500, 6.8),
(4, 3, 'India_Organizations', 2023, 250.75, 72.35, 3200, 6.2);
''')

# Query the MNC table
cursor.execute('SELECT * FROM Sales')
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.commit()
connection.close()
