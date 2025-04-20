# Example 1
# Define a program to find out whether a given number is even or odd.
# Using list indexing
num = int(input("Enter a number: "))

# List where index 0 = Even, index 1 = Odd
result = ["Even", "Odd"]

print(result[num % 2])
 
#2nd Method
#Without function, using simple if-else
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


#Example 2
#Define a method to find out if a number is prime or not.
def is_prime(n):
    if n <= 1:
        return False # 0 and 1 are not prime numbers
    for i in range(2, n):  #check every number from 2 up to (n-1).
        if n % i == 0:
            return False  # if divisible, not prime
    return True  # if no divisors found, it is prime

num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

#Example 3
#Write a function to find if a number is a palindrome or not. Take number as parameter.
def is_palindrome(n):
    # Convert the number to string
    n_str = str(n)
    
    # Check if the string is same when reversed
    if n_str == n_str[::-1]:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(num, "is a palindrome.")
else:
    print(num, "is not a palindrome.")
