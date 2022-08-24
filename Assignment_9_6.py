# Write a python script to print first N even natural numbers

n = int(input("Enter a natural number: "))
i = 1
while i <= n:
    print(i * 2, end=" ")
    i += 1
