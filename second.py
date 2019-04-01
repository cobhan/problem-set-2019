# 9. Write a program that reads in a text file and outputs every second line. The program should take the filename from an argument on the command line.

m = open("moby10b.txt") #open the file

for count, line in enumerate(m, start=1): #create count and line variables using the enumerate function which adds a counter to an iterable. 
    if count % 2 == 0: # check if the line number is evenly divisible by 2
        print(line)  # if so, print on 

m.close() # close our moby file

# reference https://cmdlinetips.com/2011/08/three-ways-to-read-a-text-file-line-by-line-in-python/