#Created by Austin Wilson
#only for the database creation and debugs.
#not intended for real life use. dont do it, or do it. i dont really care.
import sqlite3 as sql
#Connect to db as ASDB (ArtShackDataBase
ASDB=sql.connect("ArtShack.db")
#Call cursor function
cur=ASDB.cursor()

'''
Database connected above, SQL tomfoolery below

table name: art
art format as follows
Bool approved (True or False)
string  art (.jpg or .png file)
float price(starting price)
string type (Auction or buy it now (BIN) )
'''
#Checks if db exists
res=cur.execute("SELECT name FROM sqlite_master WHERE name='art'")
if(res.fetchone() is not None):
    print("DB exists. no action needed")

    
else:

    print("DB not found, creating one and populating with sample art")
    cur.execute("CREATE TABLE art(approved BOOLEAN, art TEXT, price REAL, type TEXT)")
    
    sampleart=[
        (True,'art1.png',50.0,'Auction'),
        (False,'art2.png',10.0,'BIN'),
        (True,'art3.jpg',120.0,'Auction')
        ]
    cur.executemany("INSERT INTO art VALUES (?,?,?,?)",sampleart)
    ASDB.commit()




#Prints every table for debug purposes
print("\nThe following tables are in the system")
res=cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables=res.fetchall()
for x in tables:
    print(x[0])

#Prints the entries for debug purposes
print("\nthe following entries are in the 'art' table")
res= cur.execute("SELECT * FROM art")
entries= res.fetchall()
for x in entries:
    print(x)
ASDB.commit()
