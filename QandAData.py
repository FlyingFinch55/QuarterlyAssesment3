import sqlite3

#Have to add all the questions one at a time 
#Between the insert and the conn.commit I will have all the questions commented

conn= sqlite3.connect('QuarterA3.db')
curse = conn.cursor()

#Code to add another question
#curse.execute('''INSERT INTO tableName VALUES
#              ('Question?','AnswerOption 1', 'AnswerOption 2', 'AnswerOption 3', 'AnswerOption 4', 'CorrectAnswer)
#              ''')
#conn.commit()
#Meger options 1-4 into a list 

#Table 1 labled ACCT
curse.execute('''CREATE TABLE IF NOT EXISTS ACCT
              (question TEXT, answerOption1 TEXT, answerOption2 TEXT, answerOption3 TEXT, answerOption4 TEXT, correctAnswer TEXT)''')


curse.execute('''INSERT INTO ACCT VALUES
              ('What is the Net Income equation?', 'Owners Equity + Net Sales','Revenue - Expenses','Revenue + Expenses', 'Liabilty + Equity','Revenue - Expense')
              ''')
conn.commit()

#1 ('What does Liabilty + Equity=', 'Assets','Accounts Recivale', 'Owners Equity', 'Assistant', 'Assets')
#2 ('What is the Net Income equation?', 'Owners Equity + Net Sales','Revenue - Expenses','Revenue + Expenses', 'Liabilty + Equity','Revenue - Expense')
#3


#Table 2 labled Databaase
curse.execute('''CREATE TABLE IF NOT EXISTS Database
              (question TEXT, answerOption1 TEXT, answerOption2 TEXT, answerOption3 TEXT, answerOption4 TEXT, correctAnswer TEXT)''')





#Table 3 labled Assably Prog
curse.execute('''CREATE TABLE IF NOT EXISTS AssablyProg
              (question TEXT, answerOption1 TEXT, answerOption2 TEXT, answerOption3 TEXT, answerOption4 TEXT, correctAnswer TEXT)''')





#Table 4 labeled PythonProg
curse.execute('''CREATE TABLE IF NOT EXISTS PythonProg
              (question TEXT, answerOption1 TEXT, answerOption2 TEXT, answerOption3 TEXT, answerOption4 TEXT, correctAnswer TEXT)''')






#Table 5 labled ComputerHardWear
curse.execute('''CREATE TABLE IF NOT EXISTS ComputerHardWear
              (question TEXT, answerOption1 TEXT, answerOption2 TEXT, answerOption3 TEXT, answerOption4 TEXT, correctAnswer TEXT)''')