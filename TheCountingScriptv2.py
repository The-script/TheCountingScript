'''This is 'The Counting Script'. It is a script that i made while learning python and as it says, its a script that counts .
    Copyright (C) 2022  The-script'''



import time, math, random

randommessage = ["The Counting Script does more than just counting (maybe)",
                 "This is the 2nd version of The Counting Script"
    , "Why exactly is this still called 'The Counting Script' if it does more than just counting?",
                 "These random messages exist just to waste your time",
                 "Did you know that there is a super rare message with a probability of 1 in ??? of happening",
                 "Version 2 'The Counting Script v2' will come soon™   <soon™ indicates that it will come out before 10 eternites.. maybe>"
                 ,"Also did i forget to tell you that theres a tiny (large) chance that this script breaks into bits?"]
end_wait = 0

print('''         ▒█░░▒█ ▒█▀▀▀ ▒█░░░ ▒█▀▀█ ▒█▀▀▀█ ▒█▀▄▀█ ▒█▀▀▀ 　 ▀▀█▀▀ ▒█▀▀▀█ 　 
         ▒█▒█▒█ ▒█▀▀▀ ▒█░░░ ▒█░░░ ▒█░░▒█ ▒█▒█▒█ ▒█▀▀▀ 　 ░▒█░░ ▒█░░▒█ 　 
         ▒█▄▀▄█ ▒█▄▄▄ ▒█▄▄█ ▒█▄▄█ ▒█▄▄▄█ ▒█░░▒█ ▒█▄▄▄ 　 ░▒█░░ ▒█▄▄▄█

         ▀▀█▀▀ ▒█░▒█ ▒█▀▀▀ 　 ▒█▀▀█ ▒█▀▀▀█ ▒█░▒█ ▒█▄░▒█ ▀▀█▀▀ ▀█▀ ▒█▄░▒█ ▒█▀▀█ 
         ░▒█░░ ▒█▀▀█ ▒█▀▀▀ 　 ▒█░░░ ▒█░░▒█ ▒█░▒█ ▒█▒█▒█ ░▒█░░ ▒█░ ▒█▒█▒█ ▒█░▄▄ 
         ░▒█░░ ▒█░▒█ ▒█▄▄▄ 　 ▒█▄▄█ ▒█▄▄▄█ ░▀▄▄▀ ▒█░░▀█ ░▒█░░ ▄█▄ ▒█░░▀█ ▒█▄▄█

         ▒█▀▀▀█ ▒█▀▀█ ▒█▀▀█ ▀█▀ ▒█▀▀█ ▀▀█▀▀ 
         ░▀▀▀▄▄ ▒█░░░ ▒█▄▄▀ ▒█░ ▒█▄▄█ ░▒█░░ 
         ▒█▄▄▄█ ▒█▄▄█ ▒█░▒█ ▄█▄ ▒█░░░ ░▒█░░    

                                                                               v1.9''')
time.sleep(3)
randomrare = random.randint(0, 12000)
if randomrare == random.randint(100, random.randint(101, 1422)):
    print('''Well, you got the super rare message, well too bad it ain't much really.
    I mean, it is the only random message has multiple lines so :D ''')
    print(" ")
else:
    print(randommessage[random.randint(0, len(randommessage)-1)])
    print(" ")

actionhist = []
actionhistcurrent = 0
actiontime = time.ctime()
totalrepeat = 1
histnot = 0

time.sleep(3)

while totalrepeat == 1:
    print('''　          　                 ▒█▀▄▀█ ▒█▀▀▀ ▒█▄░▒█ ▒█░▒█ 
        　          　         ▒█▒█▒█ ▒█▀▀▀ ▒█▒█▒█ ▒█░▒█ 
        　          　         ▒█░░▒█ ▒█▄▄▄ ▒█░░▀█ ░▀▄▄▀ ''')
    print('''Type the keyword for the action you wish to perform:
                           #1: TYPE "CALCULATOR" to open the really really really basic calculator
                           #2: TYPE "COUNTING" to use the original counting script :D"''')
    print("Input is not case sensitive.")
    time.sleep(1)
    action = str.upper(input("What action would you like to perform? : "))

    if action == "COUNTING":
        for i in range(100):
            print(" ")
        print('''                 ▒█▀▀█ ▒█▀▀▀█ ▒█░▒█ ▒█▄░▒█ ▀▀█▀▀ ▀█▀ ▒█▄░▒█ ▒█▀▀█ 　 
                     ▒█░░░ ▒█░░▒█ ▒█░▒█ ▒█▒█▒█ ░▒█░░ ▒█░ ▒█▒█▒█ ▒█░▄▄ 　 
                     ▒█▄▄█ ▒█▄▄▄█ ░▀▄▄▀ ▒█░░▀█ ░▒█░░ ▄█▄ ▒█░░▀█ ▒█▄▄█ 　 
                     ▒█▀▀▀█ ▒█▀▀█ ▒█▀▀█ ▀█▀ ▒█▀▀█ ▀▀█▀▀ 
                     ░▀▀▀▄▄ ▒█░░░ ▒█▄▄▀ ▒█░ ▒█▄▄█ ░▒█░░ 
                     ▒█▄▄▄█ ▒█▄▄█ ▒█░▒█ ▄█▄ ▒█░░░ ░▒█░░ 

        ''')
        time.sleep(2)

        x = int(input("Enter Initial Number: "))  # Initial Number Input

        y = int(input("Enter Final Number: ")) + 1  # Final Number Input

        print("Type 'EVEN' or 'ODD' or 'INCREMENT' or 'NORMAL COUNT'")
        print("Input is not case sensitive")

        count_type = input("Input Count Type: ")
        count_type = str.upper(count_type)

        if count_type == "EVEN":
            if x % 2 == 0:  # checks for even
                for i in range(x, y):
                    print(x)
                    x += 2
            if x % 2 != 0:  # checks for odd
                nx = x + 1
                for i in range(x, y):
                    print(nx)
                    nx += 2
            actiontime = time.ctime()
            actionhist.append("-{0}-:Count {1} -> {2} --TYPE:EVEN".format(actiontime, x, y))

        if count_type == "ODD":
            if x % 2 == 0:
                nx = x + 1

                for i in range(x, y):
                    print(nx)
                    nx += 2

            if x % 2 != 0:
                for i in range(x, y):
                    print(x)
                    x += 2

        elif count_type == "INCREMENT":
            increment = int(input(" Enter INCREMENT, increment is the difference between successive numbers"))

            for i in range(x, y):
                print(x)
                if x + increment > y:
                    break
                if x + increment < y:
                    x += increment
        elif count_type == "NORMAL COUNT":
            for i in range(x, y):
                print(x)
                x += 1

        elif count_type != "EVEN" and count_type != "ODD" and count_type != "INCREMENT" and count_type != "NORMAL COUNT":
            print("Error: unknown count type")


    elif action == "CALCULATOR":
        for i in range(100):
            print(" ")
        print('''                 ▒█▀▀█ ░█▀▀█ ▒█░░░ ▒█▀▀█ ▒█░▒█ ▒█░░░ ░█▀▀█ ▀▀█▀▀ ▒█▀▀▀█ ▒█▀▀█ 
                 ▒█░░░ ▒█▄▄█ ▒█░░░ ▒█░░░ ▒█░▒█ ▒█░░░ ▒█▄▄█ ░▒█░░ ▒█░░▒█ ▒█▄▄▀ 
                 ▒█▄▄█ ▒█░▒█ ▒█▄▄█ ▒█▄▄█ ░▀▄▄▀ ▒█▄▄█ ▒█░▒█ ░▒█░░ ▒█▄▄▄█ ▒█░▒█ ''')
        val1 = float(input("Enter A Value: "))
        calc_repeat = 1
        calc_count = 1
        while calc_repeat == 1:
            if calc_count == 1:
                calc_count = 0
                print('''Type:
                         #1: "+" to add two numbers
                         #2: "-" to subtract
                         #3: "*" to multiply
                         #4: "/" to divide
                         #5: "!" to find factorial
                         #6: "log" to find log ''')

                calc_action = str.upper(input("What Action would You Like to do? : "))
                if calc_action == "+":
                    val2 = float(input("Enter a value: "))
                    valnot = val1
                    val1 = val1 + val2
                    print(val1)
                    calc_repeat = str.upper(input('''Type "YES" if you would like to carry out other operations, if not, 
                    type "NO" : '''))

                    actiontime = time.ctime()
                    actionhist.append("--{0}--: CALC.addition: {1} + {2}".format(actiontime, valnot, val2))
                    if calc_repeat == "YES":
                        calc_repeat = 1
                        calc_count = 1
                    else:
                        calc_repeat = 0
                elif calc_action == "-":
                    val2 = float(input("Enter a value: "))
                    valnot = val1
                    val1= val1-val2
                    print(val1)
                    actiontime = time.ctime()
                    actionhist.append("--{0}--: CALC.subtraction: {1} - {2}".format(actiontime, valnot, val2))
                    calc_repeat = str.upper(input('''Type "YES" if you would like to carry out other operations, if not, 
                                    type "NO" : '''))

                    if calc_repeat == "YES":
                        calc_repeat = 1
                        calc_count = 1
                    else:
                        calc_repeat = 0
                if calc_action == "*":
                    val2 = float(input("Enter a value: "))
                    valnot = val1
                    val1 = val1 * val2
                    print(val1)
                    actiontime = time.ctime()
                    actionhist.append("--{0}--: CALC.multiplication: {1} * {2}".format(actiontime, valnot, val2))
                    calc_repeat = str.upper(input('''Type "YES" if you would like to carry out other operations, if not, 
                                    type "NO" : '''))

                    if calc_repeat == "YES":
                        calc_repeat = 1
                        calc_count = 1
                    else:
                        calc_repeat = 0
                if calc_action == "/":
                    val2 = float(input("Enter a value: "))
                    if val2 == 0:
                        print("Division By 0 is not possible, enter initial value again")
                        val1 = float(input("Enter a value : "))
                        calc_repeat = str.upper(input('''Type "YES" if you would like to carry out other operations, 
                        if not, type "NO" : '''))
                        actiontime = time.ctime()
                        actionhist.append(
                            "--{0}--: CALC.division.err: Division by 0 is not possible".format(actiontime))

                        if calc_repeat == "YES":
                            calc_repeat = 1
                            calc_count = 1
                        else:
                            calc_repeat = 0
                    else:
                        valnot = val1
                        val1 = val1 / val2
                        actiontime = time.ctime()
                        actionhist.append("--{0}--: CALC.division: {1} / {2}".format(actiontime, valnot, val2))
                        print(val1)
                        calc_repeat = str.upper(input('''Type "YES" if you would like to carry out other operations, 
                        if not, type "NO" : '''))

                        if calc_repeat == "YES":
                            calc_repeat = 1
                            calc_count = 1
                        else:
                            calc_repeat = 0
                if calc_action == "!":
                    valnot = val1
                    val1 = math.factorial(val1)
                    print(val1)
                    actiontime = time.ctime()
                    actionhist.append("--{0}--: CALC.Factorial: {1}!".format(actiontime, valnot))
                    calc_repeat = str.upper(input('''Type "YES" if you would like to carry out other operations, if not, 
                                                        type "NO" : '''))

                    if calc_repeat == "YES":
                        calc_repeat = 1
                        calc_count = 1
                    else:
                        calc_repeat = 0

                if calc_action == "LOG":
                    print("The value entered previously is the base, would you like to change it?")
                    print('''Type "YES" or "NO"''')
                    calc_log_change = str.upper(input("Would you like to change it? : "))
                    if calc_log_change == "YES":
                        val1 = float(input("Enter a value (base): "))
                        val2 = float(input("Enter a value (argument): "))
                        val3 = math.log(val2, val1)
                    if calc_log_change == "NO":
                        val2=float(input("Enter a value (argument): "))
                        val3 = math.log(val2,val1)
                    if val2 == 1 or val2 < 0:
                        print("log for negative numbers is not defined, log for 1 is also not defined")
                        break
                    if val1 == 0 or val1 < 0:
                        print("log not defined for negative numbers and 0")
                        break

                    actiontime = time.ctime()
                    actionhist.append(
                        "--{0}--: CALC.Logarithm: logbase: {1} logarg: {2}".format(actiontime, val1, val2))
                    print(str(val3) + " is the log of " + str(val2) + " to the base of " + str(val1))

                    calc_repeat = str.upper(input('''Type "YES" if you would like to carry out other operations, if not, 
                                                                            type "NO" : '''))

                    if calc_repeat == "YES":
                        calc_repeat = 1
                        calc_count = 1
                    else:
                        calc_repeat = 0
    else:
        print("Invalid Action")

    print("This is as far as the script goes so well....,")

    histask = str.upper(input('''Would you like to view action history?
                                     #1: Type 'YES' if yes
                                     #2: Type 'NO' if no

                                     '''))
    if histask == "YES":
        for histnot in range(len(actionhist)):
            print(actionhist[histnot])
    histnot = 0

    print("Would you like to go back to the menu? :")

    print('''Type:
                         #1: "YES" to go back to menu
                         #2: "NO" to end script''')
    totalrepeat = str.upper(input("Would you like to go back to the menu? : "))
    if totalrepeat == "YES":
        totalrepeat = 1
        print("Going back to menu")
        for i in range(100):
            print(" ")
        time.sleep(2)

    else:
        totalrepeat = 0
        print("This script will terminate in 10 seconds")
        for i in range(10):
            end_wait += 1
            time.sleep(1)
