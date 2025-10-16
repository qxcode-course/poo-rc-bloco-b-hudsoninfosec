
class Camisa:
    def __init__(self): # isso é o construtor em python
        self.__tamanho: str = "" # atributos em python com __ na frente são privados

    def getTamanho(self) -> str: # métodos em python tem self como primeiro atributo
        return self.__tamanho

    def setTamanho(self, valor: str):  
        valor = valor.upper()  # implementar os testes de valor e disparar os avisos caso necessário
        if valor not in ['PP','P', 'M', 'G', 'GG', 'XG']:
            print('Inválido')
        else:
            print('Válido')
        self.__tamanho = valor 
 
# loop principal
roupa = Camisa() # criando roupa com valor tamanho padrão

while roupa.getTamanho() == "": # mantendo usuário no loop
    print("Digite seu tamanho de roupa")
    tamanho = input() # lendo a resposta
    roupa.setTamanho(tamanho) # tentando atribuir e disparando erros

print("Parabens, você comprou uma roupa tamanho", roupa.getTamanho())