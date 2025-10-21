class Watch:
    def __init__(self, hora=0, minuto=0, segundo=0):
        self._hora = 0
        self._minuto = 0
        self._segundo = 0
        self.set_hora(hora)
        self.set_minuto(minuto)
        self.set_segundo(segundo)

    def set_hora(self, h):
        if 0 <= h <= 23:
            self._hora = h
        else:
            print("fail: hora invalida")

    def set_minuto(self, m):
        if 0 <= m <= 59:
            self._minuto = m
        else:
            print("fail: minuto invalido")

    def set_segundo(self, s):
        if 0 <= s <= 59:
            self._segundo = s
        else:
            print("fail: segundo invalido")

    def nextSecond(self):
        self._segundo += 1
        if self._segundo >= 60:
            self._segundo = 0
            self._minuto += 1
            if self._minuto >= 60:
                self._minuto = 0
                self._hora += 1
                if self._hora >= 24:
                    self._hora = 0

    def __str__(self):
        return f"{self._hora:02d}:{self._minuto:02d}:{self._segundo:02d}"


def main():
    relogio = Watch()
    while True:
        line = input()
        print("$" + line)
        args = line.split()
        if not args: continue
        cmd = args[0]

        if cmd == "end":
            break
        elif cmd == "show":
            print(relogio)
        elif cmd == "set" and len(args) == 4:
            relogio.set_hora(int(args[1]))
            relogio.set_minuto(int(args[2]))
            relogio.set_segundo(int(args[3]))
        elif cmd == "init" and len(args) == 4:
            relogio = Watch(int(args[1]), int(args[2]), int(args[3]))
        elif cmd == "next":
            relogio.nextSecond()
        else:
            print("fail: comando inválido")


main()
