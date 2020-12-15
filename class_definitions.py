import matplotlib.pyplot as plt

class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return f"Point ({self.x}, {self.y})"

  def __repr__(self):
    return self.__str__()

  def plot(self, ax):
    ax.scatter(self.x, self.y, s=6.0)

class LineSegment:

  def __init__(self, p1, p2):
    self.p1 = p1
    self.p2 = p2
    self.calculate_value(self.first().x)

  def first(self):
    if self.p1.x <= self.p2.x:
      return self.p1

    else:
      return self.p2

  def second(self):
    if self.p1.x <= self.p2.x:
      return self.p2

    else:
      return self.p1

  def calculate_value(self, val):
    x1 = self.first().x
    x2 = self.second().x
    y1 = self.first().y
    y2 = self.second().y
    self.value = y1 + (((y2 - y1) / (x2 - x1)) * (val - x1))

  def plot(self, ax):
    ax.plot([self.first().x, self.second().x], [self.first().y, self.second().y])
    ax.scatter([self.first().x, self.second().x], [self.first().y, self.second().y], s=4.0)

  def __eq__(self, other):
    return self.value == other.value

  def __lt__(self, other):
    return self.value < other.value

  def __le__(self, other):
    return self.value <= other.value

  def __gt__(self, other):
    return self.value > other.value

  def __ge__(self, other):
    return self.value >= other.value

  def __str__(self):
    return f"<line segment with endpoints {self.p1} and {self.p2} and value = {self.value}>"

  def __repr__(self):
    return self.__str__()

class Event:
  def __init__(self, p, ls, t):
    self.point = p
    self.linesegments = ls
    self.value = p.x
    self.type = t

  def add_segment(self, s):
    self.linesegments.append(s)

  def __eq__(self, other):
    return self.value == other.value

  def __lt__(self, other):
    return self.value < other.value

  def __le__(self, other):
    return self.value <= other.value

  def __gt__(self, other):
    return self.value > other.value

  def __ge__(self, other):
    return self.value >= other.value

  def __str__(self):
    return f"Event with point <{self.point}>, line segment(s) {self.linesegments}, value = {self.value},  ET= {self.type}"

  def __repr__(self):
    return self.__str__()