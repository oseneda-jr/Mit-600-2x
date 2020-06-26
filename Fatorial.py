def Fat(n):
    if (n == 0):
        return 1
    else:
        return n * Fat(n - 1)

a = Fat(20)
print(a)