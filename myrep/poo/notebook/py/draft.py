class Notebok:
    def __init__(self):
        self.__ligado: bool = False

    def ligar(self):
        if not self.__ligado:
            self.__ligado = True
            print("notebook ligado.")
        else:
            print("erro: notebook já está ligado")

    def desligar(self):
        if self.__ligado:
            self.__ligado = False
            print("notebook desligado.")
        else:
            print("erro: notebook já está desligado")

    def mostrar(self):
        status = "ligado" if self.__ligado else "desligado"
        print(f"O notebook está {status}.")

    def usar(self, tempo):
        if self.__ligado:
            print(f"Usando o notebook por {tempo} minutos.")
        else:
            print("erro: não é possível usar o notebook desligado.")