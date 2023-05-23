import keys
from canvasapi import Canvas
from datetime import datetime, timedelta
import pandas as pd


# Canvas API URL
API_URL = 'https://sxu.instructure.com'
# Canvas API key
API_KEY = '1780~BIKkVxs7f0rLxHwTrsz2Q9DNYXzl3b6aTNbme0p4CZvPdamZSHReQ3pTgBdCZkW7'

canvas = Canvas(API_URL, API_KEY)
def getassignments():
    #gets the users todo assignments
    pendingAssigments = canvas.get_todo_items()
    #list with assignment and due date 
    lst = []
    # for loop getting every upcoming assignment
    for assignment in pendingAssigments:

        #gets the name of the assignments
        name = assignment.assignment["name"]
        
        #gets the time of assignment and subtracts five hours (canvas defaults to GMT I'm EST) - Also assignment is an object 
        # you can call various things from such as ["description"] and etc.
        due = datetime.strptime(assignment.assignment["due_at"], "%Y-%m-%dT%H:%M:%SZ") - timedelta(hours=5)

        #gets the \day of the week
        temp = pd.Timestamp(due)
        
        #adds the name, time, and day in a list of lists
        lst.append([name, temp.day_name(), str(temp)])
        
    return lst 
        



def assignmentdays():
    #stores list in a variable
    x = getassignments()
    
    #new list for clean data of assignments
    clean = []

    #for loop tho combine Datetime and week day and the name off asignment in the other index
    for i in range(len(x)):

        #creates lists of lists for ex: [2022-03-08 Tuesday, {name of assignment}]
        clean.append([x[i][2][:10] + ' ' + x[i][1], x[i][0]])

    return clean
        
