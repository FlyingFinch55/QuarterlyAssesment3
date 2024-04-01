import sqlite3

#Have to add all the questions one at a time 
#Between the insert and the conn.commit I will have all the questions commented

conn= sqlite3.connect('QuarterA3.db')
curse = conn.cursor()