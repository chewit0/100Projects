'''
unit converter, to convert temperature, currencies(scrape latest exchange rates), distances, weights
'''
from forex_python.converter import CurrencyRates

def int_input(min = -float('inf'), max = float('inf'), string = "Enter value: "):
    '''asks for integer input between min max with a custom input message'''
    
    while True:
        try:             
            value = int(input(string))
        except:
            print("Enter int: ")
        else:
            break    
    
    while not (min<value<max):
        try:
            value = int(input(string))
        except:
            print("Enter int: ")
    return value

def choose_convert():
    choice = 0
    while  not (0 < choice < 6 ):
        try:
            choice = int(input("Enter the type you want to convert \n 1: Temperature \n 2: Weights \n 3: Currency \n 4: Distances \n 5: Quit \n"))
        except: 
            print("Please enter an integer: ")
    return choice

def convert_init(choice):
    #based on choice, set up calls for other functions
    if choice == 1:
        #temp, passed unit and value
        temp_unit = ''
        temp_value = 0

        while not (temp_unit in ['c', 'f', 'C', 'F']):
            temp_unit = input("Enter unit to convert from (C/F):\n")
        
        temp_value = int_input(string = "Enter temperature: ")

        converted = temp_convert(temp_unit, temp_value)
        print(converted)
    
    elif choice == 2:
        weight_unit = ''
        while not (weight_unit in ['kg', 'lbs', 'st']):
            weight_unit = input("Enter weight unit (lbs, st, kg): ")

        weight = int_input(0, string= "Enter Weight: ")

        converted = weight_convert(weight_unit, weight)
        print(converted)

    elif choice ==3:
        converted = currency_converter()
        print(converted)
    elif choice ==4:
        dist_unit = ''
        while not dist_unit in ['m','km']:
            dist_unit = input("Enter distance unit to convert (km, m): ")
        distance = int_input()

        converted = distance_converter(dist_unit, distance)
        print(converted)

def temp_convert(passedUnit, value):
    if passedUnit == 'c':
        temp = value / (5/9) + 32
    else: 
        temp = (value - 32) * (5/9)
    return temp

def weight_convert(passedUnit, value):
    
    if passedUnit == 'st':
        value = value*14
    
    if passedUnit == 'kg':
        weight = value * 2.2046226218
    else: 
        weight = value / 2.2046226218
    return weight

def currency_list():

    c = CurrencyRates()
    rates = c.get_rates('AUD')     
    choice_list = ['AUD']

    for line in rates.keys(): 
        choice_list.append(line)             
    return choice_list

def choose_currency(base = True):
    
    cl = currency_list()
    
    print("Available currencies: \n")

    i=0 
    for line in cl:            
        print("{}: {}".format(i, line))
        i+=1

    if base:
        string = "Select a currency (by number): "
    else:
        string = "Select a currency to convert to (by number): "

    choice = int_input(0, i, string)
        
    return cl[choice]

def currency_converter():
    
    base = choose_currency(True)
    dest = choose_currency(False)
    
    c = CurrencyRates()

    amount = 0
    msg_str = "Enter amount of {} to convert to {}: ".format(base, dest)

    amount = int_input(0, string=msg_str)    

    converted = c.convert(base, dest, amount)
    return converted

def distance_converter(passedUnit, value):
    if passedUnit == 'm':
        distance = value * 1.60934
    else:
        distance = value / 1.60934
    return distance

def main():

    quit = ''
    while not quit in ['y','Y']:
        choice = choose_convert()
        if choice == 5: break
        convert_init(choice)
        quit = input("quit? (y/n)")

if __name__ == "__main__":
    main()







