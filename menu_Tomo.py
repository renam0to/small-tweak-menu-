
def preamble():
    print("************************************************************************")
    print("We, the students of Bachelor of Science in Information Technology in order to form holistic learning environment, believe that:\n")
    print("1. All Bachelor of Science in Information Technology students regardless of gender, religion. color, or creed should have the opportunity \nto be involved in the BSIT Department.")
    print("2. All participants in the BSIT department should be responsible members of the BSIT Department of the Dalubhasaan ng Lungsod ng Lucena.")
    print("3. All BSIT students should work to create a safe learning environment")
    print("4. All BSIT students and staff should have the opportunity to voice their opinions on the departmental policies and issues")
    print("\t\t\t\t\t\t\t\t -Bachelor of Science in Information Technology Constitution PREAMBLE")
    continyuu = input("\nPress 'ENTER' to continue ")


def combine():
    print('\n\t\t\t\t\t\t\t\t\t\t       *\n\t\t\t\t\t\t\t\t\t             * * *\n\t\t\t\t\t\t\t\t\t           * * * * *\n\t\t\t\t\t\t\t\t                  * * * * * * \n\t\t\t\t\t\t\t\t\t           * * * * *\n\t\t\t\t\t\t\t\t\t             * * *\n\t\t\t\t\t\t\t\t\t\t       *')
    continyuu = input("\nPress 'ENTER' to continue ")
# ^^^^^^^^^^^^^^^^^^^^^^^^   PRINT COMMANDS  ^^^^^^^^^^^^^^^^^^^^^^^^


def variables():
    name = input("Name: ")
    confirmation = input("Did you buy a grocery?(Y/N) ")
    if confirmation.lower() == "y":
        item = input("Name of the item: ")
        price = eval(input("Price of the item(000.00): "))
        credit = eval(input("Amount given: "))
        discount = (5.2 / 100) * price
        disc1 = price - discount
        disc2 = credit - disc1
        tax = (12.3 / 100) * price
        tax1 = tax + price
        tax2 = credit - tax1
        age = eval(input("Age: "))
        if age <= 59:
            print(f"\tHello {name}! you purchased a {item}, with a price of {price} plus the tax of 12.3%, total of {tax1}. \n\tAmount Given: {credit}\n\tChange: {tax2} ")
        elif age >=60:
            print(f"\tHello! {name}, we congratulate you that you have granted a senior discount! \n\tWith your purchase of {item}, with a price of {price} plus the discount of 5.2% of your item, total of {disc1}. \n\tAmount Given: {credit}\n\tChange: {disc2} ")
      
    elif confirmation.lower() == "n":
        print("Thank you for using this program.")

    else:
        print("Invalid input")
    continyuu = input("Press 'ENTER' to continue ")

def calcval():
    number1 = eval(input("input thy number >> "))
    number2 = eval(input("input thy number >> "))

    answer1 = number1 + number2
    answer2 = number1 / number2
    answer3 = number1 - number2
    answer4 = number1 * number2
    answer5 = number1 // number2


    print ("\nThe sum of", number1,"and", number2, "is", answer1)
    print ("The division of", number1,"and", number2, "is", answer2)
    print ("The differences of", number1,"and", number2, "is", answer3)
    print ("The quotient of", number1,"and", number2, "is", answer4)
    print ("The floor division of", number1,"and", number2, "is", answer5)
    continyuu = input("Press 'ENTER' to continue ")


# ^^^^^^^^^^^^^^^^^^^^^^^^  VARIABLES COMMANDS  ^^^^^^^^^^^^^^^^^^^^^^^^
def agecond():
    age = eval(input("your age: "))

    if age >= 60 and age <=100: 
        print('Youre currently in Senior Age')
    elif age >= 46 and age <= 59:
        print('Youre currently in Post adulthood')
    elif age >=  32 and age <= 45:
        print('Youre currently in Mid Adulthood')
    elif age >= 19 and age <= 31:
        print('Youre currently in Early Adulthood')
    elif age >= 14 and age <= 18:
        print('Youre currently in Teenager')
    elif age >=8 and age <=13:
        print('Youre currently in Pre-Teen')
    elif age >= 1 and age <=7:
        print('Youre currently in Toddler')

    else:
        print('input a real number')
    continyuu = input("Press 'ENTER' to continue ")

# ^^^^^^^^^^^^^^^^^^^^^^^^  CONDITIONAL STATEMENTS   ^^^^^^^^^^^^^^^^^^^^^^^^  

def nameloop():
    from ast import Continue


    varia = True
    while varia == True:
        name=input("your name dawg: ")
        print("wassuh",name)
        print("Type 'STOP' to terminate the loop")

        if name.upper() == "STOP":
            print("Process has terminated")
            break
            varia = False
        else:
            continue
    continyuu = input("Press 'ENTER' to continue ")

def diamloop():
    for x in range(11,0,-1):
        for z in range(1,x +1):
            print(" ", end=" ")
        for y in range(11,x,-1):
            print("*", end=" ")
        for w in range(10,x,-1):
            print("*", end=" ")
        print()

    for x in range(1,11):
        for z in range(1,x +2):
            print(" ", end=" "),
        for y in range(10,x,-1):
            print("*", end=" ")
        for w in range(9,x,-1):
            print("*", end=" ")
        print()

    continyuu = input("Press 'ENTER' to continue ")
# ^^^^^^^^^^^^^^^^^^^^^^^^  LOOP PROGRAM  ^^^^^^^^^^^^^^^^^^^^^^^^

def listarray():
    what = ["1"]

    print(what)

    loopie = True
    while loopie == True:
        burn = input("what ya adding matey: ").lower()
        what.append(burn)
        print(what)
        sern = input("continue? (Y/N)")
        
        if sern == "n":
            break
        elif sern == "y":
            continue
        else:
            print("INVALID INPUT")
            continue
    print(what)


# ^^^^^^^^^^^^^^^^^^^^^^^^  ARRAY  ^^^^^^^^^^^^^^^^^^^^^^^^

def printinfo():
    print("\nPrint is a simple function program and helps display your output into a simple letters")
    print("Print also comes with different minor functions")
    print("You can combine these words called as 'strings' to form a single string")
    print("you can use a hashtag when coding, this can be use to indicate your program")
    continyuu = input("\nPress 'ENTER' to continue ")



def variableinfo():
    print("\nVariables in Python are simply being mathematic function that you can manipulate or create simple equations")
    print("It can use any mathematic signs")
    print("variables help build calculations for your program")
    continyuu = input("\nPress 'ENTER' to continue ")


def conditinfo():
    print("\nConditionals, as its name suggested, creates a 2 way identification when an item")
    print("the program helps decide when the output is True/False then the following program will run")
    continyuu = input("\nPress 'ENTER' to continue ")

def loopinfo():
    print("\nAs Loop name suggested, it repeats a program indented and distinguishes when to stop")
    print("This program can make your work being effecient and saves time making another copy")
    continyuu = input("\nPress 'ENTER' to continue ")

def arrayinfo():
    print("\nArray helps collect and arrange data or string of texts that can be manipulated")
    print("example being 'def' and list programs")
    continyuu = input("\nPress 'ENTER' to continue ")





import time

def loading_screen():
    print("Loading, please wait...")
    for i in range(1, 101): 
        time.sleep(0.05)  
        print(f"\rProgress: {i}%", end="")  
    print("\nLoading complete!")

loading_screen()

print("hey there!")


# ^^^^^^^^^^^^^^^^^^^^^^^^  python   ^^^^^^^^^^^^^^^^^^^^^^^^
#MENU SETUP ----------------------------------------------------------------------------------------
open = input("Input your name here: ")
print(f"Hello, {open}!")
repeat = True


conf = input("Would you like to startup the program? (Y/N)")
if conf.lower() == "y":
     #MENU HERE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    while repeat == True:
        
        print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Python Coding MENU")
        print("(1) Printing")
        print("(2) variables")
        print("(3) Conditionals")
        print("(4) Loops")
        print("(5) Array")
        print("(6) HELP")
        print("(7) BREAK")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        printa = input("\nChoose the following digits: ")
        


        if printa.lower() == "1": #Print
            print("(1) BSIT PREAMBLE")
            print("(2) Combine")
            printb = input("Choose the following digits: ")
            if printb.lower() == "1":
                preamble()
            elif printb.lower() == "2":
                combine()
            else:
                print("INVALID INPUT")
                continue
            

        elif printa.lower() == "2": #Variables
            print("(1) Purchase + Discount")
            print("(2) Calculator with 2 variables")
            terutn = input("Choose the following digits: ")
            if terutn.lower() == "1":
                variables()

            elif terutn.lower() == "2":
                calcval()
            else:
                print("INVALID INPUT")
                continue

        elif printa.lower() == "3": #Conditional
            print("(1) Age ID")
            condinp = input("Choose the following digits: ")
            if condinp.lower() == "1":
                agecond()
            else:
                print("INVALID INPUT")
                continue

        elif printa.lower() == "4":  #Loop
            print("(1) Name Loop")
            print("(2) Diamond")
            loopinp = input("Choose the following digits: ")
            if loopinp.lower() == "1":
                nameloop()
            elif loopinp.lower() == "2":
                diamloop()
            else:
                print("INVALID INPUT")
                continue
        
        elif printa.lower() == "5": #array
            print("(1) List Content")
            arrayinp = input("Choose the following digits: ")
            if arrayinp.lower() == "1":
                listarray()
            else:
                print("INVALID INPUT")
                continue
        
        elif printa.lower() == "6": #HELP
            print("(1) Print ")
            print("(2) Variables")            
            print("(3) Conditionals")
            print("(4) Loop")
            print("(5) Array")
            helpinp = input("Choose the following digits: ")
            if helpinp.lower() == "1":
                printinfo()
            elif helpinp.lower() == "2":
                variableinfo()
            elif helpinp.lower() == "3":
                conditinfo()
            elif helpinp.lower() == "4":
                loopinfo()
            elif helpinp.lower() == "5":
                arrayinfo()
            else:
                print("INVALID INPUT")


        elif printa.lower() == "7":
            print("Sure!")
            print("program has been terminated..")
            break    

        else:
            print("INVALID")
            continue


elif conf.lower() == "n":
    print("Very well!")
    print("program has been cancelled")
    
else:
    print("INVALID INPUT")
    print("Try again!")
       
    


