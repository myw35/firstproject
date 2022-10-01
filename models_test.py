
# import os
# from django.core.wsgi import get_wsgi_application
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
# application = get_wsgi_application()


# from MTV.models import Question, Answer

# def R_create():
#   Q = Question.objects.get(id=1)
#   Q.answer_set.create(content='Office Worker')
#   print("Answer List:", Q.answer_set.all())

# def R_delete():
#   Q = Question.objects.get(id=1)
#   A = Answer.objects.get(content__contains='Office Worker')
#   A.delete()
#   print("Answer List:", Q.answer_set.all())

# if __name__ == '__main__':
#   R_create()
#   R_delete()


# def R_selete():
#   Q = Question.objects.get(id=1)
#   print("ID(PK):", Q.id)
#   print("Title:", Q)
#   print("Content:", Q.content)
  
#   print("Answer Count:", Q.answer_set.count())
#   print("Answer List:", Q.answer_set.all())
#   print("Answer Get:", Q.answer_set.get(content__contains='Professor'))
#   print("Answer Filter:", Q.answer_set.filter(content__contains='Soccer'))
  
# if __name__ == '__main__':
#   R_selete()


# from MTV.models import Board

# def data_objects():
#   Board_object = Board.objects.get(title='Board Test Write')
#   print("ID(PK):", Board_object.id)
#   print("Title:", Board_object.title)
#   print("Content:", Board_object.content)
#   print("Create_Date:", Board_object.create_date)
#   print("Modify_Date:", Board_object.modify_date)

# if __name__ == '__main__':
#   data_objects()


# def data_create():
#   Board_data = Board(title='Django Project', content='Django Project Model Data Create TEST')
#   Board_data.save()
#   print(Board.objects.all())


# def data_modify():
#   Board_data = Board.objects.get(title='Django Project')
#   Board_data.title = 'Django Model TEST'
#   Board_data.save()
#   print(Board.objects.all())

# if __name__ == '__main__':
#   data_create()
#   data_modify()


# def data_delete():
#   Board_data = Board.objects.get(title='Django Project')
#   Board_data.delete()
#   print(Board.objects.all())

  # Board_data = Board.objects.filter(title__contains='Django').delete()
  # print(Board.objects.all())

# if __name__ == '__main__':
#   data_delete()


# def data_create():
#   Board_data = Board(title='Django Project', content='Django Project Model Data Create TEST')
#   Board_data.save()
#   print(Board.objects.all())

# if __name__ == '__main__':
#   data_create()


# def data_selete():
  #All Select
  # print(Board.objects.all())
  # print(Board.objects.count())

  # Condition Select
  # print(Board.objects.filter(id=1))
  # print(Board.objects.filter(id=2))
  # print(Board.objects.get(id=1))
  # print(Board.objects.get(id=2))

  # Condition Select ( Filter [ "__contains" ])
  # print(Board.objects.filter(title__contains="Test"))
  # print(Board.objects.filter(title__contains="Django"))

# if __name__ == '__main__':
#   data_selete()


# [Python Class.1]
# class Person:
#   age = 0
#   addr = ""
#   SSN = ""

# John = Person()
# John.age = int(input("Age Input: "))
# John.addr = input("Addr Input: ")
# John.SSN = input("SSN Input: ")
# print("John Age:", John.age)
# print("John Addr:", John.addr)
# print("John Name:", John.SSN)
# print()

# James = Person()
# James.age = int(input("Age Input: "))
# James.addr = input("Addr Input: ")
# James.SSN = input("SSN Input: ")
# print("James Age:", James.age)
# print("James Addr:", James.addr)
# print("James Name:", James.SSN)


# [Python Class.2]
# class Person:
#   def Person_print_1(self):
#     print("Person Class Method Test_1")
#   def Person_print_2():
#     print("Person Class Method Test_2")

# Person.Person_print_1()
# user1 = Person()
# user1.Person_print_1()

# Person.Person_print_2()
# user2 = Person()
# user2.Person_print_2()


# [Python Class.3]
# class Person:
#   name = ""
#   age = 0
#   def Person_set(self, name, age):
#     self.name = name
#     self.age = age
    
# user = Person()
# name = input("Name Input: ")
# age = input("Age Input: ")
# user.Person_set(name, age)
# print("Name: ", user.name)
# print("Age: ",user.age)


# [Python Class.4]
# class Person:
#   Person_dic = {}
#   def Person_set(self, num):
#     for i in range(num):
#       key = input("Person Name: ")
#       val = input("Person Age: ")
#       self.Person_dic[key] = val
#     return self.Person_dic

# P = Person()
# count = int(input("Person_Set Loop Count: "))
# dic = P.Person_set(count)
# print(dic)


# [Python Class.5-1]
# class Car:
#   model = ""
#   color = ""

#   def __init__(self):
#     self.color = "White"
#     self.model = "Benz"

# myCar1 = Car()
# print("myCar1 Model: ", myCar1.model)
# print("myCar1 Color: ", myCar1.color)


# [Python Class.5-2]
# class Car:
#   model = ""
#   color = ""

#   def __init__(self, color="White", model="Benz"):
#     self.color = color
#     self.model = model

# myCar1 = Car()
# print("myCar1 Model: ", myCar1.model)
# print("myCar1 Color: ", myCar1.color)
# print()

# myCar2 = Car(color="Red")
# print("myCar1 Model: ", myCar2.model)
# print("myCar1 Color: ", myCar2.color)
# print()

# myCar3 = Car(color="Blue", model="BMW")
# print("myCar1 Model: ", myCar3.model)
# print("myCar1 Color: ", myCar3.color)


# [Python Class.5-3]
# class Car:
#   model = ""  # Instance Variable
#   color = ""  # Instance Variable
#   count = 0   # Class Variable

#   def __init__(self, color="White", model="Benz"):
#     self.color = color
#     self.model = model
#     Car.count += 1
  
# myCar1 = Car()
# print("myCar1 Model: ", myCar1.model)
# print("myCar1 Color: ", myCar1.color)
# print()

# myCar2 = Car(color="Red")
# print("myCar2 Model: ", myCar2.model)
# print("myCar2 Color: ", myCar2.color)
# print()

# myCar3 = Car(color="Blue", model="BMW")
# print("myCar3 Model: ", myCar3.model)
# print("myCar3 Color: ", myCar3.color)
# print()

# print("myCar1 Count: ", myCar1.count)
# print("myCar2 Count: ", myCar2.count)
# print("myCar3 Count: ", myCar3.count)


# [Python Class.6]
# class Computer:
#   CPU = ""
#   RAM = ""
#   SSD = ""

#   def __init__(self):
#     self.Computer_Set()

#   def Computer_Set(self):
#     self.CPU = "Intel"
#     self.RAM = "Samsung"
#     self.SSD = "Samsung"

# myCom = Computer()
# print("myCom CPU: ", myCom.CPU)
# print("myCom RAM: ", myCom.RAM)
# print("myCom SSD: ", myCom.SSD)


# [Python Class.7]
# class Car:
#   company = "BMW"
#   color = ""
#   model = ""

# class SuperCar(Car):
#   maxSpeed = ""

#   def __init__(self):
#     self.color = "White"
#     self.model = "BMW i8"
#     self.maxSpeed = "300KM"

# myCar = SuperCar()
# print("myCar Company\t:", myCar.company)
# print("myCar Color\t:", myCar.color)
# print("myCar model\t:", myCar.model)
# print("myCar MaxSpeed\t:", myCar.maxSpeed)


# [Python Class.8]
# class Calc:
#   def calcSum(self, num1, num2):
#     sum = num1 + num2
#     print("Sum:", sum)

#   def calcSub(self, num1, num2):
#     sub = num1 - num2
#     print("Sub:", sub)

# class ComCalc(Calc):
#   def calcMul(self, num1, num2):
#     mul = num1 * num2
#     print("Mul:", mul)

#   def calcDiv(self, num1, num2):
#     div = num1 / num2
#     print("Mul:", div)

# myCalc = ComCalc()
# myCalc.calcSum(100,200)
# myCalc.calcSub(100,200)
# myCalc.calcMul(100,200)
# myCalc.calcDiv(100,200)


# [Python Class.9]
# class Ferrari:
#   year = 0
#   maxSpeed = "300KM"

#   def __init__(self, year):
#     self.year = year

#   def getYear(self):
#     return self.year
  
#   def speedPrint(self):
#     print("{} Year Ferrari Max Speed: 300KM".format(self.getYear()))

# class NewFerrari(Ferrari):

#   def speedPrint(self): # Method Overriding
#     print("{} Year Ferrari Max Speed: 400KM".format(self.getYear()))

# myCar1 = Ferrari(2020)
# myCar1.speedPrint()

# myCar2 = NewFerrari(2022)
# myCar2.speedPrint()


# [Python Class.10]
# class Parent:
#   var = "Parents Variable"
#   def PrintMethod(self):
#     print("Class A Method Execute")

# class Child(Parent):
#   var = "Child Variable"
#   def PrintMethod(self):
#     print("Class B Method Execute")
#     print(self.var)

#   def ParentMethod(self):
#     super().PrintMethod()
#     print(super().var)

# ClassTest = Child()
# ClassTest.PrintMethod()
# ClassTest.ParentMethod()

import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
application = get_wsgi_application()

from Board.models import Board
from django.contrib.auth.models import User




