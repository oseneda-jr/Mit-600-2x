def fib(n):
    """Assumes n int >= 0
       Returns Fibonacci of n"""

    if n == 2:
        print("1 vez")
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def testFib(n):
    for i in range(n+1):
        print('Fib of', i , '=', fib(i))

testFib(5)
