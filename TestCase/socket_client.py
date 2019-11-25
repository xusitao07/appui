class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector-- (%d, %d)' % (self.a, self.b)

   def __add__(self,too):
       print("输出{}".format(too))
       print("相加{}".format(self.a + too.a))
       return Vector(self.a + too.a, self.b + too.b)


v1 = Vector(2,10)
v2 = Vector(5,-2)

print (v1 + v2)