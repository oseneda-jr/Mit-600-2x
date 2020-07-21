def abs(x):
    """Assume x i a int
       Returns x if x >= 0; -x otherwhise"""

    if x < 0:
        return -x
    else:
        return x

a = abs(-0.0000000000000000000000000000000000001)