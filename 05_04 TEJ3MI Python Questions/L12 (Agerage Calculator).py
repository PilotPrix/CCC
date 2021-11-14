  # Grade Calculator/interpreter
nInput = 0
n = 0
t = 0

  # makes the users repeat certain messages n (nTimes) amount of times
def UserRepeat(sMessage, nTimes):
    if(nTimes == 0):                                                            # Case 1: n = 0, do nothing
        return
    elif(nTimes == 1):                                                          # Case 2: say once
        while(input("Please type \"" + str(sMessage) + "\"\n").lower() != sMessage.lower()):  # repeat until user says desired message
            pass    # do nothing
    elif(nTimes > 1):                                                           # Case 3: say multiple times
        print("Please type \"" + str(sMessage) + "\" " + str(nTimes) + " times")    # print "please say 'message' n times"
        for i in range (nTimes, 0, -1):                                             # repeat while loop n times
            while(input(str(i) + " more times: ").lower() != sMessage.lower()):     # while loop keeps looping until user says desired message
                pass    # lower() used so it's not case sensitive



print("This program will help you calculate your average grade and " +
      "see how well you're doing in school\n(After entering your list, type in \"0\" to finish)")

  # Input process (Continuously ask the user for numbers)
while True:
    nInput = int(input("Type in your grades here: "))
    if nInput == 0:     # end input process when user enters "0"
        break
    n += nInput         # n = the sum of the grades
    t += 1              # amount of numbers

  # print the average
average = round(n / t, 2)
print("\nYour average is " + str(average))


  # Interpret and judge the user's grades
if(average > 100):
    print("stop lying, and refain from hacking this program. " +
          "You won't look good when confronted this at the Pearly Gates of Heaven")
elif(average >= 98):
    print("there's no way, god level splendid genius s plus max pro ultra super human\n")
    UserRepeat("I'm working too hard", 3)  # make user repeat "I'm working too hard" 3 times
elif(average >= 97):
    print("Congradulations on your hard work! You've accomplished a great deal of academic performance, " +
          "you got a super high chance of making it into University of Waterloo")
elif(average >= 95):
    print("Wonderful! getting into the mid ninetys is definitely tough work, see if you can make it to 97\n")
    UserRepeat("I am going to work harder in math", 1)
elif(average >= 93):
    print("Great!\n")
    UserRepeat("I am going to do better in math", 3)
elif(average >=  90):
    print("Not bad, keep up your momentum")
elif(average >= 80):
    print("You will need more work if you want to get into Ivy leage Universities")
elif(average >= 70):
    for i in range (10):  # spam "Below standards my G" 10 times
        print("Below standards my G")
elif(average >= 50):
    print("Please buddy, live up to your standards bro")
else:
    for i in range(100):  # spam "Restart Life" 100 times if user got below a 50
        print("Restart Life")
