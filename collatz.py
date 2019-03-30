# Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.
x = int(input("Please enter a positive integer: "))
print(x)
while x != 1:
    if x%2 == 0:
        x = x // 2
        print(x)
    else: 
        x = (x*3) + 1
        print(x)
    
# https://www.reddit.com/r/Python/comments/57r6bf/collatz_conjecture_program/


    