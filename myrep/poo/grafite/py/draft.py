class Grafite:
    def __init__(self, thickness:float, hardness:str, size:int):
        self.thickness = thickness
        self.hardness = hardness
        self.size = size 
    
    def usePerSheet(self):
        gastos = {'HB':1, '2B':2, '4B':4, '6B':6}
        return gastos.get(self.hardness, None)
    
    def __str__(self):
        return f"{self.thickness}:{self.hardness}:{self.size}" 
    
class Pen:
    def __init__(self, thickness:float):
        self.__thickness = thickness
        self.__tip = None

    def hasGrafite(self) -> bool:
        return self.__tip is not None
    
    def insert(self, grafite:Grafite) -> bool:
        if self.hasGrafite():
            print("fail: ja existe grafite")
            return False
        if grafite.thickness != self.__thickness:
            print("fail: calibre incompativel")
            return False
        self.__tip = grafite
        return True 
    
    def __str__ (self):
        if self.hasGrafite():
            return f'calibre: {self.__thickness}, grafite: [{self.__tip}]'
        else:
            return f'calibre: {self.__thickness}, grafite: null'
        
    def remove(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return None
        removed = self.__tip
        self.__tip = None
        return removed
    
    def writePage(self):
        if not self.hasGrafite():
            print('fail: nao existe grafite')
            return False
        
        grafite = self.__tip
        gasto = grafite.usePerSheet()

        if gasto is None:
            print('fail: dureza invalida')
            return False
        
        if grafite.size <= 10:
            print('fail: tamanho insuficiente')
            grafite.size = 10
            return False
        
        grafite.size -= gasto

        if grafite.size < 10:
            grafite.size = 10
            print('fail: folha incompleta')

        return True
    
def main():
    lapiseira = None

    while True:
        line = input()
        print("$" + line)
        args = line.split()
    
        if args[0] == "end":
            break
        elif args[0] == 'show':
            if lapiseira is not None:
                print(lapiseira)
            else:
                print('fail: lapiseira nao inicializada')
        elif args[0] == 'init':
            calibre = float(args[1])
            lapiseira = Pen(calibre)
        elif args[0] == 'insert':
            if lapiseira:
                espessura = float(args[1])
                dureza = args[2]
                tamanho = int(args[3])
                grafite = Grafite(espessura, dureza, tamanho)
                lapiseira.insert(grafite)
            else:
                print('fail: lapiseira nao inicializada')
        elif args[0] == 'remove':
            if lapiseira:
                lapiseira.remove()
            else:
                print('fail: lapiseira nao inicializada')
        elif args[0] == 'write':
            if lapiseira:
                lapiseira.writePage()
            else:
                print('fail: lapiseira nao inicializada')

main()
    

       
        