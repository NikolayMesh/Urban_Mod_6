class Horse:
    def __init__(self):
        self.x_distance = 0 #пройденный путь.
        self.sound = 'Frrr' #звук, который издаёт лошадь.

    def run(self, dx):
        self.x_distance = int(self.x_distance) + int(dx) # движение

class Eagle:
    def __init__(self):
        self.y_distance = 0 # высота полёта
        self.sound = 'I train, eat, sleep, and repeat' # звук, который издаёт орёл (отсылка)

    def fly(self, dy):
        self.y_distance = int(self.y_distance) + int(dy) # полёт


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self) # наследование от коня
        Eagle.__init__(self) # наследование от орла

    def move(self, dx, dy):
        super().run(dx) #пройденный путь.
        super().fly(dy) # высота полёта

    def get_pos(self):
        return self.x_distance, self.y_distance


    def voice(self):
       print(self.sound)


if __name__ == '__main__':
    p1 = Pegasus()
    print(p1.get_pos())

    p1.move(10, 15)
    print(p1.get_pos())

    p1.move(-5, 20)
    print(p1.get_pos())

    p1.voice()
