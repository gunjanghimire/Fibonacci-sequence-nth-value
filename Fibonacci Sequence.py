#Author: Gunjan Ghimire, 3/7/2019

#Formula that calculates the fibonacci sequence based on user input
UserInput = int(input("How many numbers do you want on the sequence: ")) #Ask the User for the input

i =0 #Initialize the for loop counter to Zero 
a= [] #Initialize a list with zero elements which we can append to add numbers

for i in range(i, UserInput): #Specify the range of the for loop from 0 to the User input of numbers
    
    if i==0: #If the Counter is zero, loop appends zero to the list
        temporary = 0
    
    elif i == 1: #If the counter is 1, loop appends 1 to the list
        temporary = 1
    
    else: #If the counter is anything else, loop appends sum of two previous numbers to the list
        temporary = a[i-1] + a[i-2]
        
    a.append(temporary) #The sum of previous number was stored as a temporary variable aptly name temporary which is appended here to the list
 
#Here we print our list 
print('The sequence based on your need of individual numbers is as follows:')
print(a)
