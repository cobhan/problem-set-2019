# Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.

for i in range(1000,10000):
    if i % 6 == 0 and i % 12 != 0:
        print(i)

# https://stackoverflow.com/questions/8002217/how-do-you-check-whether-a-number-is-divisible-by-another-number-python/8002234