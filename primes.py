# Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime.

n = int(input("Please enter a positive integer: "))


def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(test_prime(n))

# https://www.w3resource.com/python-exercises/python-functions-exercise-9.php