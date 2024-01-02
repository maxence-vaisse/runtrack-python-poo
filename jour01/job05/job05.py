class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"
    def afficherX(self):
        return "Point(" + str(self.x) +")"
    def afficherY(self):
        return "Point(" + str(self.y) +")"
    def changerX(self, new_x):
        self.x = new_x
        return "Point(" + str(self.x) + ")"
    def changerY(self, new_y):
        self.y = new_y
        return "Point(" + str(self.y) + ")"

print(Point(13, 25).afficherLesPoints())
print(Point(13, 25).afficherX())
print(Point(13, 25).afficherY())
print(Point(13, 25).changerX(14))
print(Point(13, 25).changerY(56))
