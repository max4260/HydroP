import sqlite3

conn = sqlite3.connect("../python/hydro.db")
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE temperatures
             (device text, timestamp integer, temperature real)''')

# Create table
c.execute('''CREATE TABLE devices
             (name text, status integer, interval integer)''')
			 
# Create table
c.execute('''CREATE TABLE configurations
             (name text, value text)''')
			 
c.execute("INSERT INTO devices('name', 'status', 'interval') VALUES ('LIGHT1', 0, 5);")
c.execute("INSERT INTO devices('name', 'status', 'interval') VALUES ('TEMP1', 0, 5);")
c.execute("INSERT INTO devices('name', 'status', 'interval') VALUES ('TEMP2', 0, 5);")
c.execute("INSERT INTO devices('name', 'status', 'interval') VALUES ('TEMP3', 0, 5);")
c.execute("INSERT INTO devices('name', 'status', 'interval') VALUES ('TEMP4', 0, 5);")
conn.commit()