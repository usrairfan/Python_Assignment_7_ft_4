class Person:
    def __init__(self,color,height,weight,secret):
      self.color = color
      self.height = height
      self.weght = weight
      self.__secret = secret
    def talking(self):
       print("talking...")
        
    def sleeping(self):
       print('sleeping...')
    def get__secret(self):
       return self.__secret
Person1 = Person("white","5'5","150 lbs","bank balance")
Person2 = Person("black","6'4","180 lbs", "numbers")
Person1.talking()
print(Person1.color)
print(Person2.color)
print(Person1.get__secret())

Person2.sleeping



class Car:
   def __init__(self, color, speed):
      self.color = color
