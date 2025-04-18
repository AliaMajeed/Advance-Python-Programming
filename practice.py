#Example #01
#Write a program to take a number as a input and print out whether it is divisble by 3 or 5,
#  or both 3 and 5
# Take a number as input
number = int(input("Enter a number: "))


if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by both 3 and 5.")
elif number % 3 == 0:
    print("The number is divisible by 3.")
elif number % 5 == 0:
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 3 or 5.")

#Example #02
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Take input
n = int(input("Enter an integer: "))

# Check conditions
if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")




