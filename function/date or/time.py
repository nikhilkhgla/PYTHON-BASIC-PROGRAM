function to print current date or time
def currenttime():
    import datetime
    now = datetime.datetime.now()
    print ("Current date and time : ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    
    
currenttime()
