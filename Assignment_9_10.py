# Write a python script to print first 10 multiples of N

n = int(input("Enter a natural number: "))
i = n
while i <= n * 10:
    print(i, end=" ")
    i += n
 