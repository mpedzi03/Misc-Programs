# Student: Michael Pedzimaz
# 3/27/2018
#
# Recursive User-Responsive Version 1.0
import sys

# Function used to calculate the factorial of the passed in number. 
def CalculateFactorial(number):
    factorial = 1
    if number < 0:
        print("Sorry, you cannot have a factorial for a negative number")
    elif number == 0:
        print("The factorial for 0 is 1")
    else:
        for i in range(1, number+1):
            factorial = factorial*i
        print("The factorial of ",number," is ", factorial)

# Function used for the View, or interactivity with the user, in our program. 
def main():
    chosenNumber = input("Which number would you like to find the factorial of? ")
    CalculateFactorial(chosenNumber)
    print("Would you like to try another number? (Y/N) ")
    answer = raw_input("")
    while answer.strip() == 'Y':
        main()    
    sys.exit()


if __name__ == '__main__':
    main()

    
    
        
    
        
    
    
    
    
