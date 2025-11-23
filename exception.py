# # try:
# #     a = int(input("enter the number"))
# #     b = int(input("Enter the number"))
# #     c = a/b
# #     print(c)
# # except ZeroDivisionError:
# #     print("Can't divide by zero ")
# # else:
# #     print("divison successfull")
# # finally:
# #     print("Program excectuion successfully")

# # user_input = input("enter the number")
# # try:
# #     number = int(input("Enter the number"))
# #     print(number)
# # except ValueError:
# #     print("Please enter the correct value ")
# # else:
# #     print("Invalid input")
# # finally:
# #     print("Program excetuion successfully")


# # a = input("enter the value")
# # b = 5
# # try:
# #     result = a+b
# #     print(result)
# # except TypeError:
# #     print("Please enter the correct values")
# # finally:
# #     print("program exection successfully")

# # my_dict = {"name":"Aditya","age":20}
# # key = input("enter the key")
# # try:
# #     print(my_dict[key])
# # except KeyError:
# #     print("please enter the correct value")
# # finally:
# #     print("program execution successfully")


# # Write a Python program that should handle division by zero
# # exceptions and display an appropriate error message to the user.
# # Additionally, you should use multiple except clauses to handle 
# # different types of exceptions that might occur during the 
# # program's execution. Given numerator as 1 and denominator as 0,
# # your program should:
# # Attempt to perform the division of the first 
# # integer by the second integer. Handle the following exceptions: 
# # ArithmeticError if a division by zero occurs. 
# # ValueError if the user enters non-integer values.
# # Exception for any other unexpected exceptions that might occur. 
# # Display an error message for each specific exception type. 
# # # If the division is successful, display the result.

# # try:
# #     a = int(input("enter the number"))
# #     b = int(input("enter the number"))
# #     result = a/b
# #     print(result)
# # except ArithmeticError:
# #     print("Please enter the correct value")
# # except ValueError:
# #     print("Please enter correct values")
# # except Exception as e:
# #     print("Unexcepted error",e)
# # finally:
# #     print("Program exectuion successfully")

# # 2.Write a Python program to convert a temperature from 
# # Celsius to Fahrenheit.
# # Requirements:
# # If the input temperature is below absolute zero (-273.15°C),
# #  raise an exception with the message "Temperature below absolute"
# #  " zero is not valid."
# # Convert Celsius to Fahrenheit using the formula:
# #  Fahrenheit = (Celsius × 9 / 5) + 32
# # Display both the Celsius and Fahrenheit temperatures.

# # Error Handling:
# # If the temperature is below absolute zero, catch 
# # the exception and display "Invalid Argument"
# #  with the error message.
# # def tempature(celsius):
# #     if celsius<-273.15:
# #         raise ValueError("tempature is below")
# #     Fahrenheit = (celsius * 9 / 5) + 32
# #     return Fahrenheit
# # try:
# #     celsius = float(input("please entert the value"))
# #     Fahrenheit = tempature(celsius)
# #     print(celsius)
# #     print(Fahrenheit)
# # except ValueError:
# #     print("Please enter the correct value")
# # except Exception as e:
# #     print(e)
# # finally:
# #     print("Program exectution successfully")


# # If any other unexpected error occurs, display 
# # "An unknown error occurred."
# # Ask the user for a filename.
# # Try to open and read the file.
# # Handle the following:
# # FileNotFoundError: If the file does not exist, display an error.
# # PermissionError: If permission is denied.
# # Exception: For any other unexpected errors.
# # If successful, print the file contents.
# # Example:
# # If the user enters a non-existing filename, display
# # Error: File not found.
    

# # # Class (blueprint)
# # class Car:
# #     # attribute (data)
# #     color = "Red"
# #     brand = "Toyota"

# #     # method (behavior)
# #     def drive(self):
# #         print("The car is driving")

# # # Object (real entity)
# # my_car = Car()

# # # Accessing data and method
# # print(my_car.color)   # Red
# # my_car.drive()        # The car is driving


# # # Define the class
# # class Dog:
# #     # Constructor method to initialize the breed
# #     def __init__(self, breed):
# #         self.breed = breed   # attribute of the object
    
# #     # Method - behavior of the dog
# #     def bark(self):
# #         print("Woof!")

# # # Create two Dog objects (instances)
# # dog1 = Dog("Labrador")
# # dog2 = Dog("Pug")

# # # Call the bark() method
# # dog1.bark()
# # dog2.bark()


# # class Car:
# #     def __init__(self, brand, color):
# #         self.brand = brand
# #         self.color = color

# #     def show(self):
# #         print(f"Car: {self.brand}, Color: {self.color}")

# # car1 = Car("Honda", "Blue")
# # car2 = Car("BMW", "Black")

# # car1.show()
# # car2.show()

# # class car:
# #     color = "Red"
# #     brand = "Toyota"
    
# #     def behave(self):
# #         print('The car is driving')
# # my_car = car()
# # print(my_car.color)
# # print(my_car.brand)


# # class Car:
# #     color = "Red"
# #     brand = "Nano"

# #     def drive(self):
# #         print("The car is driving")
# # my_car = Car()
# # print(my_car.color)
# # print(my_car.brand)


# # class Dog:
# #    def __init__(self, name, breed):
# #        self.name = name
# #        self.breed = breed
# #    def bark(self):
# #        print(f"{self.name} says Woof!")
# #    def info(self):
# #        print(f"My name is {self.name} and I am a {self.breed}.")
# # dog1 = Dog("Tommy", "Labrador")
# # dog2 = Dog("Bruno", "Pug")
# # dog1.bark()
# # dog2.info()


# # class Car:
# #     def __init__(self, brand):
# #         self.brand = brand       # attribute
# #     def start(self):
# #         print("Car started!")
# # # Creating objects
# # car1 = Car("Toyota")
# # car2 = Car("BMW")
# # # Calling the method
# # car1.start()
# # car2.start()


# # class Student:
# #     def __init__(self,name,roll_no,marks):
# #         self.name = name
# #         self.roll_no = roll_no
# #         self.marks = marks
# #     def display(self):
# #         print(self.name,self.roll_no,self.marks)
# #     def check_result(self):
# #         if self.marks>=40:
# #             print("pass")
# #         else:
# #             print("fail")
# # s1 = Student("Riya",101,85)
# # s2 = Student("Aman",102,95)

# # s1.display()
# # s1.check_result()

# # s2.display()
# # s2.check_result()


# # class Employee:
# #     def __init__(self, name, salary, department):
# #         self.name = name
# #         self.salary = salary
# #         self.department = department

# #     def bonus(self):
# #         if self.department.lower() == "sales":
# #             self.salary += self.salary * 0.10
# #         else:
# #             self.salary += self.salary * 0.05
# #         print(f"{self.name}'s updated salary: ₹{self.salary}")

# # emp1 = Employee("Ravi", 40000, "Sales")
# # emp2 = Employee("Nisha", 50000, "HR")

# # emp1.bonus()
# # emp2.bonus()


# class Calculator:
#     def add(self, a, b):
#         print("Addition:", a + b)
#     def subtract(self, a, b):
#         print("Subtraction:", a - b)
#     def multiply(self, a, b):
#         print("Multiplication:", a * b)
#     def divide(self, a, b):
#         if b != 0:
#             print("Division:", a / b)
#         else:
#             print("Cannot divide by zero")
# calc = Calculator()
# calc.add(10, 5)
# calc.subtract(10, 5)
# calc.multiply(10, 5)
# calc.divide(10, 5)


# # class Person:
# #     def __init__(self, name, age):
# #         self.name = name    # public attribute
# #         self.age = age

# # p1 = Person("Riya", 25)
# # print(p1.name)    # accessible directly
# # print(p1.age)

# # p1.age = 26       # modifying directly
# # print("Updated Age:", p1.age)


# # class BankAccount:
# #     def __init__(self, owner, balance):
# #         self.owner = owner
# #         self._balance = balance   # protected attribute

# #     def show_balance(self):
# #         print(f"Owner: {self.owner}, Balance: ₹{self._balance}")

# # class SavingsAccount(BankAccount):
# #     def add_interest(self, rate):
# #         self._balance += self._balance * rate / 100

# # # Using protected attribute
# # acc = SavingsAccount("Rohit", 5000)
# # acc.add_interest(5)
# # acc.show_balance()

# # # Accessing protected variable (possible, but not advised)
# # print(acc._balance)


# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance   # private attribute

#     def show_balance(self):
#         print(f"Owner: {self.owner}, Balance: ₹{self.__balance}")

#     def deposit(self, amount):
#         self.__balance += amount

# a1 = Account("Nisha", 10000)
# a1.show_balance()

# a1.deposit(2000)
# a1.show_balance()

# # Trying to access private variable directly
# # print(a1.__balance)   #  AttributeError

# # Accessing private variable using name mangling (not recommended)
# print(a1._Account__balance)   # Works, but not advised


# class Car:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed

#     def accelerate(self):
#         self.speed += 10

#     def show_speed(self):
#         print(f"{self.brand} is running at {self.speed} km/h")

# # Creating objects
# car1 = Car("Toyota", 50)
# car2 = Car("BMW", 80)

# car1.accelerate()
# car1.accelerate()
# car2.accelerate()

# car1.show_speed()   # Toyota is running at 70 km/h
# car2.show_speed()   # BMW is running at 90 km/h


# class MathTool:
#     @staticmethod
#     def square(num):
#         return num * num

#     @staticmethod
#     def is_positive(num):
#         return num > 0

# print(MathTool.square(5))         # 25
# print(MathTool.is_positive(-10))  # False


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def display(self):   # instance method
#         print(f"Name: {self.name}, Marks: {self.marks}")

#     def grade(self):     # instance method
#         if self.marks >= 90:
#             print("Grade: A+")
#         elif self.marks >= 75:
#             print("Grade: A")
#         else:
#             print("Grade: B")

# s1 = Student("Riya", 92)
# s2 = Student("Aman", 78)

# s1.display()
# s1.grade()

# s2.display()
# s2.grade()


# class Employee:
#     company_name = "Google"  # class variable
#     def __init__(self, name):
#         self.name = name
#     @classmethod
#     def change_company(cls, new_name):
#         cls.company_name = new_name
#     def show(self):
#         print(f"Employee: {self.name}, Company: {Employee.company_name}")
# e1 = Employee("Rohit")
# e2 = Employee("Aman")
# e1.show()
# Employee.change_company("Microsoft")
# e2.show()

# class Employee:
#     company_name = "Google"
#     def __init__(self,name):
#         self.name = name
#     @classmethod
#     def change_company(cls,new_name):
#         cls.company_name = new_name
#     def show(self):
#         print(self.name,Employee.company_name)
# e1 = Employee("Rohit")
# e2 = Employee("Aman")
# e1.show()
# Employee.change_company("Microsoft")
# e2.show()
    

# class MathOperations:
#     @staticmethod
#     def add(a, b):
#         return a + b

#     @staticmethod
#     def multiply(a, b):
#         return a * b
# print(MathOperations.add(10, 5))
# print(MathOperations.multiply(3, 4))

# class MathOperations:
#     def add(a,b):
#         return a+b
    
#     def multiply(a,b):
#         return a*b
# print(MathOperations.add(10,4))
# print(MathOperations.multiply(3,4))



# class MathHelper:
#     def square(n):
#         return n * n
#     def cube(n):
#         return n * n * n

# # Try calling using an object
# obj = MathHelper()
# print(obj.square(5))

# class Employee:
#     bonus = 1000
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def show_details(self):
#         total = self.salary + Employee.bonus
#         print(f"Employee: {self.name}, Total Salary: {total}")
#     @classmethod
#     def change_bonus(cls, new_bonus):
#         cls.bonus = new_bonus
# e1 = Employee("Rohit", 30000)
# e2 = Employee("Aman", 25000)
# e1.show_details()
# Employee.change_bonus(2000)
# e2.show_details()


# class Person:
#     def __init__(self, name):
#         self.name = name
#     def greet(self):
#         print(f"Hello {self.name}, welcome to the OOP world!")
# p1 = Person("Riya")
# p2 = Person("Aman")

# p1.greet()
# p2.greet()


# class Temperature:
#     @staticmethod
#     def to_fahrenheit(celsius):
#         return (celsius * 9/5) + 32

#     @staticmethod
#     def to_celsius(fahrenheit):
#         return (fahrenheit - 32) * 5/9

# print(Temperature.to_fahrenheit(0))    
# print(Temperature.to_celsius(212))      


# class Car:
#     total_cars = 0
#     def __init__(self, model, mileage):
#         self.model = model
#         self.mileage = mileage
#         Car.total_cars += 1
#     def show_details(self):
#         print(f"Model: {self.model}, Mileage: {self.mileage} kmpl")
#     @classmethod
#     def show_total(cls):
#         print("Total cars created:", cls.total_cars)
#     @staticmethod
#     def is_mileage_good(mileage):
#         return mileage > 15
# c1 = Car("Swift", 18)
# c2 = Car("i20", 14)

# c1.show_details()
# Car.show_total()
# print("Swift good mileage:", Car.is_mileage_good(c1.mileage))
# print("i20 good mileage:", Car.is_mileage_good(c2.mileage))


# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand      # instance attribute
#         self.color = color

# c1 = Car("Toyota", "Red")
# c2 = Car("BMW", "Black")

# print(c1.brand)   # Toyota
# print(c2.brand)   # BMW

# class Car:
#     wheels = 4   # class attribute (same for all cars)
#     def __init__(self, brand):
#         self.brand = brand  # instance attribute

# c1 = Car("Toyota")
# c2 = Car("BMW")

# print(c1.wheels)  # 4
# print(c2.wheels)  # 4

# Car.wheels = 6    # changing class attribute
# print(c1.wheels)  # 6
# print(c2.wheels)  # 6


# class Student:
#     def __init__(self, name, age):
#         self.name = name      # Public attribute
#         self.age = age        # Public attribute

# s1 = Student("Riya", 18)

# # Accessing public attributes
# print("Name:", s1.name)
# print("Age:", s1.age)


# class Student:
#     def __init__(self, name, marks):
#         self._marks = marks   # Protected attribute
#         self.name = name

# class Topper(Student):
#     def show_marks(self):
#         print(f"{self.name}'s Marks:", self._marks)

# s1 = Topper("Riya", 95)
# s1.show_marks()
# Accessing protected attribute outside (possible but not recommended)
# print("Accessing protected marks outside:", s1._marks)


# class Student:
#     def __init__(self,name,marks):
#         self._marks = marks
#         self.name = name
#     class Topper(Student):
#         def show_marks(self):
#             s1 = Topper("Riya", 95)
# s1.show_marks()
# Student._marks()
# # Accessing protected attribute outside (possible but not recommended)
# print("Accessing protected marks outside:", s1._marks)
            

# class Student:
#     def __init__(self, name, marks):
#         self._marks = marks   # Protected attribute
#         self.name = name

# class Topper(Student):
#     def show_marks(self):
#         print(f"{self.name}'s Marks:", self._marks)

# s1 = Topper("Riya", 95)
# s1.show_marks()

# # Accessing protected attribute outside (possible but not recommended)
# print("Accessing protected marks outside:", s1._marks)


# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name              # Public attribute
#         self.__balance = balance      # Private attribute

#     def show_balance(self):
#         print(f"Account Holder: {self.name}")
#         print(f"Balance: {self.__balance}")

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")
#         else:
#             print("Invalid amount!")

# # Creating an object
# acc1 = BankAccount("Rohit", 50000)

# # Accessing public method
# acc1.show_balance()
# acc1.deposit(10000)

# Trying to access private attribute directly 
# print(acc1.__balance)



# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name              # Public attribute
#         self.__balance = balance      # Private attribute

#     def show_balance(self):
#         print(f"Account Holder: {self.name}")
#         print(f"Balance: {self.__balance}")

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")
#         else:
#             print("Invalid amount!")

# # Creating an object
# acc1 = BankAccount("Rohit", 50000)

# # Accessing public method
# acc1.show_balance()
# acc1.deposit(10000)

# # Trying to access private attribute directly ❌
# print(acc1.__balance)


# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance   # Private attribute

#     # Public method (getter)
#     def get_balance(self):
#         return self.__balance

#     # Public method (setter)
#     def set_balance(self, amount):
#         if amount >= 0:
#             self.__balance = amount
#         else:
#             print("Invalid balance amount!")

# acc1 = BankAccount("Rohit", 50000)

# # Accessing private variable safely
# print("Balance:", acc1.get_balance())

# # Modifying private variable safely
# acc1.set_balance(60000)
# print("Updated Balance:", acc1.get_balance())


# class Book:
#     def __init__(self, title, author):
#         self.title = title      # public
#         self.author = author    # public

#     def show_details(self):
#         print(f"Book: {self.title}, Author: {self.author}")

# # Creating objects
# b1 = Book("Python Basics", "John Smith")
# b2 = Book("OOP in Python", "Mary Thomas")

# b1.show_details()
# b2.show_details()

# # Accessing public attributes directly
# print(b1.title)
# print(b2.author)


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self._salary = salary    # protected

# class Manager(Employee):
#     def show_info(self):
#         print(f"Manager: {self.name}, Salary: ₹{self._salary}")

# # Creating object
# m1 = Manager("Riya", 75000)
# m1.show_info()

# # Accessing protected attribute outside (possible but not advised)
# print("Accessing protected salary outside:", m1._salary)


# class Locker:
#     def __init__(self, pin):
#         self.__pin = pin  # private

#     def verify_pin(self, user_pin):
#         if user_pin == self.__pin:
#             print("Access Granted ")
#         else:
#             print("Access Denied ")

# l1 = Locker(1234)
# l1.verify_pin(1234)
# l1.verify_pin(9999)

# # Trying to access directly 
# # print(l1.__pin)

# # Access using name mangling 
# print("Accessing private attribute:", l1._Locker__pin)

# 

# user_input = input("enter the number")
# try:
#     number = int(user_input)
#     print(number)
# except ValueError:
#     print("Please enter the correct value")
# else:
#     print("value is correct")
# finally:
#     print("Program exceuted successfully")

# a  = input("enter the number")
# b = 5
# try:
#     result = a+b
#     print(result)
# except TypeError:
#     print("Please enter the correct value")
# else:
#     print("Correct values")
# finally:
#     print("program excecuted succcesfully")


# my_list = [3,32,45,32]
# index = int(input("Enter the index"))
# try:
#     print(my_list[index])
# except IndexError:
#     print("Please enter the correct index value")
# finally:
#     print("Program executed successfully")


# my_dict = {"name":"saloni","age":20}
# key = input("enter the key")
# try:
#     print(my_dict[key])
# except KeyError:
#     print("Please enter the correct key")
# except ValueError:
#     print("Please enter correct value")
# else:
#     print("correct key")
# finally:
#     print("Program executed successfully")

#  Write a Python program to perform division while handling different exceptions.
# Requirements:
# Take two integers as input — a numerator and a denominator.
# Attempt to divide the numerator by the denominator.

# Handle the following exceptions:

# ArithmeticError: If division by zero occurs, display an appropriate error message.
# ValueError: If non-integer values are entered.
# Exception: For any other unexpected errors.
# If the division is successful, display the result.

# Example:
#  Given numerator = 1 and denominator = 0, the program should handle the division by zero 
# and display an error message instead of crashing.


# try:
#     numerator = int(input("enter the number"))
#     denominator = int(input("enter the number"))
#     result = numerator/denominator
#     print(result)
# except ArithmeticError:
#     print("Please enter the correct values")
# except ValueError:
#     print('Please enter the correct values')
# except Exception as e:
#     print(e)
# finally:
#     print('program executed successfully')

# 2.Write a Python program to convert a temperature from Celsius to Fahrenheit.
# Requirements:
# If the input temperature is below absolute zero (-273.15°C), 
# raise an exception with the message "Temperature below absolute zero is not valid."
# Convert Celsius to Fahrenheit using the formula:
#  Fahrenheit = (Celsius × 9 / 5) + 32
# Display both the Celsius and Fahrenheit temperatures.
# Error Handling:
# If the temperature is below absolute zero, catch the exception 
# and display "Invalid Argument" with the error message.

# def convert_to_fahernite(celsius):
#     if celsius <-273.15:
#         raise ValueError("Please enter the correct value")
#     Fahrenheit = (celsius * 9 / 5) + 32
#     return Fahrenheit
# try:
#     celsius = float(input("enter the  value"))
#     Fahrenheit = convert_to_fahernite(celsius)
#     print(celsius)
#     print(Fahrenheit)
# except ValueError as e:
#     print(e)
# except Exception:
#     print("An unknown error occured")

# 3.If any other unexpected error occurs, display "An unknown error occurred."
# Ask the user for a filename.
# Try to open and read the file.
# Handle the following:
# FileNotFoundError: If the file does not exist, display an error.
# PermissionError: If permission is denied.
# Exception: For any other unexpected errors.
# If successful, print the file contents.
# Example:
# If the user enters a non-existing filename, display
# Error: File not found.





