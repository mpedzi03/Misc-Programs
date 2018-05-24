# Student: Michael Pedzimaz
# 3/27/2018
#
# Iterative Non-User-Responsiveness Version 1.0

def FactorialIterative(n):
    _sum = 1
    if (n <= 1):
        return _sum
    while (n > 1):
        _sum *= n
        n = n - 1
    return _sum

def main():
    num = 2
    while (num == 2 or num == 3 or num == 4):   
        factorialValue = FactorialIterative(num)
        print 'The factorial of ' +str(num)+ ' is ' +str(factorialValue)+' .\n'
        num = num + 1

if __name__ == '__main__':
    main()
