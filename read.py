import sqlite3

conn= sqlite3.connect('QuarterA3.db')
curse = conn.cursor()

curse.execute("SELECT * FROM sqlite_master WHERE type='table'")
#Reads all table
print(curse.fetchall())
print()

curse.execute("SELECT * FROM ACCT")
print(curse.fetchall())
print()