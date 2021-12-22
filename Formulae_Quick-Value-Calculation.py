from time import sleep
from fractions import Fraction
import math

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def selection_of_formulae():
    print(" ")
    print(color.BOLD+'''This script contains three Physics\' "Equations of Motion":'''+color.END)
    sleep(3)
    print(color.ITALIC+"1- First Equation of Motion (Vf = Vi + at)"+color.END)
    sleep(2.5)
    print(color.ITALIC+"2- Second Equation of Motion (S = Vit + 1/2 at²)"+color.END)
    sleep(2.5)
    print(color.ITALIC+"3- Third Equation of Motion (2aS = Vf² - Vi²)"+color.END)
    sleep(2.8)
    
def choose_of_formula():
    print(" ")
    choice_of_formula = input(color.BOLD+color.BLUE+"Which Equation do you wish to run? (Type 1,2 or 3): "+color.END)
    # First checks if input is convertible in integer form
    try:
        choice_of_formula = int(choice_of_formula)
    # Otherwise keeps it as it is
    except:
        choice_of_formula = choice_of_formula
    if choice_of_formula == 1:
        startup_1()
    elif choice_of_formula == 2:
        startup_2()
    elif choice_of_formula == 3:
        startup_3()
    else:
        print(color.BOLD+color.UNDERLINE+color.RED+"Invalid input. Please type 1 OR 2 OR 3."+color.END)
        sleep(2)
        choose_of_formula()

def exit_code():
    print(" ")
    print(color.BOLD+"The script will now exit. Goodbye!"+color.END)
    sleep(1.7)
    print(" ")
    print(color.GREEN+color.BOLD+"What do you think of my script by the way?"+color.END)
    sleep(1.4)
    print(color.GREEN+color.BOLD+"Let me know!"+color.END)
    sleep(1.4)
    print("   ==========================================")
    print(color.ITALIC+"         Programmed by: Mubashir78"+color.END)
    print("   ==========================================")
    sleep(1.8)
    exit()

# There are separate restart codes for each of the Equation of Motion

def restart_code_1():
    sleep(2.5)
    print(" ")
    print(color.BLUE+color.BOLD+color.ITALIC+"You can either retry the equation, go back to choosing another equation, or exit this script."+color.END)
    sleep(3.7)
    print(" ")
    restart = input(color.BLUE+color.BOLD+color.ITALIC+"To retry this equation, type 'retry'; To go back to choosing another equation, type 'go back'; To exit, type 'exit': "+color.END).lower()
    if restart == "retry":
        print(" ")
        print(color.ITALIC+"Restarting..."+color.END)
        sleep(1.8)
        main_1()
    elif restart == "go back":
        print(" ")
        print(color.ITALIC+"Reverting back...")
        sleep(2.5)
        choose_of_formula()
    elif restart == "exit":
        exit_code()
    else:
        print(" ")
        print(color.BOLD+"Invalid input!"+color.END)
        sleep(2)
        print(color.ITALIC+"Restarting..."+color.END)
        sleep(1.8)
        restart_code_1()

def restart_code_2():
    sleep(2.5)
    print(" ")
    print(color.BLUE+color.BOLD+color.ITALIC+"You can either retry the equation, go back to choosing another equation, or exit this script."+color.END)
    sleep(3.7)
    print(" ")
    restart = input(color.BLUE+color.BOLD+color.ITALIC+"To retry this equation, type 'retry'; To go back to choosing another equation, type 'go back'; To exit, type 'exit': "+color.END).lower()
    if restart == "retry":
        print(" ")
        print(color.ITALIC+"Restarting..."+color.END)
        sleep(1.8)
        main_2()
    elif restart == "go back":
        print(" ")
        print(color.ITALIC+"Reverting back...")
        sleep(2.5)
        choose_of_formula()
    elif restart == "exit":
        exit_code()
    else:
        print(" ")
        print(color.BOLD+"Invalid input!"+color.END)
        sleep(2)
        print(color.ITALIC+"Restarting..."+color.END)
        sleep(1.8)
        restart_code_2()

def restart_code_3():
    sleep(2.5)
    print(" ")
    print(color.BLUE+color.BOLD+color.ITALIC+"You can either retry the equation, go back to choosing another equation, or exit this script."+color.END)
    sleep(3.7)
    print(" ")
    restart = input(color.BLUE+color.BOLD+color.ITALIC+"To retry this equation, type 'retry'; To go back to choosing another equation, type 'go back'; To exit, type 'exit': "+color.END).lower()
    if restart == "retry":
        print(" ")
        print(color.ITALIC+"Restarting..."+color.END)
        sleep(1.8)
        main_3()
    elif restart == "go back":
        print(" ")
        print(color.ITALIC+"Reverting back..."+color.END)
        sleep(2.5)
        choose_of_formula()
    elif restart == "exit":
        exit_code()
    else:
        print(" ")
        print(color.BOLD+"Invalid input!"+color.END)
        sleep(2)
        print(color.ITALIC+"Restarting..."+color.END)
        sleep(1.8)
        restart_code_3()

# Same for the main codes as well

def main_1():
    print(" ")
    # Takes input for variables
    Vi=input(color.CYAN+"Value of 'Vi': "+color.END)
    Vf=input(color.CYAN+"Value of 'Vf': "+color.END)
    a= input(color.CYAN+"Value of 'a': "+color.END)
    t= input(color.CYAN+"Value of 't': "+color.END)

    variables = [Vi,Vf,a,t]
    
    true_variables = []
    for v in variables:
        # Tries to add variables converted into float to the list above
        try:
            true_variables.append(float(v))
        # Otherwise adds them as they are
        except ValueError:
            true_variables.append(v)

    variables = true_variables
    del (true_variables,v)
    # Creates a new, empty list, and puts the type of values present in "variables" list above in it
    list_of_types = []
    for var in variables:
        list_of_types.append(type(var))
    # Counts the number of string types found and assigns the number to another variable
    number_of_strings = list_of_types.count(str)
    del var

    if number_of_strings == 2 or number_of_strings == 3 or number_of_strings == 4:
        print(color.BOLD+color.RED+color.UNDERLINE+"Sorry, calculation is not possible. Please make sure that only one value is unknown, while the rest must be known."+color.END)
        sleep(2)
        restart_code_1()

    elif number_of_strings == 0:
        print(color.BOLD+color.RED+color.UNDERLINE+"Sorry, all values are already known. Please make sure one value is unknown."+color.END)
        sleep(2)
        restart_code_1()
    # Separate formula depending upon which value is unknown/string
    elif type(variables[0]) == str:
        print(" ")
        print(color.ITALIC+"Calculating value of 'Vi'..."+color.END)
        found_Vi = float(Vf) - float(a) * float(t)
        limited_found_Vi = round(found_Vi,3)
        sleep(3.5)
        print(color.GREEN+color.UNDERLINE+"The value of 'Vi' is:",float(limited_found_Vi),"m/s"+color.END)
        restart_code_1()

    elif type(variables[1]) == str:
        print(" ")
        print(color.ITALIC+"Calculating value of 'Vf'..."+color.END)
        found_Vf = float(Vi) + float(a) * float(t)
        limited_found_Vf = round(found_Vf,3)
        sleep(3.5)
        print(color.GREEN+color.UNDERLINE+"The value of 'Vf' is:",float(limited_found_Vf),"m/s"+color.END)
        restart_code_1()

    elif type(variables[2]) == str:
        print(" ")
        print(color.ITALIC+"Calculating value of 'a'..."+color.END)
        found_a = (float(Vf) - float(Vi)) / float(t)
        limited_found_a = round(found_a,3)
        sleep(3.5)
        print(color.GREEN+color.UNDERLINE+"The value of 'a' is:",float(limited_found_a),"m/s²"+color.END)
        restart_code_1()

    elif type(variables[3]) == str:
        print(" ")
        print(color.ITALIC+"Calculating the value of 't'..."+color.END)
        found_t = (float(Vf) - float(Vi)) / float(a)
        limited_found_t = round(found_t,3)
        sleep(3.5)
        print(color.GREEN+color.UNDERLINE+"The value of 't' is:",float(limited_found_t),"sec"+color.END)
        restart_code_1()

def main_2():
    print(" ")
    S = input(color.CYAN+"Value of 'S': "+color.END)
    Vi = input(color.CYAN+"Value of 'Vi': "+color.END)
    t = input(color.CYAN+"Value of 't': "+color.END)
    a = input(color.CYAN+"Value of 'a': "+color.END)

    variables = [S,Vi,t,a]
    true_variables = []

    for v in variables:
        try:
            true_variables.append(float(v))
        except ValueError:
            true_variables.append(v)
    variables = true_variables
    del (true_variables,v)

    list_of_types = []
    for var in variables:
        list_of_types.append(type(var))
    number_of_strings = list_of_types.count(str)
    del var
    
    if number_of_strings == 2 or number_of_strings == 3 or number_of_strings == 4:
        print(color.BOLD+color.RED+color.UNDERLINE+"Sorry, calculation is not possible. Please make sure that only one value is unknown, while the rest must be known."+color.END)
        sleep(2)
        restart_code_2()
    
    elif number_of_strings == 0:
        print(color.BOLD+color.RED+color.UNDERLINE+"Sorry, all values are already known. Please make sure one value is unknown."+color.END)
        sleep(2)
        restart_code_2()
    
    elif type(variables[0]) == str:
        print(" ")
        print(color.ITALIC+"Calculating value of 'S'..."+color.END)
        found_S = (float(Vi) * float(t)) + (Fraction(1, 2) * float(a) * (float(t) * float(t)))
        limited_found_S = round(found_S,3)
        sleep(3.5)
        print(color.GREEN+color.UNDERLINE+"The value of 'S' is:",float(limited_found_S),"m"+color.END)
        restart_code_2()

    elif type(variables[1]) == str:
        print(" ")
        print(color.ITALIC+"Calculating value of Vi..."+color.END)
        found_Vi = (float(S) - (Fraction(1, 2) * float(a) * (float(t) * float(t)))) / float(t)
        limited_found_Vi = round(found_Vi,3)
        sleep(3.5)
        print(color.GREEN+color.UNDERLINE+"The value of 'Vi' is:",float(limited_found_Vi),"m/s"+color.END)
        restart_code_2()

    elif type(variables[2]) == str:
        print(" ")
        print(color.ITALIC+"Calculating value of t..."+color.END)
        found_t = (math.sqrt((float(Vi) * float(Vi)) + 2 * float(a) * float(S)) - float(Vi)) / float(a)
        limited_found_t = round(found_t,3)
        sleep(3.5)
        print(color.GREEN+color.UNDERLINE+"The value of 't' is:",float(limited_found_t),"sec"+color.END)
        restart_code_2()

    elif type(variables[3]) == str:
        print(" ")
        print(color.ITALIC+"Calculating value of a..."+color.END)
        found_a = (2 * float(S) / (float(t) * float(t))) - (2 * float(Vi) / float(t))
        limited_found_a = round(found_a,3)
        sleep(3.5)
        print(color.GREEN+color.UNDERLINE+"The value of 'a' is:",float(limited_found_a),"m/s²"+color.END)
        restart_code_2()

def main_3():
    print(" ")
    a = input(color.CYAN+"Value of 'a': "+color.END)
    S = input(color.CYAN+"Value of 'S': "+color.END)
    Vf = input(color.CYAN+"Value of 'Vf': "+color.END)
    Vi = input(color.CYAN+"Value of Vi: "+color.END)

    variables = [a,S,Vf,Vi]
    true_variables = []

    for v in variables:
        try:
            true_variables.append(float(v))
        except ValueError:
            true_variables.append(v)
    variables = true_variables
    del (true_variables,v)

    list_of_types = []
    for var in variables:
        list_of_types.append(type(var))
    number_of_strings = list_of_types.count(str)
    del var

    if number_of_strings == 2 or number_of_strings == 3 or number_of_strings == 4:
        print(color.BOLD+color.RED+color.UNDERLINE+"Sorry, calculation is not possible. Please make sure that only one value is unknown, while the rest must be known."+color.END)
        sleep(2)
        restart_code_3()
    
    elif number_of_strings == 0:
        print(color.BOLD+color.RED+color.UNDERLINE+"Sorry, all values are already known. Please make sure one value is unknown."+color.END)
        sleep(2)
        restart_code_3()

    elif type(variables[0]) == str:
        print(" ")
        print(color.ITALIC+"Calculating value of 'a'..."+color.END)
        found_a = ((float(Vf) * float(Vf)) - (float(Vi) * float(Vi))) / (2 * float(S))
        limited_found_a = round(found_a,5)
        sleep(3.5)
        print(color.GREEN+color.UNDERLINE+"The value of 'a' is:",float(limited_found_a),"m/s²"+color.END)
        restart_code_3()

    elif type(variables[1]) == str:
        print(" ")
        print(color.ITALIC+"Calculating value of 'S'..."+color.END)
        found_S = ((float(Vf) * float(Vf)) - (float(Vi) * float(Vi))) / (2 * float(a))
        limited_found_S = round(found_S,5)
        sleep(3.5)
        print(color.GREEN+color.UNDERLINE+"The value of 'S' is:",float(limited_found_S),"m"+color.END)
        restart_code_3()

    elif type(variables[2]) == str:
        print(" ")
        print(color.ITALIC+"Calculating value of 'Vf'..."+color.END)
        found_Vf = math.sqrt(2 * float(a) * float(S) + float(Vi))
        limited_found_Vf = round(found_Vf,5)
        sleep(3.5)
        print(color.GREEN+color.UNDERLINE+"The value of 'Vf' is:",float(limited_found_Vf),"m/s"+color.END)
        restart_code_3()

    elif type(variables[3]) == str:
        print(" ")
        print(color.ITALIC+"Calculating value of 'Vi'..."+color.END)
        found_Vi = math.sqrt((float(Vf) * float(Vf)) - (2 * float(a) *float(S)))
        limited_found_Vi = round(found_Vi,5)
        sleep(3.5)
        print(color.GREEN+color.UNDERLINE+"The value of 'Vi' is:",float(limited_found_Vi),"m/s"+color.END)
        restart_code_3()

def startup_1():
    print(" ")
    print("   =====================================================")
    print(color.ITALIC+"     Value Calculator For 'First Equation Of Motion'")
    print("              Programmed by: Mubashir78"+color.END)
    print("   =====================================================")
    sleep(3)
    print(" ")
    print(color.BOLD+"Welcome! This little script calculates the values of '"+color.BLUE+"Vf"+color.END+"','"+color.BLUE+"Vi"+color.END+"','"+color.BLUE+"a"+color.END+"' &  '"+color.BLUE+"t"+color.END+"'!")
    sleep(2.8)
    print("")
    print(color.BOLD+"Just type in the known values one by one, marking the unknown value with "+color.UNDERLINE+"English words"+color.END+color.BOLD+" or "+color.UNDERLINE+"'?'"+color.END+color.BOLD+", and the unknown value will be automatically calculated."+color.END)
    sleep(2.8)
    main_1()

def startup_2():
    pass
    print(" ")
    print("   =====================================================")
    print(color.ITALIC+"     Value Calculator For 'Second Equation Of Motion'")
    print("              Programmed by: Mubashir78"+color.END)
    print("   =====================================================")
    sleep(3)
    print(" ")
    print(color.BOLD+"Welcome! This little script calculates the values of '"+color.BLUE+"S"+color.END+"','"+color.BLUE+"Vi"+color.END+"','"+color.BLUE+"t"+color.END+"' &  '"+color.BLUE+"a"+color.END+"'!")
    sleep(2.8)
    print("")
    print(color.BOLD+"Just type in the known values one by one, marking the unknown value with "+color.UNDERLINE+"English words"+color.END+color.BOLD+" or "+color.UNDERLINE+"'?'"+color.END+color.BOLD+", and the unknown value will be automatically calculated."+color.END)
    sleep(2.8)
    main_2()

def startup_3():
        print(" ")
        print("   =====================================================")
        print(color.ITALIC+"     Value Calculator For 'Third Equation Of Motion'")
        print("              Programmed by: Mubashir78"+color.END)
        print("   =====================================================")
        sleep(3)
        print(" ")
        print(color.BOLD+"Welcome! This little script calculates the values of '"+color.BLUE+"a"+color.END+"','"+color.BLUE+"S"+color.END+"','"+color.BLUE+"Vf"+color.END+"' &  '"+color.BLUE+"Vi"+color.END+"'!")
        sleep(2.8)
        print("")
        print(color.BOLD+"Just type in the known values one by one, marking the unknown value with "+color.UNDERLINE+"English words"+color.END+color.BOLD+" or "+color.UNDERLINE+"'?'"+color.END+color.BOLD+", and the unknown value will be automatically calculated."+color.END)
        sleep(2.8)
        main_3()

selection_of_formulae()
choose_of_formula()