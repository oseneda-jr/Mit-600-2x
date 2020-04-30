class Touro(object):
    def __init__(self, p, c, b):
        self.peso = p
        self.cor = c
        self.nasc = b
        
    def __str__(self):
        return str(self.peso) + self.cor +str(self.nasc)
    
touro1 = Touro(15, 'Branco', 2015)

print(touro1)