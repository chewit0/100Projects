#**Find PI to the Nth Digit** 
#Enter a number and have the program generate PI up to that many decimal places. 
#Keep a limit to how far the program will go. (10000)
#uses Chudnovsky algorithm https://en.wikipedia.org/wiki/Chudnovsky_algorithm

import math
from decimal import Decimal, getcontext as gc

def user_input(min, max):
    digits = 0

    while ( min > digits or digits > max):
        digits = input("Enter number of decimal places for pi")
        try: 
            digits = int(digits)
        except:
            digits = 0

    return digits

def pi_to_n(digits):

    X, M, K, L, S = 1, 1, 6, 13591409, 13591409
    C = Decimal(426880* math.sqrt(10005))
    gc().prec = 1000

    for k in range (1, 70):
            
        M += M * (K**3 - 16*K) / k**3
        K += 12
        X *= -262537412640768000
        L += 545140134
        S += Decimal( M * L ) / X

    pi = C/S
    pi = Decimal(str(pi)[:digits+2])

    print(pi)
    return pi

if __name__ == "__main__":
    pi = pi_to_n(user_input(1,100))
