class ShoppingCart:

 def add_item(self,age,count):
     self.count = count
     self.age = age
     self.bool1 = "True"
     bool1 = True

     print(f"{age}, {count},{bool1}")

obj1: ShoppingCart = ShoppingCart()
obj2: ShoppingCart = ShoppingCart()
obj2.bool1 = False
#

obj1.add_item(20,1)
obj2.add_item(20,1)
