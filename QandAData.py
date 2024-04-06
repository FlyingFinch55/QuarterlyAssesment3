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


#1 ('What does Liabilty + Equity=', 'Assets','Accounts Recivale', 'Owners Equity', 'Assistant', 'Assets')
#2 ('What is the Net Income equation?', 'Owners Equity + Net Sales','Revenue - Expenses','Revenue + Expenses', 'Liabilty + Equity','Revenue - Expense')
#3 ('Does Gross Profit = Revenue - Cost of Goods Sold?', 'True','False','','','True')
#4('What is the ratio of Current Assets divided by Current Liabilities?','Equity Ratio','Current Ratio','Asset Ratio','Turnover Ratio','Current Ratio')
#5('True or False, Inventory Turnover measures how fast merchandise is sold.','True','False','','', 'True')
#6('Sales are $18,000 with a discount of $500 and returns of $1,500. What is the Net Sales?', '$1,500','$500','$18,000','$16,000','$16,000')
#7('What does COGS stand for?', 'Collection of Good Socks,','Cost of Golden Shoes','Caller of Goods Sold','Cost of Goods Sold','Cost of Goods Sold')
#8('Is cash an Asset or a Liability?', 'Asset','Liability','','','Asset')
#9('What does LIFO mean?', 'Last in First out','Lost in Financial Options','Lender in Federal operating contract','Letters in Fire Oven','Last in First out')
#10('What does FIFO mean?', 'First in First out','First in Financial Options','Fees in Federal operating contract','Flour in Fire Oven','First in First out')


#Table 2 labled Databaase
curse.execute('''CREATE TABLE IF NOT EXISTS Database
              (question TEXT, answerOption1 TEXT, answerOption2 TEXT, answerOption3 TEXT, answerOption4 TEXT, correctAnswer TEXT)''')




#1('Name the key that is the Primary Key of another entity.','Foreign Key','Compound Key','Piano Key','Skeleton Key', 'Foreign Key')
#2('Name the key that is made of more than one attribute.', 'Compound Key','Foreign Key','Pinao Key','Skeleton Key','Compound Key')
#3('True or False, the Primary Key is not a unique attribute.','True','False','','','False' )
#4('True or False, there are 3 main types of anomalies.','True','False','','','True')
#5('Relationships are made using what?','Complemt Key','Foreign Key','Emotions','Two entitys','Foreign Key')
#6('What color on the stop light method are 1 to 1 relationship?','Green','Yellow','Red','Blue','Yellow')
#7('What color on the stop light method are 1 to many relationship?','Green','Yellow','Red','Blue','Green')
#8('What color on the stop light method are many to many relationship?','Green','Yellow','Red','Blue','Red')
#9('What entity is used to clear up many to many relationships?','Intersection Entities','Clear Entities','Janitor Entities','Secondary Entities','Intersection Entities')
#10 ('How many entities are in a binary model?','1','2','3','4','2')

#Table 3 labled Assably Prog
curse.execute('''CREATE TABLE IF NOT EXISTS AssablyProg
              (question TEXT, answerOption1 TEXT, answerOption2 TEXT, answerOption3 TEXT, answerOption4 TEXT, correctAnswer TEXT)''')

curse.execute('''INSERT INTO AssablyProg VALUES
              (
              ''')
conn.commit()

#1


#Table 4 labeled PythonProg
curse.execute('''CREATE TABLE IF NOT EXISTS PythonProg
              (question TEXT, answerOption1 TEXT, answerOption2 TEXT, answerOption3 TEXT, answerOption4 TEXT, correctAnswer TEXT)''')






#Table 5 labled ComputerHardWear
curse.execute('''CREATE TABLE IF NOT EXISTS ComputerHardWear
              (question TEXT, answerOption1 TEXT, answerOption2 TEXT, answerOption3 TEXT, answerOption4 TEXT, correctAnswer TEXT)''')