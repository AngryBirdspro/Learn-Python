import tkinter as tk
r = tk.Tk() 
r.title('Python 3 Quiz') 
r.geometry("1200x800")
r.title("Python 3 Quiz")

def title_screen():
    intro = tk.Label(r, text="""
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
----------------------------------------------------------------------------------------------------------------------
Please enter your full name that you want me to call you for the entire session down below
------------------------------------------------------------------------------------------
""", font=("Aptos", 18))
    intro.pack()
    name = tk.Entry(r)
    start = tk.Label(r, text="Welcome to the Python 3 Quiz, " + str(tk.Entry(r)) + "! Click Start when ready to start the Basics Quiz!", font=("Aptos", 18))
    name.pack(pady = 0)
    start.pack()
title_screen()

r.mainloop()