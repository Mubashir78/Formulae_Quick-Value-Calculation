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

class Error:
    er_code_more_than_1_str = color.BOLD+color.RED+color.UNDERLINE+"Sorry, calculation is not possible. Please make sure that only one value is unknown, while the rest must be known."+color.END
    er_code_no_str = color.BOLD+color.RED+color.UNDERLINE+"Sorry, all values are already known. Please make sure one value is unknown."+color.END
    er_code_inv_inp = color.BOLD+color.RED+color.UNDERLINE+"Invalid input. Please try again."+color.END

def selection_of_formulae():
    print(" ")
    print(color.BOLD+'''This script contains three Physics\' "Equations of Motion":'''+color.END)
    sleep(2.5)
    print(color.ITALIC+"1- First Equation of Motion (Vf = Vi + at)"+color.END)
    sleep(2)
    print(color.ITALIC+"2- Second Equation of Motion (S = Vit + 1/2 at²)"+color.END)
    sleep(2)
    print(color.ITALIC+"3- Third Equation of Motion (2aS = Vf² - Vi²)"+color.END)
    sleep(2.4)
    
def choose_of_formula():
    print(" ")
    choice_of_formula = input(color.BOLD+color.BLUE+"Which Equation do you wish to run? (Type 1,2 or 3): "+color.END)
    
    if choice_of_formula == "1":
        startup("First", "Vf", "Vi", "a", "t")
        main_1()
    elif choice_of_formula == "2":
        startup("Second", "S", "Vi", "t", "a")
        main_2()
    elif choice_of_formula == "3":
        startup("Third", "a", "S", "Vf", "Vi")
        main_3()
    else:
        print(color.BOLD+color.UNDERLINE+color.RED+"Invalid input. Please type 1 OR 2 OR 3."+color.END)
        sleep(2)
        choose_of_formula()

def exit_code():
    print(" ")
    print(color.BOLD+"The script will now exit. Goodbye!"+color.END)
    sleep(1.5)
    print(" ")
    print(color.GREEN+color.BOLD+"What do you think of my script by the way?"+color.END)
    sleep(1.3)
    print(color.GREEN+color.BOLD+"Let me know!"+color.END)
    sleep(1.3)
    print("   ==========================================")
    print(color.ITALIC+"         Programmed by: Mubashir Ahmed"+color.END)
    print("   ==========================================")
    sleep(1.6)
    exit()

# There are separate restart codes for each of the Equation of Motion

#

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
        # Otherwise adds them as they are (i.e strings)
        except ValueError:
            true_variables.append(v)

    variables = true_variables
    # Creates a new, empty list, and puts the type of values present in "variables" list above in it
    list_of_types = []
    for i in variables:
        list_of_types.append(type(i))
    # Counts the number of string types found and assigns the number to another variable
    number_of_strings = list_of_types.count(str)

    if number_of_strings == 2 or number_of_strings == 3 or number_of_strings == 4:
        print("%s" % Error.er_code_more_than_1_str)
        sleep(1.8)
        restart_code(main_1)

    elif number_of_strings == 0:
        print("%s" % Error.er_code_no_str)
        sleep(1.8)
        restart_code(main_1)
    # Separate formula depending upon which value is unknown/string
    elif type(variables[0]) == str:
        print(" ")
        print(color.ITALIC+"Calculating value of 'Vi'..."+color.END)
        found_Vi = float(Vf) - float(a) * float(t)
        limited_found_Vi = round(found_Vi,3)
        sleep(2.6)
        print(color.GREEN+color.UNDERLINE+"The value of 'Vi' is:",float(limited_found_Vi),"m/s"+color.END)
        restart_code(main_1)

    elif type(variables[1]) == str:
        print(" ")
        print(color.ITALIC+"Calculating value of 'Vf'..."+color.END)
        found_Vf = float(Vi) + float(a) * float(t)
        limited_found_Vf = round(found_Vf,3)
        sleep(2.6)
        print(color.GREEN+color.UNDERLINE+"The value of 'Vf' is:",float(limited_found_Vf),"m/s"+color.END)
        restart_code(main_1)

    elif type(variables[2]) == str:
        print(" ")
        print(color.ITALIC+"Calculating value of 'a'..."+color.END)
        found_a = (float(Vf) - float(Vi)) / float(t)
        limited_found_a = round(found_a,3)
        sleep(2.6)
        print(color.GREEN+color.UNDERLINE+"The value of 'a' is:",float(limited_found_a),"m/s²"+color.END)
        restart_code(main_1)

    elif type(variables[3]) == str:
        print(" ")
        print(color.ITALIC+"Calculating the value of 't'..."+color.END)
        found_t = (float(Vf) - float(Vi)) / float(a)
        limited_found_t = round(found_t,3)
        sleep(2.6)
        print(color.GREEN+color.UNDERLINE+"The value of 't' is:",float(limited_found_t),"sec"+color.END)
        restart_code(main_1)

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

    list_of_types = []
    for var in variables:
        list_of_types.append(type(var))
    number_of_strings = list_of_types.count(str)
    
    if number_of_strings == 2 or number_of_strings == 3 or number_of_strings == 4:
        print("%s" % Error.er_code_more_than_1_str)
        sleep(1.8)
        restart_code(main_2)
    
    elif number_of_strings == 0:
        print("%s" % Error.er_code_no_str)
        sleep(1.8)
        restart_code(main_2)
    
    elif type(variables[0]) == str:
        print(" ")
        print(color.ITALIC+"Calculating value of 'S'..."+color.END)
        found_S = (float(Vi) * float(t)) + (Fraction(1, 2) * float(a) * (float(t) * float(t)))
        limited_found_S = round(found_S,3)
        sleep(2.6)
        print(color.GREEN+color.UNDERLINE+"The value of 'S' is:",float(limited_found_S),"m"+color.END)
        restart_code(main_2)

    elif type(variables[1]) == str:
        print(" ")
        print(color.ITALIC+"Calculating value of Vi..."+color.END)
        found_Vi = (float(S) - (Fraction(1, 2) * float(a) * (float(t) * float(t)))) / float(t)
        limited_found_Vi = round(found_Vi,3)
        sleep(2.6)
        print(color.GREEN+color.UNDERLINE+"The value of 'Vi' is:",float(limited_found_Vi),"m/s"+color.END)
        restart_code(main_2)

    elif type(variables[2]) == str:
        print(" ")
        print(color.ITALIC+"Calculating value of t..."+color.END)
        found_t = (math.sqrt((float(Vi) * float(Vi)) + 2 * float(a) * float(S)) - float(Vi)) / float(a)
        limited_found_t = round(found_t,3)
        sleep(2.6)
        print(color.GREEN+color.UNDERLINE+"The value of 't' is:",float(limited_found_t),"sec"+color.END)
        restart_code(main_2)

    elif type(variables[3]) == str:
        print(" ")
        print(color.ITALIC+"Calculating value of a..."+color.END)
        found_a = (2 * float(S) / (float(t) * float(t))) - (2 * float(Vi) / float(t))
        limited_found_a = round(found_a,3)
        sleep(2.6)
        print(color.GREEN+color.UNDERLINE+"The value of 'a' is:",float(limited_found_a),"m/s²"+color.END)
        restart_code(main_2)

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
        print("%s" % Error.er_code_more_than_1_str)
        sleep(1.8)
        restart_code(main_3)
    
    elif number_of_strings == 0:
        print("%s" % Error.er_code_no_str)
        sleep(1.8)
        restart_code(main_3)

    elif type(variables[0]) == str:
        print(" ")
        print(color.ITALIC+"Calculating value of 'a'..."+color.END)
        found_a = ((float(Vf) * float(Vf)) - (float(Vi) * float(Vi))) / (2 * float(S))
        limited_found_a = round(found_a,5)
        sleep(2.6)
        print(color.GREEN+color.UNDERLINE+"The value of 'a' is:",float(limited_found_a),"m/s²"+color.END)
        restart_code(main_3)

    elif type(variables[1]) == str:
        print(" ")
        print(color.ITALIC+"Calculating value of 'S'..."+color.END)
        found_S = ((float(Vf) * float(Vf)) - (float(Vi) * float(Vi))) / (2 * float(a))
        limited_found_S = round(found_S,5)
        sleep(2.6)
        print(color.GREEN+color.UNDERLINE+"The value of 'S' is:",float(limited_found_S),"m"+color.END)
        restart_code(main_3)

    elif type(variables[2]) == str:
        print(" ")
        print(color.ITALIC+"Calculating value of 'Vf'..."+color.END)
        found_Vf = math.sqrt(2 * float(a) * float(S) + float(Vi))
        limited_found_Vf = round(found_Vf,5)
        sleep(2.6)
        print(color.GREEN+color.UNDERLINE+"The value of 'Vf' is:",float(limited_found_Vf),"m/s"+color.END)
        restart_code(main_3)

    elif type(variables[3]) == str:
        print(" ")
        print(color.ITALIC+"Calculating value of 'Vi'..."+color.END)
        found_Vi = math.sqrt((float(Vf) * float(Vf)) - (2 * float(a) *float(S)))
        limited_found_Vi = round(found_Vi,5)
        sleep(2.6)
        print(color.GREEN+color.UNDERLINE+"The value of 'Vi' is:",float(limited_found_Vi),"m/s"+color.END)
        restart_code(main_3)

def restart_code(main_no):
    while True:
        sleep(2)
        print(" ")
        restart = input(color.BLUE+color.BOLD+color.ITALIC+"To retry this equation, type 'retry'; To go back to choosing another equation, type 'go back'; To exit, type 'exit': "+color.END).lower()
        
        if restart == "retry":
            print(" ")
            print(color.ITALIC+"Restarting..."+color.END)
            sleep(1.5)
            main_no()
        elif restart == "go back":
            print(" ")
            print(color.ITALIC+"Reverting back...")
            sleep(2)
            choose_of_formula()
        elif restart == "exit":
            exit_code()
        else:
            print("%s" % Error.er_code_inv_inp)

def startup(num, var_1, var_2, var_3, var_4):
    print(" ")
    print("   =====================================================")
    print(color.ITALIC+f"     Value Calculator For '{num} Equation Of Motion'")
    print("              Programmed by: Mubashir Ahmed"+color.END)
    print("   =====================================================")
    sleep(2.5)
    print(" ")
    print(color.BOLD+"Welcome! This little script calculates the values of '"+color.BLUE+f"{var_1}"+color.END+"','"+color.BLUE+f"{var_2}"+color.END+"','"+color.BLUE+f"{var_3}"+color.END+"' &  '"+color.BLUE+f"{var_4}"+color.END+"'!")
    sleep(2)
    print("")
    print(color.BOLD+"Just type in the known values one by one, marking the unknown value with "+color.UNDERLINE+"English words"+color.END+color.BOLD+" or "+color.UNDERLINE+"'?'"+color.END+color.BOLD+", and the unknown value will be automatically calculated."+color.END)
    sleep(2.3)

selection_of_formulae()
choose_of_formula()