# QuarterlyAssesment3

##Warnning! There are two error I can not seem to fix. 
1. You have to kill the terminal to comptly close the program. It does not just close after you close the window. I think this is besouse I do not have self.root.destroy() any where in the code. I do not have it becouse no matter where I put it, it either causes errors so the program can not run or closes everything before the quiz starts. So just make sure you also kill  the terminal along with closing the ttk windoe.
2.The number of questions is to big for the window. When the 10 question window pops up you can not see the last few questions. There is no way to scroll down and get to the rest of the questions. I have no idea on how to fix. so you cant see all the questions. Usally you can see around 7 questions but it differs on which topic/table you pick.




##QandA file- 
This file adds questions to the quiz bowl. In the database there is 5 tables ACCT, Database, AssablyProg, PythonProg, and ComputerHardWear.
Each table has 10 rows. Each row has the values question TEXT, answerOption1 TEXT, answerOption2 TEXT, answerOption3 TEXT, answerOption4 TEXT, and correctAnswer TEXT. In the file is commented out code that is a outline for how to add questions to a databse, the code used to make each table in the database and commented lines that are the questions, answeroptions and correct answers for the table. 


##read file-
This file is for me to read what questions and things are in the database. I just used the file to make sure all the values where added to the database correcly. I also used to to compare vs what was showing up in the quiz bowl. The only code in this file is to read all tables in the database and to read all values saved in each table

##QuizBowl file-
This is the only file that the user needs to access. This file runs the quiz bowl.There are two classes, QandA and TopicSelection.
 In TopicSelection there is two definitions, __init__ and topicData. The __inti__ does the window for the topic selection for the quiz. The topicData takes the info from the combox from the __inti__ and then reads in the values from that table. the vales are read in and using a for loop stored in arrays and a list. Then using another for loop it takes the values and runs the QandA class. 
In QandA class there is two definitions, __init__ and checkanswers. The __init__ does the window that with each instace, has a frame and inside that fram has the lable question, a combox that has the posstible answers a submit button to check the answer and a label that states wether the anser option choosen is correct or not. The Checkanswers def is the one that checks the user's submited answer option agenst the correct answer. If it is correct it desplays in green Correct, if incorrect then despalys Incorrect in red. 


##Tester file-
This was a file I made to test different ideas I had for how to work the Quizbowl. I started this file beocsue I wanted to try somthing crazy that would mess up everything that I had done up to that point so I made this file. It was the first pancake that you mess up so the others look good. It has the same code as the QuizBowl file but with a few more lables and print statments for error catching. 
