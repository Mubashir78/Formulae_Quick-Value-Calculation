# Programmed by: Mubashir Ahmed OR known as Mubashir78 on Github
# https://www.github.com/Mubashir78

import math
from fractions import Fraction
from sys import stdout
from time import sleep

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


def print_slow(str):
    for letter in str:
        stdout.write(letter)
        stdout.flush()
        sleep(0.02)
    print(" ")


def selection_of_formulae():
    print(" ")
    print_slow(color.BOLD+'''This script contains three Physics\' "Equations of Motion":'''+color.END)
    sleep(1.2)

    print_slow(color.ITALIC+"1- First Equation of Motion (Vf = Vi + at)"+color.END)
    sleep(0.8)

    print_slow(color.ITALIC+"2- Second Equation of Motion (S = Vit + 1/2 at²)"+color.END)
    sleep(0.8)

    print_slow(color.ITALIC+"3- Third Equation of Motion (2aS = Vf² - Vi²)"+color.END)
    sleep(1)

    return choose_of_formula()

    
def choose_of_formula():
    print(" ")
    choice_of_formula = input(color.BOLD+color.BLUE+"Which Equation do you wish to run? (Type 1,2 or 3): "+color.END).lower()
    
    if choice_of_formula == "1":
        startup("First", "Vf", "Vi", "a", "t")
        return main_1()
    
    elif choice_of_formula == "2":
        startup("Second", "S", "Vi", "t", "a")
        return main_2()
    
    elif choice_of_formula == "3":
        startup("Third", "a", "S", "Vf", "Vi")
        return main_3()
    
    elif choice_of_formula == "exit":
        return exit_code()

    else:
        print_slow(color.BOLD+color.UNDERLINE+color.RED+"Invalid input. Please type 1 OR 2 OR 3."+color.END)
        sleep(2)
        return choose_of_formula()

def exit_code():
    print(" ")
    print_slow(color.BOLD+"The script will now exit. Goodbye!"+color.END)
    sleep(0.5)
    
    print_slow("   ===================================")
    print_slow(color.ITALIC+"\tProgrammed by: Mubashir78"+color.END)
    print_slow("   ===================================")
    sleep(0.3)
    
    return

# There are separate main codes for each of the Equation of Motion

def main_1():
    print(" ")
    # Takes input for variables
    Vi=input(color.CYAN+"Value of 'Vf': "+color.END)
    Vf=input(color.CYAN+"Value of 'Vi': "+color.END)
    a= input(color.CYAN+"Value of 'a': "+color.END)
    t= input(color.CYAN+"Value of 't': "+color.END)

    variables = [Vf,Vi,a,t]
    
    true_variables = []
    for v in variables:
        # Tries to add variables converted into float to the list above
        try:
            true_variables.append(float(v))

        # Otherwise adds them as they are (i.e strings)
        except ValueError:
            true_variables.append(v)

    variables = true_variables
    del (true_variables, v)

    # Creates a new, empty list, and puts the type of values present in "variables" list above in it
    list_of_types = []
    for i in variables:
        list_of_types.append(type(i))

    # Counts the number of string types found and assigns the number to another variable
    number_of_strings = list_of_types.count(str)

    if number_of_strings == 2 or number_of_strings == 3 or number_of_strings == 4:
        print_slow(Error.er_code_more_than_1_str)
        sleep(0.8)
        return main_1()

    elif number_of_strings == 0:
        print_slow(Error.er_code_no_str)
        sleep(0.8)
        return main_1()

    # Separate formula depending upon which value is unknown/string
    elif type(variables[0]) == str:
        print(" ")
        print_slow(color.ITALIC+"Calculating value of 'Vf'..."+color.END)
        found_Vf = float(Vi) - float(a) * float(t)
        lim_found_Vf = round(found_Vf,3)
        sleep(1)
        print_slow(color.GREEN+color.UNDERLINE+f"The value of 'Vf' is: {float(lim_found_Vf)} m/s"+color.END)
        return restart_code(main_1)

    elif type(variables[1]) == str:
        print(" ")
        print_slow(color.ITALIC+"Calculating value of 'Vi'..."+color.END)
        found_Vi = float(Vf) + float(a) * float(t)
        lim_found_Vi = round(found_Vi,3)
        sleep(1)
        print_slow(color.GREEN+color.UNDERLINE+f"The value of 'Vi' is: {float(lim_found_Vi)} m/s"+color.END)
        return restart_code(main_1)

    elif type(variables[2]) == str:
        print(" ")
        print_slow(color.ITALIC+"Calculating value of 'a'..."+color.END)
        found_a = (float(Vf) - float(Vi)) / float(t)
        lim_found_a = round(found_a,3)
        sleep(1)
        print_slow(color.GREEN+color.UNDERLINE+f"The value of 'a' is: {float(lim_found_a)} m/s²"+color.END)
        return restart_code(main_1)

    elif type(variables[3]) == str:
        print(" ")
        print_slow(color.ITALIC+"Calculating the value of 't'..."+color.END)
        found_t = (float(Vf) - float(Vi)) / float(a)
        lim_found_t = round(found_t,3)
        sleep(1)
        print_slow(color.GREEN+color.UNDERLINE+f"The value of 't' is: {float(lim_found_t)} sec"+color.END)
        return restart_code(main_1)

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
    del (true_variables, v)

    list_of_types = []
    for i in variables:
        list_of_types.append(type(i))
    number_of_strings = list_of_types.count(str)
    del i

    if number_of_strings == 2 or number_of_strings == 3 or number_of_strings == 4:
        print_slow(Error.er_code_more_than_1_str)
        sleep(0.8)
        return main_2()
    
    elif number_of_strings == 0:
        print_slow(Error.er_code_no_str)
        sleep(0.8)
        return main_2()
    
    elif type(variables[0]) == str:
        print(" ")
        print_slow(color.ITALIC+"Calculating value of 'S'..."+color.END)
        found_S = (float(Vi) * float(t)) + (Fraction(1, 2) * float(a) * (float(t) * float(t)))
        lim_found_S = round(found_S,3)
        sleep(1)
        print_slow(color.GREEN+color.UNDERLINE+f"The value of 'S' is: {float(lim_found_S)} m"+color.END)
        return restart_code(main_2)

    elif type(variables[1]) == str:
        print(" ")
        print_slow(color.ITALIC+"Calculating value of Vi..."+color.END)
        found_Vi = (float(S) - (Fraction(1, 2) * float(a) * (float(t) * float(t)))) / float(t)
        lim_found_Vi = round(found_Vi,3)
        sleep(1)
        print_slow(color.GREEN+color.UNDERLINE+f"The value of 'Vi' is: {float(lim_found_Vi)} m/s"+color.END)
        return restart_code(main_2)

    elif type(variables[2]) == str:
        print(" ")
        print_slow(color.ITALIC+"Calculating value of t..."+color.END)
        found_t = (math.sqrt((float(Vi) * float(Vi)) + 2 * float(a) * float(S)) - float(Vi)) / float(a)
        lim_found_t = round(found_t,3)
        sleep(1)
        print_slow(color.GREEN+color.UNDERLINE+f"The value of 't' is: {float(lim_found_t)} sec"+color.END)
        return restart_code(main_2)

    elif type(variables[3]) == str:
        print(" ")
        print_slow(color.ITALIC+"Calculating value of a..."+color.END)
        found_a = (2 * float(S) / (float(t) * float(t))) - (2 * float(Vi) / float(t))
        lim_found_a = round(found_a,3)
        sleep(1)
        print_slow(color.GREEN+color.UNDERLINE+f"The value of 'a' is: {float(lim_found_a)} m/s²"+color.END)
        return restart_code(main_2)

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
    for i in variables:
        list_of_types.append(type(i))
    number_of_strings = list_of_types.count(str)
    del i

    if number_of_strings == 2 or number_of_strings == 3 or number_of_strings == 4:
        print_slow(Error.er_code_more_than_1_str)
        sleep(0.8)
        return main_3()
    
    elif number_of_strings == 0:
        print_slow(Error.er_code_no_str)
        sleep(0.8)
        return main_3()

    elif type(variables[0]) == str:
        print(" ")
        print_slow(color.ITALIC+"Calculating value of 'a'..."+color.END)
        found_a = ((float(Vf) * float(Vf)) - (float(Vi) * float(Vi))) / (2 * float(S))
        lim_found_a = round(found_a,5)
        sleep(1)
        print_slow(color.GREEN+color.UNDERLINE+f"The value of 'a' is: {float(lim_found_a)} m/s²"+color.END)
        return restart_code(main_3)

    elif type(variables[1]) == str:
        print(" ")
        print_slow(color.ITALIC+"Calculating value of 'S'..."+color.END)
        found_S = ((float(Vf) * float(Vf)) - (float(Vi) * float(Vi))) / (2 * float(a))
        lim_found_S = round(found_S,5)
        sleep(1)
        print_slow(color.GREEN+color.UNDERLINE+f"The value of 'S' is: {float(lim_found_S)} m"+color.END)
        return restart_code(main_3)

    elif type(variables[2]) == str:
        print(" ")
        print_slow(color.ITALIC+"Calculating value of 'Vf'..."+color.END)
        found_Vf = math.sqrt(2 * float(a) * float(S) + float(Vi))
        lim_found_Vf = round(found_Vf,5)
        sleep(1)
        print_slow(color.GREEN+color.UNDERLINE+f"The value of 'Vf' is: {float(lim_found_Vf)} m/s"+color.END)
        return restart_code(main_3)

    elif type(variables[3]) == str:
        print(" ")
        print_slow(color.ITALIC+"Calculating value of 'Vi'..."+color.END)
        found_Vi = math.sqrt((float(Vf) * float(Vf)) - (2 * float(a) *float(S)))
        lim_found_Vi = round(found_Vi,5)
        sleep(1)
        print_slow(color.GREEN+color.UNDERLINE+f"The value of 'Vi' is: {float(lim_found_Vi)} m/s"+color.END)
        return restart_code(main_3)

def restart_code(main_no):
    while True:
        sleep(0.6)
        print(" ")
        restart = input(color.BLUE+color.BOLD+color.ITALIC+"To retry this equation, type 'retry'; To go back to choosing another equation, type 'go back'; To exit, type 'exit': "+color.END).lower()
        
        if restart == "retry":
            print_slow(" ")
            print_slow(color.ITALIC+"Restarting..."+color.END)
            sleep(0.5)
            return main_no()
        
        elif restart == "go back":
            print(" ")
            print_slow(color.ITALIC+"Reverting back...")
            sleep(0.5)
            return choose_of_formula()
        
        elif restart == "exit":
            return exit_code()
        
        else:
            print_slow(Error.er_code_inv_inp)

def startup(num, var_1, var_2, var_3, var_4):
    print(" ")
    print("   =====================================================")
    print(color.ITALIC+f"     Value Calculator For '{num} Equation Of Motion'")
    print("\t\tProgrammed by: Mubashir78"+color.END)
    print("   =====================================================")
    sleep(1)
    
    print(" ")
    print_slow(color.BOLD+"Welcome! This little script calculates the values of '"+color.BLUE+f"{var_1}"+color.END+"','"+color.BLUE+f"{var_2}"+color.END+"','"+color.BLUE+f"{var_3}"+color.END+"' & '"+color.BLUE+f"{var_4}"+color.END+"'!")
    sleep(0.6)
    
    print("")
    print_slow(color.BOLD+"Just type in the known values one by one, marking the unknown value with "+color.UNDERLINE+"English words"+color.END+color.BOLD+" or "+color.UNDERLINE+"'?'"+color.END+color.BOLD+", and the unknown value will be automatically calculated."+color.END)
    sleep(1)

selection_of_formulae()

# Programmed by: Mubashir Ahmed OR known as Mubashir78 on Github
# https://www.github.com/Mubashir78
