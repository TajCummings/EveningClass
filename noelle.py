def author_sig():
    print("Noelle Adkin")
    print("CPT051")
    print("noelle.py")
    print("October 2020")
    print("--------------------")

TAX = .01
CURRENCY = " Gold pieces"

wizard_hat_price = 100
magic_sword_price = 200
health_potion = 10

def show_buy_menu():
    print("What are you buying?")
    print("A.)" +"Wizard hat : " + str(wizard_hat_price) + CURRENCY)
    print("B.)" +"Magic Sword : " + str(magic_sword_price) + CURRENCY)
    print("C.)" +"Health Potion : " + str(health_potion) + CURRENCY)
    print("* Taxes not included")

def take_input():
    print("Enter your Selection here:")
    selection = input()
    return selection

def error_message():
    print("Error")

def name_of_function():
    print("Code statment 1")
    print("Code statment 2")

    print("code statment 3")

#functions above
#------------------------------------Main-------------------------
#code below
author_sig() #Terminal/start

show_buy_menu() #output

menu_select = take_input() #input

print("You selected : " + menu_select) #output
print("First letter : " + menu_select[0]) #output

    
