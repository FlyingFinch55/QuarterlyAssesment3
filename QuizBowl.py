from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()
root.title("Quiz Bowl")

conn= sqlite3.connect('QuarterA3.db')
curse = conn.cursor()


class TopicSelection():
    def __init__(self,master, topicOptions):

        self.labPick = ttk.Label(master, text="Pick a topic for your quiz")
        self.labPick.grid()

        self.topicPick = ttk.Combobox(master)
        self.topicPick.config(value= topicOptions)
        self.topicPick.grid()
        self.quizTopic =  self.topicPick.get()

        self.submitButt = ttk.Button(master, text="Submit")
        self.submitButt.config(command= self.TopicChosen())
        self.submitButt.grid()
    
    def TopicChosen(self):
        if self.topicPick.get() == ListOptions[0]: #Python
            curse.execute("SELECT * FROM PythonProg")
            rows = curse.fetchall()
            questions_and_options_list = []
            for row in rows:
                question = row[0]
                correct_answer = row[5]
                answer_options = (row[1], row[2], row[3], row[4])
                questions_and_options_list.append((question, correct_answer, answer_options))
            for question in questions_and_options_list:
                ques = QandA(root, question[0],answer_options,correct_answer)


        if self.topicPick.get() == ListOptions[4]: #Database
            curse.execute("SELECT * FROM Database")
            rows = curse.fetchall()
            questions_and_options_list = []
            for row in rows:
                question = row[0]
                correct_answer = row[5]
                answer_options = (row[1], row[2], row[3], row[4])
                questions_and_options_list.append((question, correct_answer, answer_options))
            for question in questions_and_options_list:
                ques = QandA(root, question[0],answer_options,correct_answer)

        if self.topicPick.get() == ListOptions[1]: #ACCT
            curse.execute("SELECT * FROM ACCT")
            rows = curse.fetchall()
            questions_and_options_list = []
            for row in rows:
                question = row[0]
                correct_answer = row[5]
                answer_options = (row[1], row[2], row[3], row[4])
                questions_and_options_list.append((question, correct_answer, answer_options))
            for question in questions_and_options_list:
                ques = QandA(root, question[0],answer_options,correct_answer)


        if self.topicPick.get() == ListOptions[2]: #Assably
            curse.execute("SELECT * FROM AssablyProg")
            rows = curse.fetchall()
            questions_and_options_list = []
            for row in rows:
                question = row[0]
                correct_answer = row[5]
                answer_options = (row[1], row[2], row[3], row[4])
                questions_and_options_list.append((question, correct_answer, answer_options))
            for question in questions_and_options_list:
                ques = QandA(root, question[0],answer_options,correct_answer)

        if self.topicPick.get() == ListOptions[3]: #ComputerHardware
           curse.execute("SELECT * FROM ComputerHardWear")
           rows = curse.fetchall()
           questions_and_options_list = []
           for row in rows:
                question = row[0]
                correct_answer = row[5]
                answer_options = (row[1], row[2], row[3], row[4])
                questions_and_options_list.append((question, correct_answer, answer_options))
           for question in questions_and_options_list:
                ques = QandA(root, question[0],answer_options,correct_answer)         



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
        


ListOptions = ["Python code", "Accounting basics", "Assebly code", "Computer Hardwear", "Database"]
startTopic = TopicSelection(root,ListOptions)


root.mainloop()