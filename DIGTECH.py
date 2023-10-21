#importations
import math
import time
#----------

#title screen--------------------------------------------------------------------------------------------------------------------------
def title_screen():
    print("""
----------------------------------------------------------------------------------------------------------------------
Welcome to the Python 3 Quiz! This quiz will test your knowledge within Python 3 and educate you to become a
Python 3 Master. You will begin with a basics quiz and if you get 100%, you can move onto the advanced quiz and if you
get all questions right on that as well, you'll be about ready to use Python 3 in the real world in IT environments.
to give you a background on Python 3, the first version of Python 3 - Python 3.0 (also called "Python 3000" or "Py3K") 
was released on December 3 2008 by Guido van Rossum. It was designed to rectify fundamental design flaws in the 
language, the changes required could not be implemented while retaining full backwards compatibility with the 2.x 
series, which necessitated a new major version number. Please type your answer for multi-choice questions in capitals
and type sentences without capitalizing letters or commas, but still include full stops and type 'T' or 'F' to answer
True/False Questions.
----------------------------------------------------------------------------------------------------------------------""")
    name = input('Please enter your full name: ')
    print("""----------------------------------------------------------------
Welcome to the Python 3 Basics Quiz,""", name + "! Get ready!", 
"""\n-------------------------------------------------------------------------
    ____        __  __                   _____    ____             _          
   / __ \__  __/ /_/ /_  ____  ____     |__  /   / __ )____ ______(_)_________
  / /_/ / / / / __/ __ \/ __ \/ __ \     /_ <   / __  / __ `/ ___/ / ___/ ___/
 / ____/ /_/ / /_/ / / / /_/ / / / /   ___/ /  / /_/ / /_/ (__  ) / /__(__  ) 
/_/    \__, /\__/_/ /_/\____/_/ /_/   /____/  /_____/\__,_/____/_/\___/____/  
      /____/                                                                                                                      
""")
#------------------------------------------------------------------------------------------------------------------------------------

#basics quiz-------------------------------------------------------------------------------------------------------------------
basics_quiz = [
["""-------------------------------------------------------------------------
What do you need to type in order for Python 3 to print a string literal?\n(A) Print('')\n(B) print()\n(C) print('')\n(D) print''\n""", "C"
, 
"""\n
--------------------------------------------------------------------------------
C will print nothing, B will give you a syntax Error, D's format is for Python 2
--------------------------------------------------------------------------------
"""
],

["""
-------------------------------------------------------------------------- 
Difference between Ctrl + D / Ctrl + C?
(A) Ctrl + C stops a process but not the prompt, Ctrl + D quits the prompt
(B) Ctrl + C quits the prompt, Ctrl + D stops a process but not the prompt
stops a process but not the prompt
(C) Nothing
--------------------------------------------------------------------------\n""", "A", 
"""\n
------------------------------------------------------------------------
There is a difference and if you answered B, it's the opposite way round
------------------------------------------------------------------------
"""],

["""
---------------------------------------------------------------------------------------------------------------
True/False: The 4 basic data types in Python are 'strings', 'floats', 'integers', and 'Boolean(True/False)'
---------------------------------------------------------------------------------------------------------------\n
""", "True", 
"""\n
--------------------------------------
Great try. You'll get it next time! :)
--------------------------------------
"""],

["""
---------------------------------------------------------------------------------------------------------------
True/False: If you set this variable: current_time = 12, and then type under it: print(current_Time) it will
print the number 12
---------------------------------------------------------------------------------------------------------------\n
""", "False", 
"""\n
-------------------------------------------------------------------------------------------------------------------------
It will give you an error saying current_Time is not defined because it's not, but great try. You'll get it next time! :)
-------------------------------------------------------------------------------------------------------------------------
"""],
["""
------------------------------------------------
What does this symbol do? '+'
(A) Literally adds 2 things together
(B) Literally subtracts one thing from the other
(C) Literally multiplys 2 things together
(D) Literally divides one thing from the other
------------------------------------------------
""", "A", 
"""
-------------------
Did you fail maths?
-------------------
"""

],

[
"""
------------------------------------------------
What does this symbol do? '/'
(A) Literally adds 2 things together
(B) Literally subtracts one thing from the other
(C) Literally multiplys 2 things together
(D) Literally divides one thing from the other
------------------------------------------------
""", "D", 
"""
------------------------------------
'/' replaces the division symbol '÷'
------------------------------------
"""
],

[
"""
------------------------------------------------
What does this symbol do? '*'
(A) Literally adds 2 things together
(B) Literally subtracts one thing from the other
(C) Literally multiplys 2 things together
(D) Literally divides one thing from the other
------------------------------------------------
""", "C", 
"""
--------------------------------
'*' replaces the multiply symbol
--------------------------------
"""
],

[
"""
------------------------------------------------
What does this symbol do? '-'
(A) Literally adds 2 things together
(B) Literally subtracts one thing from the other
(C) Literally multiplys 2 things together
(D) Literally divides one thing from the other
------------------------------------------------
""", "B", 
"""
-------------------
Did you fail maths?
-------------------
"""
],

[
"""
------------------------------------------------
What does this symbol do? '**'
(A) Literally adds 2 things together
(B) 'To the power of'
(C) Literally multiplys 2 things together
(D) Literally divides one thing from the other
------------------------------------------------
""", "B", 
"""
----------------------------------
'x ** y' means x to the power of y
----------------------------------
"""
],

[
"""
----------------------------------------------------------
True/False: There's no difference between lists and tuples
----------------------------------------------------------
""", "False", "Lists are mutable but tuples aren't"
],

[
"""
-----------------------------------------------
True/False: Is there another way to write this:
print("What is your name?")
name = input()
print(name)
-----------------------------------------------
""", "True", 
"""
---------------------------------
name = input("What is your name?)
print(name)
---------------------------------
"""
],

[
"""
------------------------------------------
What's the difference between "==" and "="
(A) Nothing
(B) "==" is not a valid syntax in python language
(C) "=" assigns values into a variable while "==" check to see if something is equal to another
(D) "=" check to see if something is equal to another  "==" assigns values into a variable while
------------------------------------------
""", "C", """
------------------------------------------------------------------------
"=="" is a valid syntax and if you picked D, it's the opposite way round
------------------------------------------------------------------------
"""
],

[
"""
----------------------------------------------------------------------------------------------------------------------------
What is a "for" loop?
(A) A control flow statement that's used to execute statements as long as the conditions are met that's also known as an it
(B) Nothing
(C) A control flow statement that's used to exeute statements even if the statements are not met
----------------------------------------------------------------------------------------------------------------------------
""", "A", """
----------------------
It's the opposite of C
----------------------
"""
],

[
"""
----------------------------------------------------------------------------------------------------------------------------
What is a "while" loop?
(A) Does the same as a for loop
(B) A control flow statement that's used to exeute statements even if the statements are not met
(C) Nothing
----------------------------------------------------------------------------------------------------------------------------
""", "A", """
---------------------------------------------------------------------------------------------------------------------
The only difference a while loop has with a for loop is that a for loop is used on things like tuples and lists while
a while loop doesn't to be directly used on something, it can just be something like while True:
---------------------------------------------------------------------------------------------------------------------
"""
]
]
#------------------------------------------------------------------------------------------------------------------------------------

#advanced quiz----------------------------------------------------------------------------------------------------------------
advanced_quiz = [

]
#-----------------------------------------------------------------------------------------------------------------------------

# only used to check question count------------------------
print(len(basics_quiz))
#print(len(advanced_quiz))
#----------------------------------------------------------

#Main code--------------------------------------------------------------------------------------------------------------------
def run_quizzes():
    score = 0
    title_screen()
    time.sleep(5)
    for x in basics_quiz:
        answer = input(x[0])
        if answer == x[1]:
            print("""\n
   ______                          __  __   _       __     ____   ____                   __
  / ____/___  _____________  _____/ /_/ /  | |     / /__  / / /  / __ \____  ____  ___  / /
 / /   / __ \/ ___/ ___/ _ \/ ___/ __/ /   | | /| / / _ \/ / /  / / / / __ \/ __ \/ _ \/ / 
/ /___/ /_/ / /  / /  /  __/ /__/ /_/_/    | |/ |/ /  __/ / /  / /_/ / /_/ / / / /  __/_/  
\____/\____/_/  /_/   \___/\___/\__(_)     |__/|__/\___/_/_/  /_____/\____/_/ /_/\___(_)   
                                                                                           
""")
            time.sleep(1.5)
            score+=1
        else:
            print(x[2])
            time.sleep(2.5)
    print(score / len(basics_quiz) * 100, "%")
    time.sleep(5)
run_quizzes()
#-------------------------------------------------------------------------------------------------------------------------------