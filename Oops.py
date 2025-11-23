# # class Car:
# #     color = "Red"
# #     brand = "Toyota"
# #     def drive(self):
# #         print("the car is driving")
# # myCar = Car()
# # print(myCar.color)
# # print(myCar.brand)

# # constuctor:

# # __init__
# class Dog:
#     def __init__(self,breed,name):
#         self.breed = breed
#         self.name = name
#     def bark(self):
#         print("wolf")
#     def info(self):
#         print("info")
# dog1 = Dog('Labradog',"tommy")
# dog2 = Dog("Pug","doberman")
# dog1.bark()
# dog2.bark()


# # Write a Python program to create a class called 
# # Car that has the following:
# # An attribute brand to store the car's brand name.
# # A method start() that prints "Car started!" when called.
# # Create two objects of this class:
# # any two cars
# # Then, call the start() method for both objects.
 
# # class Car:
# #     def __init__(self,brand):
# #         self.brand = brand
# #     def start(self):
# #         print("Car started")
# # car1 = Car("Bmw")
# # car2 = Car("Toyota")
# # car1.start()
# # car2.start()



# # Create a class Student with attributes name, roll_no, and marks.
# # Add a method display() to print the details.
# # Also, create a method check_result() that prints “Pass” if marks ≥ 40, 
# # otherwise “Fail”.
# # Create two student objects and display their results.
# # class Student:
# #     def __init__(self,name,roll_no,marks):
# #         self.name = name
# #         self.marks = marks
# #         self.roll_no = roll_no
# #     def display(self):
# #         print(self.name,self.marks,self.roll_no)
# #     def check_result(self):
# #         if self.marks>=40:
# #             print("pass")
# #         else:
# #             print("fail")
# # s1 = Student("Aditya",7,50)
# # s2 = Student("Govind",96,500)
# # s1.display()
# # s1.check_result()
# # s2.display()
# # s2.check_result()



# # Create a class Employee with attributes name, salary, and department.
# # Add a method bonus() that increases salary by 10% if department 
# # is “Sales”, otherwise by 5%.
# # Display the updated salary.




# # Create a class Calculator that can perform addition, subtraction, 
# # multiplication, and division.
# # Each operation should be a separate method.
# # Create an object and call each method with different values.

# # Defining a class
# # class Student:
# #     def __init__(self, name, roll_no, marks):
# #         self.name = name
# #         self.roll_no = roll_no
# #         self.marks = marks

# #     def display(self):
# #         print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}")

# #     def check_result(self):
# #         if self.marks >= 40:
# #             print("Result: Pass")
# #         else:
# #             print("Result: Fail")

# # class Student:
# #     def __init__(self,name,marks):
# #         self.name = name
# #         self.marks = marks
# #     def display(self):
# #         print(self.name,self.marks)
# #     def grade(self):
# #         if self.marks >=90:
# #             print("grade A")
# #         elif self.marks <=75:
# #             print("Grade B")
# #         else:
# #             print("Grade C")
# # s1 = Student("Aditya",99)
# # s2 = Student("Ayush",6)
# # s1.display()
# # s1.grade()
# # s2.display()
# # s2.grade()

# # class Employee:
# #     company_name = "Classplus"
# #     def __init__(self,name):
# #         self.name = name
# #     @classmethod
# #     def change_company(cls,new_name):
# #         cls.company_name = new_name
# #     def show(self):
# #         print(self.name,Employee.company_name)
# # e1 = Employee("Pratham")
# # e2 = Employee("Pushkar")
# # e1.show()
# # Employee.change_company("Google")
# # e2.show()


# # class MathOperation:
# #     @staticmethod
# #     def add(a,b):
# #         return a+b
# #     @staticmethod
# #     def multipication(a,b):
# #         return a*b
# # print(MathOperation.add(10,20))
# # print(MathOperation.multipication(2,30))

# # Q1.Create a class Person that stores a person’s name.
# # Add an instance method greet() that prints a welcome message.
# # Create two objects and call the method.

# class Person:
#     def __init__(self,name):
#         self.name = name
#     def greet(self):
#         print(f"Hello {self.name} , welcome to Oops class")

# p1 = Person("Krishiv")
# p2 = Person("Direk")
# p1.greet()
# p2.greet()

# # Q2. Create a class Employee with:
# # Class variable: bonus = 1000
# # Instance variables: name, salary
# # Instance method: show_details()
# # Class method: change_bonus() to modify class bonus.     

# class Employee:
#     bonus = 1000
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def show_details(self):
#         total = self.salary + Employee.bonus
#         print(self.name,total)
#     @classmethod
#     def change_bonus(cls,new_bonus):
#         cls.bonus = new_bonus

# e1 = Employee("Abhishek",150)
# e2 = Employee("Ayush",200)
# e1.show_details()
# Employee.change_bonus(500)
# e2.show_details()

        
# # Create a class Temperature with static methods:
# # to_fahrenheit(celsius) → converts to Fahrenheit
# # to_celsius(fahrenheit) → converts to Celsius


# # Q4..Create a class Car with:
# # Class variable: total_cars
# # Instance variable: model, mileage
# # Static method: is_mileage_good(mileage) → returns True if > 15
# # Class method: show_total() → prints total cars
# # Instance method: show_details()

# # class Car:
# #     total_cars = 0
# #     def __init__(self,model,mileage):
# #         self.model = model
# #         self.mileage = mileage
# #         Car.total_cars +=1
# #     def show_details(self):
# #         print(self.model,self.mileage)
# #     @classmethod
# #     def show_total(cls):
# #         print(cls.total_cars)
# #     @staticmethod
# #     def is_mileage_good(mileage):
# #         return mileage>15
# # c1 = Car("Bmw",17)
# # c2 = Car("Defender",18)
# # c1.show_details()
# # c2.show_details()
# # print(Car.is_mileage_good(c1.mileage))
# # print(Car.is_mileage_good(c2.mileage))

# # class Car:
# #     wheels = 4
# #     def __init__(self,brand):
# #         self.brand = brand
# # C1 = Car("Bmw")
# # C2 = Car("Toyoto")
# # print(C1.wheels)
# # print(C2.wheels)
# # Car.wheels =6
# # print(C1.wheels)
# # print(C2.wheels)


# # class Students:
# #     def __init__(self,name,age):
# #         self.name = name
# #         self.age = age

# # S1 = Students("Raman",18)
# # S2 = Students("aditya",22)
# # print(S1.name)
# # print(S1.age)
    
# # class Students:
# #     def __init__(self,name,marks):
# #         self._name = name
# #         self.marks = marks
# # class Topper(Students):
# #     def show_marks(self):
# #         print(self._name,self.marks)
# # s1 = Topper("Ayush",49)
# # s1.show_marks()
# # #Acessing protected element(But not recommended)
# # print(s1._name)

# # class BankAccount:
# #     def __init__(self,name,balance):
# #         self.name = name
# #         self.__balance = balance
# #     def show_balance(self):
# #         print(self.name,self.__balance)
    
    

        
    
# # Q1.Create a class Book that has public attributes title and author.
# # Add a method show_details() that prints the book title and author.
# # Create two book objects and display their details.

# # class Book:
# #     def __init__(self,title,author):
# #         self.title = title
# #         self.author = author
# #     def show_details(self):
# #         print(self.title,self.author)
# # b1 = Book("Python","John Smith")
# # b2 = Book("Oops","Mary thomas")
# # b1.show_details()
# # b2.show_details()
# # print(b1.title)
# # print(b2.title)
# # print(b1.author)
# # print(b2.author)

# # Q2.Create a class Employee with a protected attribute _salary. 
# # Then create a subclass Manager that prints the employee’s salary. 
# # Show that it can be accessed in the subclass but should not be accessed
# #  directly outside.
        
        


    

# # Q3.Create a class Locker that has a private attribute __pin.
# # Use a method to verify the pin entered by the user.
# # Show what happens if we try to access the private variable directly.

# # class Locker:
# #     def __init__(self,pin):
# #         self.__pin = pin
# #     def verify_pin(self,user_pin):
# #         if user_pin == self.__pin:
# #             print("Access Granted")
# #         else:
# #             print("Access denied")
# # l1 = Locker(1234)
# # l1.verify_pin(1234)
# # l1.verify_pin(8938)
# # print(l1._Locker__pin)

        
# # for i in range(1,6):
# #     for j in range(1,i+1):
# #         print(i,end= " ")
# #     print()

        
# # for i in range(1,6):
# #     for j in range(1,i+1):
# #         print(j,end= " ")
# #     print()
        
# # class BankAccount:
# #     def __init__(self, balance):
# #         self.balance = balance  # Public variable

# # account = BankAccount(1000)
# # print("Initial balance:", account.balance)

# # #  Anyone can directly change the balance
# # account.balance = -500
# # print("Updated balance:", account.balance)

# # class BankAccount:
# #     def __init__(self, balance):
# #         self.__balance = balance  # Private variable

# #     def deposit(self, amount):
# #         if amount > 0:
# #             self.__balance += amount
# #         else:
# #             print("Deposit amount must be positive.")

# #     def get_balance(self):
# #         return self.__balance

# # account = BankAccount(1000)
# # print("Current balance:", account.get_balance())

# # account.deposit(500)
# # print("After deposit:", account.get_balance())

# # # Trying to access private variable directly
# # print(account.__balance)  #  Error


# # class Car:
# #     def __init__(self):
# #         self.__speed = 0

# #     def accelerate(self, amount):
# #         if self.__speed + amount <= 200:
# #             self.__speed += amount
# #         else:
# #             self.__speed = 200
# #             print("Speed limit reached (200 km/h)")

# #     def brake(self, amount):
# #         if self.__speed - amount >= 0:
# #             self.__speed -= amount
# #         else:
# #             self.__speed = 0
# #             print("Car stopped completely.")

# #     def get_speed(self):
# #         print("Current Speed:", self.__speed, "km/h")

# # car = Car()
# # car.accelerate(50)
# # car.get_speed()

# # car.accelerate(180)
# # car.get_speed()

# # car.brake(100)
# # car.get_speed()

# class SoftwareLicense:
#     def __init__(self, license_key):
#         self.__license_key = license_key
#         self.__attempts = 0
#         self.__is_locked = False

#     def validate(self, key):
#         if self.__is_locked:
#             print("Your account is locked due to too many failed attempts.")
#             return

#         if key == self.__license_key:
#             print("License validated successfully! Software unlocked.")
#             self.__attempts = 0
#         else:
#             self.__attempts += 1
#             print("Invalid License Key!")
#             if self.__attempts >= 3:
#                 self.__is_locked = True
#                 print("Account locked after 3 failed attempts.")

# # Test
# software = SoftwareLicense("XYZ-1234-VALID")

# software.validate("ABC-9999")
# software.validate("WRONG-KEY")
# software.validate("XYZ-1234-VALID")
# software.validate("TRY-AGAIN")  # won’t work if locked

# class ShoppingCart:
#     def __init__(self):
#         # Private variable to store total amount
#         self.__total_amount = 0

#     # Method to add product price
#     def add_item(self, price):
#         if price > 0:
#             self.__total_amount += price
#             print(f" Added item worth ₹{price}. Current total: ₹{self.__total_amount}")
#         else:
#             print("Invalid price! Please enter a positive value.")

#     # Method to remove product price
#     def remove_item(self, price):
#         if 0 < price <= self.__total_amount:
#             self.__total_amount -= price
#             print(f" Removed item worth ₹{price}. Current total: ₹{self.__total_amount}")
#         else:
#             print(" Invalid amount! Cannot remove item.")

#     # Method to safely display total
#     def show_total(self):
#         print(f"Current total amount: ₹{self.__total_amount}")


# # --- Example Execution ---
# cart = ShoppingCart()
# cart.add_item(1000)
# cart.add_item(500)
# cart.remove_item(300)
# cart.show_total()
# cart.remove_item(1500)  # Invalid



# class FlightTicket:
#     def __init__(self, destination, base_price, tax_percent):
#         self.destination = destination
#         self.__base_price = base_price
#         self.__tax_percent = tax_percent

#     def set_tax(self, tax):
#         if 0 <= tax <= 20:
#             self.__tax_percent = tax
#             print(f"✅ Tax updated to {tax}% for {self.destination}")
#         else:
#             print(" Invalid tax percentage!")

#     def get_total_price(self):
#         return self.__base_price + (self.__base_price * self.__tax_percent / 100)

#     def show_ticket(self):
#         print(f"Destination: {self.destination}")
#         print(f"Base Price: ₹{self.__base_price}")
#         print(f"Tax: {self.__tax_percent}%")
#         print(f"Total Ticket Price: ₹{self.get_total_price()}")


# # --- Test Code ---
# ticket1 = FlightTicket("Delhi", 8000, 5)
# ticket1.show_ticket()
# ticket1.set_tax(25)  #  Invalid
# ticket1.set_tax(10)  #  Valid
# ticket1.show_ticket()


# # Parent class
# class Animal:
#     def speak(self):
#         print("Animals make sounds")
# # Child class (inherits from Animal)
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks: Woof Woof!")
# # Object of child class
# d = Dog()
# d.speak()   # inherited from Animal
# d.bark()    # defined in Dog


# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand
#     def start(self):
#         print(f"{self.brand} vehicle is starting...")
# class Car(Vehicle):
#     def drive(self):
#         print(f"{self.brand} car is driving...")
# # Object
# c = Car("Toyota")
# c.start()
# c.drive()


# class Grandfather:
#     def house(self):
#         print("Grandfather’s house")

# class Father(Grandfather):
#     def car(self):
#         print("Father’s car")

# class Son(Father):
#     def bike(self):
#         print("Son’s bike")

# # Object
# s = Son()
# s.house()
# s.car()
# s.bike()


# class Teacher:
#     def teach(self):
#         print("Teacher teaches students")

# class Musician:
#     def play_music(self):
#         print("Musician plays the guitar")

# class MusicTeacher(Teacher, Musician):
#     def inspire(self):
#         print("Music Teacher inspires students")

# # Object
# mt = MusicTeacher()
# mt.teach()
# mt.play_music()
# mt.inspire()


# class Animal:
#     def eat(self):
#         print("All animals eat food")

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# class Cat(Animal):
#     def meow(self):
#         print("Cat meows")

# # Objects
# d = Dog()
# c = Cat()
# d.eat()
# d.bark()
# c.meow()

# class Parent:
#     def __init__(self):
#         print("Parent constructor")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()   # calling parent constructor
#         print("Child constructor")

# c = Child()


# class Company:
#     def __init__(self, company_name):
#         self.company_name = company_name

# class Employee(Company):
#     def __init__(self, company_name, emp_name):
#         super().__init__(company_name)
#         self.emp_name = emp_name

# class Developer(Employee):
#     def __init__(self, company_name, emp_name, language):
#         super().__init__(company_name, emp_name)
#         self.language = language

# class TeamLead(Developer):
#     def __init__(self, company_name, emp_name, language, team_size):
#         super().__init__(company_name, emp_name, language)
#         self.team_size = team_size

#     def show_details(self):
#         print(f"Company: {self.company_name}")
#         print(f"Employee Name: {self.emp_name}")
#         print(f"Programming Language: {self.language}")
#         print(f"Team Size: {self.team_size}")

# # Object
# t1 = TeamLead("TechNova", "Arjun", "Python", 8)
# t1.show_details()


# # Parent Class 1
# class Camera:
#     def take_photo(self):
#         print("Taking photo with a high-resolution camera.")

# # Parent Class 2
# class Phone:
#     def make_call(self):
#         print("Making a phone call...")

# # Child Class (inherits from both)
# class Smartphone(Camera, Phone):
#     def browse_internet(self):
#         print("Browsing the internet on a smartphone.")

# # Creating object
# sp = Smartphone()
# sp.take_photo()
# sp.make_call()
# sp.browse_internet()


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

# class EBook(Book):
#     def __init__(self, title, author, file_size):
#         super().__init__(title, author)
#         self.file_size = file_size

#     def show_info(self):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"File Size: {self.file_size} MB")

# ebook = EBook("Python Mastery", "Rohit Sharma", 5)
# ebook.show_info()

# class Animal:
#     def __init__(self, species):
#         self.species = species
#         print(f"Animal created: {self.species}")

# class Dog(Animal):
#     def __init__(self, species, name):
#         # call parent constructor
#         super().__init__(species)
#         self.name = name
#         print(f"Dog created: {self.name}")

# # Create object
# d = Dog("Mammal", "Tommy")


# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand

# class Car(Vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_capacity):
#         super().__init__(brand, model)
#         self.battery_capacity = battery_capacity

#     def show_details(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Battery: {self.battery_capacity} kWh")

# # Create object
# tesla = ElectricCar("Tesla", "Model S", 100)
# tesla.show_details()


# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

# class Student(User):
#     def __init__(self, name, email, course):
#         super().__init__(name, email)
#         self.course = course

# class PremiumStudent(Student):
#     def __init__(self, name, email, course, subscription_fee):
#         super().__init__(name, email, course)
#         self.subscription_fee = subscription_fee

#     def show_info(self):
#         print(f"Name: {self.name}, Email: {self.email}, Course: {self.course}, Fee: ₹{self.subscription_fee}")

# # Create object
# p1 = PremiumStudent("Aarav", "aarav@example.com", "Python OOP", 1500)
# p1.show_info()

# Encapsulation:
# 1.Create a class Car with a private variable __speed.
#  Add methods to:
# accelerate(amount) → increase speed (maximum 200)
# brake(amount) → decrease speed (minimum 0)
# get_speed() → print current speed

# class Car:
#     def __init__(self):
#         self.__speed = 0
#     def accelerate(self,amount):
#         if self.__speed+ amount <=200:
#             self.__speed += amount
#         else:
#             self.__speed = 200
#     def brake(self,amount):
#         if self.__speed -amount >=200:
#             self.__speed -= amount
#         else:
#              self.__speed =0
#     def get_speed(self):
#         print(self.__speed)
# car = Car()
# car.accelerate(50)
# car.get_speed()
# car.brake(59)

# 2.You have to build a ShoppingCart class that:
# Has private variable __total_amount
# Allows adding and removing product prices
# Prevents total from becoming negative
# Has a method to display current total safely

# class ShoppingCart:
#     def __init__(self):
#         self.__total_amount = 0
#     def add_item(self,price):
#         if price >0:
#             self.__total_amount+= price
#             print(price,self.__total_amount)
#         else:
#             print("Invalid price")
#     def remove_item(self,price):
#         if 0<price<self.__total_amount:
#              self.__total_amount-= price
#         else:
#             print("Invalid Price")
#     def show_total(self):
#         print(self.__total_amount)
# cart = ShoppingCart()
# cart.add_item(1000)
# cart.remove_item(400)
# cart.show_total()
       
# 3.Create a FlightTicket class that:
# Has private variables __base_price and __tax_percent
# Calculates total ticket price as base_price + (base_price * tax / 100)
# Allows updating tax but limits it between 0–20% only
# The ticket price should never be accessed or modified directly

# class FlightTicket:
#     def __init__(self,base_price,tax_percent):
#         self.__base_price = base_price
#         self.__tax_percent = tax_percent
#     def set_tax(self,tax):
#         if 0<=tax<=20:
#             self.__tax_percent = tax
#             print(tax)
#         else:
#             print("Invalid tax")
#     def total_price(self):
#         return self.__base_price+(self.__base_price* self.__tax_percent / 100)
#     def show_ticket(self):
#         print(self.__base_price)
#         print(self.__tax_percent)
# ticket1 =FlightTicket(8000,5)
# ticket1.show_ticket()
# ticket1.total_price()
# ticket1.set_tax(19)
    
# Inheritance:

# class Vehical:
#     def __init__(self,brand):
#         self.brand =brand
#     def start(self):
#         print(self.brand)
# class Car(Vehical):
#     def drive(self):
#         print(self.brand)
# c = Car("Bmw")
# c.drive()
# c.start()
        
# class GrandFather:
#     def house(self):
#         print("grandfather's House")
# class Father(GrandFather):
#     def Car(self):
#         print("father's Car")
# class son(Father):
#     def bike(self):
#         print("Son's Bike")
# s = son()
# s.house()
# s.Car()
# s.bike()



# class Teacher:
#     def teach(self):
#         print("Teacher teaches to the students")
# class Musician:
#     def play_music(self):
#         print("Learn the music")
# class MusicTeacher(Teacher,Musician):
#     def inspire(self):
#         print("Music Teacher inspire to the students")
# mt = MusicTeacher()
# mt.teach()
# mt.play_music()
# mt.inspire()


# class Animal:
#     def eat(self):
#         print("All animals eat food")
# class Dog(Animal):
#     def bark(self):
#         print("bark")
# class Cat(Animal):
#     def meow(self):
#         print("Cat moves")
# d = Dog()
# c = Cat()
# d.eat()
# c.eat()
# d.bark()
# c.meow()


# Q1.Create a class Book with attributes title and author.
# Create a class EBook that inherits from Book and adds attribute 
# file_size.
# Display complete book info.

# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author
# class EBook(Book):
#     def __init__(self, title, author,file_size):
#         super().__init__(title, author)
#         self.file_size = file_size
#     def show_info(self):
#         print(self.title)
#         print(self.author)
#         print(self.file_size)
# ebook = EBook("Python Mastery","Ethan",34)
# ebook.show_info()

#  Q2.Create a Company class with a company name.
#  Create an Employee class that inherits Company and adds 
# employee names.
#  Create a Developer class that inherits Employee and adds programming 
# language.
#  Finally, create a TeamLead class that inherits 
#    Developer and adds team size.
#  Display all information properly.

# class Company:
#     def __init__(self,company_name):
#         self.company_name = company_name
# class Employee(Company):
#     def __init__(self, company_name,empolyee_name):
#         super().__init__(company_name)
#         self.employee_name = empolyee_name
# class Developer(Employee):
#     def __init__(self, company_name,empolyee_name,language):
#           super().__init__(company_name,empolyee_name)
#           self.language = language
# class TeamLead(Developer):
#     def __init__(self, company_name,empolyee_name,language,team_size):
#           super().__init__(company_name,empolyee_name,language)
#           self.team_size = team_size
#     def show_details(self):
#          print(self.employee_name)
#          print(self.team_size)
#          print(self.language)
#          print(self.company_name)
# t1 = TeamLead("PST","Ayush","Python",10)
# t1.show_details()

# Q3.Create:
# A class Camera → has a method take_photo()
# A class Phone → has a method make_call()
# A class Smartphone → inherits both Camera and Phone, and adds method browse_internet()
# Then create an object of Smartphone and show all features.


# class Camera:
#     def take_photo(self):
#         print("Photos")
# class Phone:
#     def make_call(self):
#         print("call")
# class Smartphone(Camera,Phone):
#     def browse_internet(self):
#         print("camera")
# sp = Smartphone()
# sp.take_photo()
# sp.make_call()
# sp.browse_internet()

# Q4.Create three classes:
# Vehicle → base class (has brand)
# Car → inherits from Vehicle (adds model)
# ElectricCar → inherits from Car (adds battery_capacity)

# Display full details using super() in constructors


# Q5. Create a system for an online course with these rules:
# Class User stores name and email.
# Class Student inherits from User and stores course name.
# Class PremiumStudent inherits from Student and adds subscription_fee.
# Print all details using super() at each level.  
# class User:
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email
# class Student(User):
#     def __init__(self, name, email,course_name):
#         super().__init__(name, email)
#         self.course_name = course_name
# class PremiumStudent(Student):
#     def __init__(self, name, email, course_name,subscription_fee):
#         super().__init__(name, email, course_name)
#         self.subscription_fee = subscription_fee
#     def show_details(self):
#         print(self.name)
#         print(self.email)
#         print(self.course_name)
#         print(self.subscription_fee)

# s1 = PremiumStudent("Pranitha","gmail","Cse",70000000000)
# s1.show_details()

# You are tasked with creating a Python program that manages a student grading system 
# and handles exceptions using nested try-except blocks.
# Create a Python program that performs the following tasks:

# Define a class Student with the following attributes:
# name (a string): The name of the student.
# score (an integer): The student's score on an exam.
# Implement member functions for the following operations:
# getName(): Returns the name of the student.
# getScore(): Returns the student's score.
# In the main program:

# Create a Student object with predefined values for the student's name and score. 
# For example, create a student named “Ethan" with a score of -90.
# Use nested try-except blocks to handle the following scenarios:
# Innermost try-except (specific exception handling): Use an inner try-except 
# block to catch exceptions related to invalid scores. If the student's score is 
# not within the valid range (0-100), throw an exception of type ValueError with 
# the message "Invalid score."
# Outermost try-except (general exception handling):
#  Use an outermost try-except block to catch any unhandled exceptions
#   and display "An unknown error occurred.".

# Display the student's name and score if they
# are valid or handle exceptions gracefully andprovide meaningful error messages.

# class Student:
#     def __init__(self, student_name, student_score):
#         self.student_name = student_name
#         self.student_score = student_score
    
#     def getName(self):
#         return self.student_name
    
#     def getScore(self):
#         return self.student_score
    
# try:
#     student = Student("Ethan", -90)
#     try:
#         if student.getScore() < 0 or student.getScore() > 100:
#             raise ValueError("Invalid Score")
#         print(student.getName())
#         print(student.getScore())
#     except ValueError as e:
#         print(e)
# except Exception as e:
#         print(e)
#         print("Unknown Error")


# class Human:
#     def speak(self):
#         print("Human can speak")
# class Robot:
#     def speak(self):
#         print("Robot can speak")
# class Dog:
#     def speak(self):
#         print("Dog can speak")
# def call_to_speak(enity):
#     enity.speak()
# for creation in [Human(),Robot(),Dog()]:
#     call_to_speak(creation)

# class Animal:
#     def sound(self):
#         print("genric sound")
# class Dog(Animal):
#     def sound(self):
#         print("bark")
# class Cat(Animal):
#     def sound(self):
#         print("Meow")
# animals = [Dog(),Cat(),Animal()]
# for a in animals:
#     a.sound()


# class Math:
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
# obj = Math()
# obj.add(1,2,4)

# class Math:
#     def add(self,*args):
#         total = sum(args)
#         print(total)
# obj = Math()
# obj.add(1,2,3,4,4,2)
# obj.add()

# print(5+6)
# print("5"+"6")
# print([1,2]+[3,4])

# __init__
# __add__
# __gt__
# __ls__

# class Student:
#     def __init__(self,marks):
#         self.marks = marks
#     def __add__(self,other):
#         return self.marks+ other.marks
#     def __gt__(self,other):
#         return self.marks>other.marks
# s1 = Student(88)
# s2 = Student(89)
# print(s1+s2)
# print(s1>s2)
    
# Write two classes Printer and Scanner,
# both having a method operate(). Demonstrate duck typing.

# class Printer:
#     def operate(self):
#         print("Printing")
# class Scanner:
#     def operate(self):
#         print("Scanner")
# for device in [Printer(),Scanner()]:
#     device.operate()

# Create a base class Shape with a method area().
# Override it in Circle and Square.
# class shape:
#     def area(self):
#         print("calcualting the area")
# class Circle(shape):
#     print("area of the circle")
# class square(shape):
#     print("square")
# for shape in [Circle(),square(),shape()]:
#     shape.area()

# Create a parent class Shape with a method area().
# Then create two child classes Circle and Rectangle, both overriding the area() 
# method to calculate their respective areas.
# Call the area() method for each class object to demonstrate runtime polymorphism.

# Create a class Employee with a method info() that displays details 
# differently based on how many details are passed — like name only, 
# or name + department, or name + department + salary.
# class Employee:
#     def info(self,*args):
#         if len(args) ==1:
#             print(args[0])
#         elif len(args) == 2:
#             print(args[0],args[1])
#         elif len(args) == 3:
#             print(args[0],args[1],args[2])
#         else:
#             print("Invalid number of arguments")
# obj = Employee()
# obj.info("Pratham")
# obj.info("Pratham","IT")
# obj.info("Pratham","IT",150)

# Create a class Distance that stores distance in kilometers and meters.
#  Overload the + operator to add two Distance objects together.

# class Distance:
#     def __init__(self,km,m):
#         self.km = km
#         self.m = m
#     def __add__(self,other):
#         total_m = self.m + other.m
#         total_km = self.km +other.km + total_m//1000
#         total_m = total_m%1000
#         return Distance(total_m,total_km)
#     def display(self):
#         print(self.m)
#         print(self.km)
# d1 = Distance(5,589)
# d2 = Distance(6,390)
# d3 = d1+d2
# d3.display()


# Create three payment classes — CreditCard, PayPal, and UPI.
# Each class has a method make_payment(amount).
# Write a function process_payment() that accepts any payment method 
# object and calls its method.
# class CreditCard:
#     def make_payment(self,amount):
#         print(amount)
# class PayPal:
#     def make_payment(self,amount):
#         print(amount)
# class UPI:
#     def make_payment(self,amount):
#         print(amount)

# def process_payment(payment_method,amount) :
#     payment_method.make_payment(amount)

# for method in [CreditCard(),PayPal(),UPI()]:
#     process_payment(method,100)
       


# Create a base class Vehicle with a method max_speed().
# Create subclasses Car, Bike, and Truck, each overriding max_speed() 
# to return different speed limits.
# Then create a function show_speed(vehicle) that accepts any object 
# and prints its speed — using runtime polymorphism.

# class Vehicle:
#     def max_speed(self):
#         return "speed not found"
# class Car(Vehicle):
#     def max_speed(self):
#         return "Car speed"
# class Bike(Vehicle):
#     def max_speed(self):
#         return "Bike speed"
# class Truck(Vehicle):
#     def max_speed(self):
#         return "Truck speed"
# def show_speed(vehicle):
#     print(vehicle.max_speed())
# list = [Car(),Bike(),Truck()]
# for v in list:
#     show_speed(v)


# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return 3.14*self.radius*self.radius
# class Reactangle(Shape):
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length*self.width
# c = Circle(5)
# r = Reactangle(3,4)
# print(c.area())
# print(r.area())
      
# Question 1: Create an abstract class Vehicle with
# abstract method start_engine().
# Then create two subclasses Car and Bike that implement it.    

# from abc import ABC ,abstractmethod  
# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass
# class Car(Vehicle):
#     def start_engine(self):
#         return "Car engine started"
# class Bike(Vehicle):
#     def start_engine(self):
#         return "Bike started"
# c = Car()
# b = Bike()
# print(c.start_engine())
# print(b.start_engine())

# Question 2. Enforcing Structure
# Create an abstract class Appliance that defines:
# an abstract method turn_on()
# an abstract method turn_off()
# Create subclasses:
# washingMachine
# Refrigerator
# Each should implement both methods with appropriate messages.

# from abc import ABC ,abstractmethod 
# class Appliance(ABC):
#     @abstractmethod
#     def turn_on(self):
#         pass
#     @abstractmethod
#     def turn_off(self):
#         pass
# class washingMachine(Appliance):
#     def turn_off(self):
#         print("Washing machine is turn off")
#     def turn_on(self):
#         print("Washing machine is turn on")
# class Refrigerator(Appliance):
#         def turn_off(self):
#             print("Refrigerator is turn off")
#         def turn_on(self):
#             print("Refrigerator is turn on")
# wm = washingMachine()
# rf = Refrigerator()
# wm.turn_on()
# wm.turn_off()
# rf.turn_on()
# rf.turn_off()

# Create an abstract class Payment with 
# abstract method make_payment(amount).
# Create subclasses:
# CreditCardPayment
# UPIPayment
# PayPalPayment
# Each should print a unique message showing how the payment was made.
# from abc import ABC ,abstractmethod
# class Payment(ABC):
#     @abstractmethod 
#     def make_payment(self):
#         pass
# class CreditCardPayment(Payment):
#     def make_payment(self,amount):
#         print(amount)
# class UPIPayment(Payment):
#     def make_payment(self,amount):
#         print(amount)
# class PayPalPayment(Payment):
#     def make_payment(self,amount):
#         print(amount)
# payment = [CreditCardPayment(),UPIPayment(),PayPalPayment()]
# for p in payment:
#     p.make_payment(1900)


# Create an abstract class Shape having:
# Constructor that takes color
# Abstract method area()
# Concrete method display_color()
# Create subclasses Circle and Rectangle that implement area().




# Question 2. Enforcing Structure
# Create an abstract class Appliance that defines:
# an abstract method turn_on()
# an abstract method turn_off()
# Create subclasses:
# washingMachine
# Refrigerator
# Each should implement both methods with appropriate messages.



# Create a base class Vehicle with a method max_speed().
# Create subclasses Car, Bike, and Truck, each overriding max_speed() 
# to return different speed limits.
# Then create a function show_speed(vehicle) that accepts any object 
# and prints its speed — using runtime polymorphism.


#Define a class Car with private attributes and methods to access them.







        





# def test(vale):
#     if(vale<(-273) or vale >273):
#         raise ValueError("Incorrect value")
# x = (input("enter value"))
# try:
#     y=int(x)
#     test(y)
# except ValueError:
#     print("enter correct value")
# except Exception as e:
#     print(e)

# else:
#     print("correct value")    

# dict = {"age":12,"name":"kularatha"}
# try:
#     print(dict["lala"])
# except KeyError:
#     print("key")    




# def add(a, b):
#     a = 3
#     b = 4

# try:
#     a = 3
#     b = v
#     c = a+b 

#     print("addition", c)
# except ValueError as e:
#     print(e)

# finally:
#     print("Program executed successfully")


# try:
#     x = (5+"5")
# except TypeError as e:
#     print(e)



# try:
#     name:"Shivaansh"
#     city:"new York"
# except ValueError : 
#     print(d[food:"burger"])



# try:
#     nums = (int(input("enter a number:")))
#     b =
# except ValueError: 
#      #like this line we get the input from the user and user giving it in wrong formate like string formate 
#     print( b , "this is a value error")







# for i in range(100,1,-1):
#     print(i)



# try:
#     x = int("abc")
#     print(x)
# except ValueError as e:
#     print(e)
# finally:
#     print("done")






