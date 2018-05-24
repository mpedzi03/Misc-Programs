# Student: Michael Pedzimaz
# 3/27/2018
#
# Recursive Non-User-Responsiveness Version 1.0

def FactorialRecursive(n):
    if (n < 1):
        return 1
    else:
        returnNumber = n * FactorialRecursive(n - 1)
        return returnNumber
    
def main():
    num = 2
    while (num == 2 or num == 3 or num == 4):   
        factorialValue = FactorialRecursive(num)
        print 'The factorial of ' +str(num)+ ' is ' +str(factorialValue)+' .\n'
        num = num + 1

    
if __name__ == '__main__':
    main()
