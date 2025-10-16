class Chinela:
    # inicialização da chinela com valor de tamanho 0
    def __init__(self):    # isso é o construtor em python
        self.__tamanho = 0 # quando tem __ na frente em python é privado

    def getTamanho(self): # métodos em python tem self como primeiro atributo
        return self.__tamanho

    def setTamanho(self, valor: int):
        if valor % 2 != 0:
            print('Erro: o tamanho deve ser um número PAR.')
        elif valor < 20 or valor > 50:
            print('Erro: o tamanho deve estar entre 20 e 50.')
        else:
            self.__tamanho = valor
            print('Tamanho válido! Chinela Ajustada.')
# loop principal
chinela = Chinela() # criando chinela com valor tamanho padrão

while chinela.getTamanho() == 0: # mantendo usuário no loop
    print("Digite seu tamanho de chinela: ")
    try:
        tamanho = int(input()) # lendo a resposta e convertendo pra inteiro
        chinela.setTamanho(tamanho) # tentando atribuir e disparando 
    except ValueError:
        print('Erro: Digite apenas números inteiros.')

print("Parabens, você comprou uma chinela tamanho", chinela.getTamanho())