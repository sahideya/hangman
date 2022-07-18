import math

class Apple():
  def __init__(self, w, c, s, l):
    #wは重さ、cは色、sは甘さ、lは大きさ
    self.weight = w
    self.color = c
    self.suit = s
    self.large = l


class Circle():
  def __init__(self, r):
    self.radius = r

  def area(self):
    return self.radius ** 2 * math.pi

circle1 = Circle(3)
print(circle1.area())


class Triangle():
  def __init__(self, base, height):
    self.base = base
    self.height = height

  def area(self):
    return self.base * self.height / 2

triangle = Triangle(5, 3)
print(triangle.area())

class Hexagon:
  def __init__(self, side):
    self.side = side
  
  def length(self):
    return self.side * 6

hexagon = Hexagon(5)
print(hexagon.length())

