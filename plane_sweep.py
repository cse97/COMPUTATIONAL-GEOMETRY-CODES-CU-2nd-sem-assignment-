import avl_tree
from class_definitions import *
import matplotlib.pyplot as plt

class Intersection:
  def __init__(self, linesegments):
    self.pQ = []
    self.sL = avl_tree.AVL()
    self.points = []
    self.linesegments = linesegments

    for s in linesegments:
      self.pQ.append(Event(s.first(), [s], 0))
      self.pQ.append(Event(s.second(), [s], 1))

  def recalculate(self, l):
    for ls in self.linesegments:
      ls.calculate_value(l)

  def find_intersections(self, fout):
    while(self.pQ != []):
      #print(self.pQ)
      e = min(self.pQ)
      self.pQ.remove(e)
      fout.write(f'Encounted :: {e}\n')
      l = e.value

      if(e.type == 0):
        fout.write(f'ADDED in Sweep line status :: {e.linesegments[0]}\n\n')
        for s in e.linesegments:
          self.recalculate(l)
          self.sL.insert(s)
          if(self.sL.predecessor(s) != None):
            r = self.sL.predecessor(s).key
            self.reportIntersection(r, s, l, fout)
          if(self.sL.successor(s) != None):
            t = self.sL.successor(s).key
            self.reportIntersection(t, s, l, fout)
          if(self.sL.predecessor(s) != None and self.sL.successor(s) != None):
            r = self.sL.predecessor(s).key
            t = self.sL.successor(s).key
            self.removeFuture(r, t)

      elif(e.type == 1):
        fout.write(f'DELETED from Sweep line status :: {e.linesegments[0]}\n\n')
        for s in e.linesegments:
          if(self.sL.predecessor(s) != None and self.sL.successor(s) != None):
            r = self.sL.predecessor(s).key
            t = self.sL.successor(s).key
            self.reportIntersection(r, t, l, fout)
          self.sL.delete(s)

      elif(e.type == 2):
        s1 = e.linesegments[0]
        s2 = e.linesegments[1]
        fout.write(f'SWAP in Sweep line status :: {s1} and {s2}\n\n')
        self.swap(s1, s2)
        if(s1.value < s2.value):
          self.handleIntersection(l, s1, s2, fout)
        else:
          self.handleIntersection(l, s2, s1, fout)
        self.points.append(e.point)
    

  def handleIntersection(self, l, s1, s2, fout):
    if(self.sL.successor(s1) != None):
      t = self.sL.successor(s1).key
      self.reportIntersection(t, s1, l, fout)
      self.removeFuture(t, s2)

    if(self.sL.predecessor(s2) != None):
      r = self.sL.predecessor(s2).key
      self.reportIntersection(r, s2, l, fout)
      self.removeFuture(r, s1)

  def reportIntersection(self, s1, s2, L, fout):
    x1 = s1.first().x
    y1 = s1.first().y
    x2 = s1.second().x
    y2 = s1.second().y
    x3 = s2.first().x
    y3 = s2.first().y
    x4 = s2.second().x
    y4 = s2.second().y
    r = (x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3)
    
    if(r != 0):
      t = ((x3 - x1) * (y4 - y3) - (y3 - y1) * (x4 - x3)) / r
      u = ((x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1)) / r
      if(t >= 0 and t <= 1 and u >= 0 and u <= 1):
        x_c = x1 + t * (x2 - x1);
        y_c = y1 + t * (y2 - y1);
        if(x_c > L):
          nP = Point(x_c, y_c)
          fout.write("-------------------------\n")
          fout.write(f'Intersection found and added between {s1} and {s2}. New point added : {nP}\n')
          fout.write("-------\n\n")
          self.pQ.append(Event(nP, [s1, s2], 2))
  
  def removeFuture(self, s1, s2):
    for e in self.pQ:
      if(e.type == 2):
        if((e.linesegments[0] == s1 and e.linesegments[1] == s2) or (e.linesegments[0] == s2 and e.linesegments[1] == s1)):
          self.pQ.remove(e)
  
  def swap(self, s1, s2):
    self.sL.delete(s2)
    self.sL.delete(s1)
    value = s1.value
    s1.value = s2.value
    s2.value = value
    self.sL.insert(s1)
    self.sL.insert(s2)

  def printIntersections(self, fout):
    fout.write("Intersection points found : \n\n")
    for p in self.points:
      fout.write("({}, {})\n".format(p.x, p.y))
    fout.write(f"\nNo. of Intersection points : {len(self.points)}\n\n")
    
ls = []
fl = open("/home/debapriya/Desktop", 'r')

for l in fl:
  st = l.split(' ')
  p1 = Point(float(st[0]), float(st[1]))
  p2 = Point(float(st[2]), float(st[3][:-1]))
  ls.append(LineSegment(p1, p2))

fout = open("/home/debapriya/Desktop", "w+")

fig, ax = plt.subplots()
for l in ls:
  l.plot(ax)

test = Intersection(ls)
test.find_intersections(fout)

fout.write('-------   Compltete   -------\n\n')
test.printIntersections(fout)
fout.close()

for p in test.points:
  ax.scatter(p.x, p.y, s=4.0)

plt.show()