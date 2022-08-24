""" 
Write a python script to print first N odd natural numbers
in reverse order
"""

n = int(input("Enter a natural number: "))
i = 1
while n >= i:
    print(n * 2 - 1, end=" ")
    n -= 1
