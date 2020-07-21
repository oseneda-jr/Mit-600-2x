def sumDigit(s):
    """Assumes s is a string
       Returns the sum of decimal digits in s
       For example, if s = 'a2b3c' it returns 5"""
    
    soma = 0
    for ch in s:
        try:
            val = int(ch)
            soma += val
        except:
            continue
    if soma == 0:
        print('Não há digitos numéricos a somar!')
    else:
        print(soma)

s = '3b3dhxddd45'
a = sumDigit(s)