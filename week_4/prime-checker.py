#Write your code below this line 👇
import math


def prime_checker(number):
    if (number <= 1):
        print(f"{number} is not prime number")
        return
    sqRoot = math.isqrt(number)
    for i in range(2, sqRoot + 1):
        if (number % i == 0):
            print(f"{number} is not prime number")
            return

    print(f"{number} is prime number")


#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
