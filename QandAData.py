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
              (question TEXT, answerOptions LIST, correctAnswer TEXT)''')

AnswerList = ['Assets','Accounts Recivale', 'Owners Equity', 'Assistant']
AnserOpt = str(AnswerList)
curse.execute('''INSERT INTO ACCT VALUES
              ('What does Liabilty + Equity=', AnserOpt, 'Assets')
              ''')
conn.commit()




#Table 2 labled Databaase
curse.execute('''CREATE TABLE IF NOT EXISTS Database
              (question TEXT, answerOptions LIST, correctAnswer TEXT)''')





#Table 3 labled Assably Prog
curse.execute('''CREATE TABLE IF NOT EXISTS AssablyProg
              (question TEXT, answerOptions LIST, correctAnswer TEXT)''')





#Table 4 labeled PythonProg
curse.execute('''CREATE TABLE IF NOT EXISTS PythonProg
              (question TEXT, answerOptions LIST, correctAnswer TEXT)''')






#Table 5 labled ComputerHardWear
curse.execute('''CREATE TABLE IF NOT EXISTS ComputerHardWear
              (question TEXT, answerOptions LIST, correctAnswer TEXT)''')