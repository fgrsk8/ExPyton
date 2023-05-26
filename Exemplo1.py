class Point:
    def __int__(self, x=0, y=0,):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x

    def sety(self, y):
        self.y

    def get(self):
        return self.x, self.y

    def move(self, offsetx, offsety):
        self.x += offsetx
        self.y += offsety

    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'


