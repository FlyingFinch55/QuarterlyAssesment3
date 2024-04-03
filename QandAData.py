import sqlite3

#Have to add all the questions one at a time 
#Between the insert and the conn.commit I will have all the questions commented

conn= sqlite3.connect('QuarterA3.db')
curse = conn.cursor()

#Code to add another question
#curse.execute('''INSERT INTO tableName VALUES
#              ('Question?','Answer Options','Correct Answer)
#              ''')


#Table 1 labled ACCT
curse.execute('''CREATE TABLE IF NOT EXISTS ACCT
              (question TEXT, answerOptions TEXT, correctAnswer TEXT)''')

AnswerList = ['Assets','Accounts Recivale', 'Owners Equity', 'Assistant']
AnserOpt = str(AnswerList)
curse.execute('''INSERT INTO ACCT VALUES
              ('What does Liabilty + Equity=', AnserOpt, 'Assets')
              ''')
conn.commit()

