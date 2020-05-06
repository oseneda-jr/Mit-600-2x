#Find if a str occurs in other one

def isIn(str1, str2):
    if str1 in str2:
        return True
    else:
        return False

a = isIn('cal', 'caviar')
print(a)