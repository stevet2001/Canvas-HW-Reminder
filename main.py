import canvascalender
import quotes
import keys
import pytextnow
import time

# creates pytextnow object
client = pytextnow.Client(
    keys.user,
    sid_cookie=keys.sid,
    csrf_cookie=keys.csrf)

def getgreeting():
    #determines the greeting of the message
    currentTime = int(time.strftime('%H'))   

    if currentTime < 12 :
        return('Good morning')
    if currentTime > 12 :
        return('Good afternoon')
    if currentTime > 6 :
        return('Good evening')


def sendmessage():

    # Variable that stores the list of lists of todo assignments
    Assignments = canvascalender.assignmentdays()

    # variable that will be mutated to hold the full message
    fullmess = getgreeting() + ' ' + keys.name + ',' + r"\n" 

    # for loop that iterates as many times as their is assignments grabbing the date and name  r"\n" allows for -
    # textnow to create new blank lines
    for i in range(len(Assignments)):
        x = Assignments[i][0] +r"\n" + Assignments[i][1] 

        # addition of assignments for one string 
        if i == 0:
            fullmess = fullmess + r"\n"*2 + 'Assignments Due:' + r"\n" + x  
        fullmess = fullmess + r"\n"*2 + x 
    fullmess = fullmess + r"\n"*2

    
    # adds a quote to the full message string
    fullmess = fullmess + r"\n"*2 + quotes.getrandomquote() 

    # sends the message to the user 
    client.send_sms(keys.phone,fullmess)



#excutes message
sendmessage()