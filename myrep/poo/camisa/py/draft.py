
class Camisa:
    def __init__(self): 
        self.__tamanho: str = "" 

    def getTamanho(self) -> str: 
        return self.__tamanho

    def setTamanho(self, valor: str):  
        valor = valor.upper()  
        if valor not in ['PP','P', 'M', 'G', 'GG', 'XG']:
            print('Inválido')
        else:
            print('Válido')
        self.__tamanho = valor 
 

roupa = Camisa() 

while roupa.getTamanho() == "": 
    print("Digite seu tamanho de roupa")
    tamanho = input() 
    roupa.setTamanho(tamanho) 

print("Parabens, você comprou uma roupa tamanho", roupa.getTamanho())