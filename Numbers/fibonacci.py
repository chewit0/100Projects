#Fibonacci up to n

def user_input(min, max):
    digits = 0

    while ( min > digits or digits > max):
        digits = input("Enter number, n, between {} and {} to generate fibonacci up to n: ".format(min, max))
        try: 
            digits = int(digits)
        except:
            digits = 0

    return digits

def fib(n):
    
    prev, curr = 1, 1 #First two numbers 
    i=0

    while (i < n):
        print(prev)        
        temp = curr
        curr = prev + curr
        prev = temp
        i += 1

fib(user_input(1, 10))   