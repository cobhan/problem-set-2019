# 1. sumupto.py
# 1. Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number.

n = int(input("Please enter a positive integer:"))
i = list(range(1,n + 1))

sum = sum(i)

print(sum)