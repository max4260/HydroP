import sqlite3

conn = sqlite3.connect("../python/hydro.db")
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE temperates
             (device text, timestamp integer, temperature real)''')

# Create table
c.execute('''CREATE TABLE devices
             (name text, status integer, interval integer)''')
			 
# Create table
c.execute('''CREATE TABLE configurations
             (name text, value text)''')
			 
c.execute("INSERT INTO devices('name', 'status', 'interval') VALUES ('LIGHT1', 1, 5);")
conn.commit()