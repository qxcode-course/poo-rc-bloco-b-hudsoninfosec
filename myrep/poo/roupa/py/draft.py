
class Roupa:
    def __init__(self): # isso é o construtor em python
        self.__tamanho: str = "" # atributos em python com __ na frente são privados

    def getTamanho(self) -> str: # métodos em python tem self como primeiro atributo
        return self.__tamanho

    def setTamanho(self, valor: str):  
        valor = valor.upper()  # implementar os testes de valor e disparar os avisos caso necessário
        if valor not in ['PP','P', 'M', 'G', 'GG', 'XG']:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
        else:
            self.__tamanho = valor 
 
def main():
    
    roupa = Roupa() 

    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split()

        if len(args) == 0:
            continue
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(f"size: ({roupa.getTamanho()})")
        elif args[0] == "size":
            if len(args) > 1:
                roupa.setTamanho(args[1])
            else:
                print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
main()


