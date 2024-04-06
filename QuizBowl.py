from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()
root.title("Quiz Bowl")

conn= sqlite3.connect('QuarterA3.db')
curse = conn.cursor()


class TopicSelection():
    #def __init__(self, *args):
        #super().__init__(*args)
        
        #self.MainScreen(root, ListOptions)

    def __init__(self,master, topicOptions):

        self.labPick = ttk.Label(master, text="Pick a topic for your quiz")
        self.labPick.grid()

        self.topicPick = ttk.Combobox(master)
        self.topicPick.config(value= topicOptions)
        self.topicPick.grid()

        self.submitButt = ttk.Button(master, text="Submit")
        self.submitButt.config(command= self.RunQuiz())
        self.submitButt.grid()
    
    def RunQuiz(self):
        print("Submit button work")
        Table = self.topicPick.get()
        print(Table)
        if Table == "Accounting basics":
           curse.execute("SELECT * FROM ACCT")
           print(curse.fetchall())
           print()
        #for question in Table:
            #quizbowler = QandA(question, answeroptions,correctAnswer)

        if Table == "Database":
            curse.execute("SELECT * FROM Database")
            print(curse.fetchall())
            print()

        if Table == "Assebly code":
            curse.execute("SELECT * FROM AssablyProg")
            print(curse.fetchall())
            print()

        if Table == "Python code":
            curse.execute("SELECT * FROM PythonProg")
            print(curse.fetchall())
            print()

        if Table == "Computer Hardwear":
            curse.execute("SELECT * FROM ComputerHardWear")
            print(curse.fetchall())
            print()




class QandA:
    def __init__(self,master,strQuestion,listAnswers, correctAns):
        self.correctAnswer=correctAns

        self.frameQA = ttk.Frame(master, relief='raised',padding=(5,5))
        self.frameQA.grid()
        
        self.lab1 = ttk.Label(self.frameQA, text=strQuestion)
        self.lab1.grid()
        
        self.answerOpt = ttk.Combobox(self.frameQA)
        self.answerOpt.grid()
        self.answerOpt.config(values=listAnswers)

        
        self.testButt = ttk.Button(self.frameQA, text="Submit",command=self.checkAnswe)
        self.testButt.grid()

        self.feedLable = ttk.Label(self.frameQA)
        self.feedLable.grid()

    def checkAnswe(self):
        if self.answerOpt.get() == self.correctAnswer:
            self.feedLable.config(text="Correct",foreground="green")
        else:
            self.feedLable.config(text="Incorrect", foreground="red")
        

ListTester = ["Yes","No","Maybe","Try again later"]
ListOptions = ["Python code", "Accounting basics", "Assebly code", "Computer Hardwear", "Database"]
startTopic = TopicSelection(root,ListOptions)
testQandA = QandA(root,"Is this working?",ListTester,"Yes")

root.mainloop()