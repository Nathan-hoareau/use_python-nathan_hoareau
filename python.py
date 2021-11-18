####Part1####

###Step1###

##Step1.1##

#Exercice1.1.1#

fruit = "apples"
quant = 5
pie_crust = "empty"
isOvenOn = True


print(f'''You have {quant} {fruit} and the pie crust is {pie_crust}, is the
oven on ? {isOvenOn}''')

##Step1.2##

def print_hello_please():
    print("Hello")

def print_hello_with_my_name(myName):
    print("Hello", myName)

def calc_my_age_in_two_years(myCurrentAge):
    print(f"You are {myCurrentAge} years old")
    my_age_in_two_years = myCurrentAge + 2
    return my_age_in_two_years

print_hello_please()
print_hello_with_my_name("Nathan")
my_age_in_two_years = calc_my_age_in_two_years(19)

print(f"In two years, i'll be {my_age_in_two_years} years old")

#Exercice1.2.1#

fruit = "banana"
quant = 7
pie_crust = "empty"
isOvenOn = False

def prepMyFruit(quant, fruit, pie_crust):
    print(f"You put {quant} {fruit}s on the crust")
    pie_crust = f"filled with delicious {fruit}s"
    return pie_crust

pie_crust = prepMyFruit(quant, fruit, pie_crust)
print("my pie is", pie_crust)

#Exercice1.2.2#

fruit = "apple"
quant = 5
pie_crust = "empty"
isOvenOn = False

def turn_on_oven(isOvenOn):
    isOvenOn = True
    return isOvenOn

pie_crust = prepMyFruit(quant, fruit, pie_crust)
isOvenOn = turn_on_oven(isOvenOn)
print("my pie is", pie_crust)
print("Is the oven turned on ?", isOvenOn)

def cookDaPie(crust):
    print(f"You pie {crust} is cooked, Bon appetit")

cookDaPie(pie_crust)

####Part2####

def dice_roll_res(dice_value1 , dice_value2):
    if dice_value1 == dice_value2:
        return("Same value , play again")
    if dice_value1 == 1 or dice_value2 == 1:
        return("too bad you lose")
    elif dice_value1 % 2 == 0 and dice_value2 % 2 != 0:
        return("you win")
    else:
        return("nothing happen ...")

print(dice_roll_res(1,3))
print(dice_roll_res(3,3))
print(dice_roll_res(6,3))
print(dice_roll_res(7,3))

#Exercice2.1#

def ask_me_adout_string(string):
    if (string[0] == 'a' or string[0] == 'A'):
        print(f"that's an A")
    if (len(string) < 5):
        print(f"error, need longer string")
    if (string[0] == string[len(string) - 1] or string[0] == string[len(string) - 1].upper()):
        print("they are the same O_O")

ask_me_adout_string("rat")
ask_me_adout_string("alpaga")
ask_me_adout_string("ALPAGA")
ask_me_adout_string("KayAk")
ask_me_adout_string("ce workshop me rapporte 2 xp merci")

####Part3####

##Step3.1##

#Exercice 3.1.1#

import sys 

def get_sys_argc():
    return len(sys.argv)

get_sys_argc()

#Exercice 3.1.2#

import sys as sy

def get_sy_argc():
    return len(sy.argv)

get_sy_argc()

#Exercice 3.1.3#

from sys import *

def get_sys_argc():
    return len(argv)

get_sys_argc()

#Exercice 3.1.4#

from sys import *

def get_sys_argc():
    try:
        print("You must only import the argv methode", file=stdout)
    except:
        print("Success")
    return len(argv)

get_sys_argc()