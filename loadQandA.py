from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Quiz Bowl")


class TopicSelection:
    def __init__(self,master, topicOptions):
        self.labIntro = ttk.Label(master, text="Welcome to the Quiz bowl")
        self.labIntro.grid()
        self.labPick = ttk.Label(master, text="Pick a topic for your quiz")
        self.labPick.grid()

        self.topicPick = ttk.Combobox(master)
        self.topicPick.config(value= topicOptions)
        self.topicPick.grid()

        self.submitButt = ttk.Button(master, text="Submit")
        self.submitButt.grid()


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
        

ListOptions = ["Python code", "Accounting basics", "Assebly code", "Computer Hardwear"]
startTopic = TopicSelection(root,ListOptions)

root.mainloop()