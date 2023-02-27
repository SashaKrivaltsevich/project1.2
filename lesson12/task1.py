class Vector:
    def __init__(self, point1,point2):
        self.point1 = point1
        self.point2 = point2

    def length(self):
        x1, y1 = self.point1
        x2, y2 = self.point2
        length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        return length

    def __eq__(self, other):
        return self.length() == other.length()

    def __ne__(self, other):
        return self.length() != other.length()

    def __gt__(self, other):
        return self.length() > other.length()

    def __lt__(self, other):
        return self.length() < other.length()

    def __ge__(self, other):
        return self.length() >= other.length()

    def __le__(self, other):
        return self.length() <= other.length()


vector1 = Vector((1, 1), (2, 2))
vector2 = Vector((1, 1), (4, 4))

print(vector1 == vector2)
print(vector1 != vector2)
print(vector1 > vector2)
print(vector1 < vector2)
print(vector1 >= vector2)
print(vector1 <= vector2)


