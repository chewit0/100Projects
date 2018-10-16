import random


def integerInput(message='Enter integer: '):
    '''
    Asks user for integer until one is passed
    '''
    repeat = True
    number = 'a'

    while repeat:
        try:
            number = int(number)
            repeat = False
        except:
            number = input(message)
    return number


def coinflip(number):
    coin = ['H', 'T']
    result = {'H': 0, 'T': 0}

    for i in range(0, number):
        result[random.choice(coin)] += 1

    print("\nAfter {} flips:\n\nHeads: {}\nTails: {}\n".format(
        number, result['H'], result['T']))


def main():
    coinflip(userinput("Enter number of coin flips: "))

main()
