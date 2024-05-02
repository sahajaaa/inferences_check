import pyodbc
import csv

# Connect to SQL Server
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=(localdb)\\local2;DATABASE=Nexturn_CE;Trusted_Connection=yes;')

cursor = conn.cursor()

# Define the path to the CSV file
csv_file = 'Mar13.csv'

# Define the SQL query to insert rows into the table
insert_query = '''
    INSERT INTO PPEDetectionTest (CameraSerial, Class, DetectionId, DetectionThreshold, 
    BoundingBoxLeft, BoundingBoxRight, BoundingBoxTop, BoundingBoxBottom, DetectionUnixEpoch, 
    DetectionDateTime, DetectionImageUrl, ModifiedBy, ModifiedDate)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''

# Open the CSV file and insert each row into the database
with open(csv_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row if exists
    for row in reader:
        row.pop(-2) 
        cursor.execute(insert_query, row)

# Commit the transaction and close the connection
conn.commit()
conn.close()