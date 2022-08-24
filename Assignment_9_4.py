# Write a python script to print first N odd natural numbers

n = int(input("Enter a natural number: "))
i = 1
while i <= n:
    print(i * 2 - 1, end=" ")
    i += 1
