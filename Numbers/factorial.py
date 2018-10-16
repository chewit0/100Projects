

def integerInput(message='Enter integer: '):
    repeat = True
    number = 'a'

    while repeat:
        try:
            number = int(number)
            repeat = False
        except:
            number = input(message)
    return number


def factorial(num):
    '''Calculates and prints factorial of given integer'''
    total = 0
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
    

def main():
    integer = integerInput("Enter integer for factorial: ")
    print("{}! = {}".format(integer, factorial(integer)))

if __name__ == "__main__":
    main()
