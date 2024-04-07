from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3

root = Tk()
root.title("Quiz Bowl")

conn= sqlite3.connect('QuarterA3.db')
curse = conn.cursor()


class TopicSelection:


    def __init__(self,root, topicOptions):
        self.root = root
        self.root.title("Topic Selection")

        self.labPick = ttk.Label(self.root, text="Pick a topic for your quiz")
        self.labPick.grid()

        self.topicPick = ttk.Combobox(self.root)
        self.topicPick.config(value= topicOptions)
        self.topicPick.grid()

        self.submitButt = ttk.Button(self.root, text="Start Quiz")
        self.submitButt.config(command= self.topicData)
        self.submitButt.grid()

        


    def topicData(self):
        self.root.withdraw()
        self.q_and_a_window = tk.Toplevel(self.root)
        
        if self.topicPick.get() == ListOptions[0]:
            curse.execute("SELECT * FROM PythonProg")
            rows = curse.fetchall()
            questions_and_options_list = []
            for row in rows:
                question = row[0]
                correct_answer = row[5]
                answer_options = (row[1], row[2], row[3], row[4])
                questions_and_options_list.append((question, correct_answer, answer_options))
            for question, correct_answer,answer_options in questions_and_options_list:
                QandA(self.q_and_a_window, question,answer_options,correct_answer)
            
            

        if self.topicPick.get() == ListOptions[4]:
            curse.execute("SELECT * FROM Database")
            rows = curse.fetchall()
            questions_and_options_list = []
            for row in rows:
                question = row[0]
                correct_answer = row[5]
                answer_options = (row[1], row[2], row[3], row[4])
                questions_and_options_list.append((question, correct_answer, answer_options))
            for question, correct_answer,answer_options in questions_and_options_list:
                QandA(self.q_and_a_window, question,answer_options,correct_answer)
           

        if self.topicPick.get() == ListOptions[1]:
            curse.execute("SELECT * FROM ACCT")
            rows = curse.fetchall()
            questions_and_options_list = []
            for row in rows:
                question = row[0]
                correct_answer = row[5]
                answer_options = (row[1], row[2], row[3], row[4])
                questions_and_options_list.append((question, correct_answer, answer_options))
            for question, correct_answer,answer_options in questions_and_options_list:
                QandA(self.q_and_a_window, question,answer_options,correct_answer)
            

        if self.topicPick.get() == ListOptions[2]:
            curse.execute("SELECT * FROM AssablyProg")
            rows = curse.fetchall()
            questions_and_options_list = []
            for row in rows:
                question = row[0]
                correct_answer = row[5]
                answer_options = (row[1], row[2], row[3], row[4])
                questions_and_options_list.append((question, correct_answer, answer_options))
            for question, correct_answer,answer_options in questions_and_options_list:
                QandA(self.q_and_a_window, question,answer_options,correct_answer)

        if self.topicPick.get() == ListOptions[3]:
            curse.execute("SELECT * FROM ComputerHardWear")
            rows = curse.fetchall()
            questions_and_options_list = []
            for row in rows:
                question = row[0]
                correct_answer = row[5]
                answer_options = (row[1], row[2], row[3], row[4])
                questions_and_options_list.append((question, correct_answer, answer_options))
            for question, correct_answer,answer_options in questions_and_options_list:
                QandA(self.q_and_a_window, question,answer_options,correct_answer)
        


class QandA:
    def __init__(self,root,strQuestion,listAnswers, correctAns):
        self.root = root
        self.root.title("Quiz Questions")

        self.correctAnswer=correctAns

        self.frameQA = ttk.Frame(self.root, relief='raised',padding=(5,5))
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
TestStart = TopicSelection(root,ListOptions)




root.mainloop()