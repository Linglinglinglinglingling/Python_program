#the first two numbers of a Fibonacci sequence could be either 0 and 1 or 1 and 1;
#  and each of the subsequent numbers is the sum of the previous two numbers.

#0, 1, 1, 2, 3, 5, 8, 13 ...

#1, 1, 2, 3, 5, 8, 13 ...


#calculate the nth number's value
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    a=fibonacci(50)
    print(a)