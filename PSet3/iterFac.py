def iterFac(n):
    """assumes that n is an int > 0
        returns n!"""
    res = 1
    while n > 1:
        res = res * n
        n -= 1
    return res
    
r = iterFac(2,3)
print r