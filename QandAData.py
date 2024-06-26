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


#1('What does LDR stand for?','Loud','Load','Live','Little','Load')
#2('What does STR stand for?','Standard','Stall','Store','Still','Store')
#3('What does MOV stand for?','Commove','Amove','Movies','Move','Move')
#4('What size is DCD?','word','bite','byte','half-word','word')
#5('What size is DCW?','word','bite','byte','half-word','half-word')
#6('What size is DCB?','word','bite','byte','half-word','byte')
#7('True or False ENDP ends the program.','True','False','','','True')
#8('True or False, Array1 DCD 0, 0, 0, 0 makes an array of words all values 0.','True','False','','','True')
#9('What does 0011 + 0010 equal?','0000','1111','1010','0101','0101')
#10('What does 0100 + 0011 equal?','0000','1111','0111','1000','0111')


#Table 4 labeled PythonProg
curse.execute('''CREATE TABLE IF NOT EXISTS PythonProg
              (question TEXT, answerOption1 TEXT, answerOption2 TEXT, answerOption3 TEXT, answerOption4 TEXT, correctAnswer TEXT)''')


#1('What is the extension for a Python file?','.py','.db','.c','.exe','.py')
#2('What is the extension for a Database file?','.py','.db','.c','.exe','.db')
#3('What is the variable type for strings?','int','str','float','bool','str')
#4('What is the variable type for integers?','int','str','float','bool','int')
#5('What is the variable type for real numbers?','int','str','float','bool','float')
#6('What is the variable type for booleans?','int','str','float','bool','bool')
#7('What type of variable does print("55") print?','int','str','float','bool','str')
#8('What type of variable does print(55) print?','int','str','float','bool','int')
#9('What symbol is used to comment a line?','*','//','comment','#','#')
#10('What does print("5"+"5") print?','55','10','25','55555','55')


#Table 5 labled ComputerHardWear
curse.execute('''CREATE TABLE IF NOT EXISTS ComputerHardWear
              (question TEXT, answerOption1 TEXT, answerOption2 TEXT, answerOption3 TEXT, answerOption4 TEXT, correctAnswer TEXT)''')


#1('What does OS stand for?','Operating system','Oh Sh**','Operating segment','Off-Cycle system','Operating system')
#2('What does CPU stand for?','Central Popcorn unit','Chocolate processimg untensils','Central processing unit','Copper polar use','Central processing unit')
#3('What does RAM stand for?','A male sheep','Random Access Memory','Raw Access Memory','Random Accounting Memo','Random Access Memory')
#4('Is a keyboard an input or output device?','input','output','','','input')
#5('Is a speaker an input or output device?','input','output','','','output')
#6('True or False, Windows is an OS.','True','False','','','True')
#7('True or False, Bing is an OS.','True','False','','','False')
#8('What does SaaS stand for?','Software as a Service','Sweet as a Sugar','Self as a Service','Software as a Salad','Software as a Service')
#9('What does Paas stand for?','Platform as a Service','Popcore as a Service','Platform as a Sandwitch','Penguin as a Shark','Platform as a Service')
#10('What does SSD stand for?','Soild State Drive','Sweet Savory Dip','State Soild Drive','Software Sold Data','Soild State Drive')
