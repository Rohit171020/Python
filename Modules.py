# import os
# os.remove("Shardha.py")

# a = int(input("Enter your number:"))
# b = int(input("Enter your number:"))
# try:
#     c = a/b
#     print("Result",c)
# except:
#     print("Can't divide to zero")
# print("Ankit")
# print("hey how are u")

# a = int(input("Enter your number:"))
# b = int(input("Enter your number:"))
# try:
#     c = a/b
#     print("Result",c)
# except:
#     print("Can't divide to zero")
# else:
#     print("Ankit")


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# result = a / b   # Error if b = 0
# print("Result is:", result)


# try:
#     # Code that might cause an exception
# except ExceptionType:
#     # Code to handle the exception
# else:
#     # Code that runs if no exception occurs
# finally:
#     # Code that always runs (optional)


# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     result = a / b
#     print("Result:", result)
# except ZeroDivisionError:
#     print(" You cannot divide by zero. Please enter a valid number.")


# Step 1: Take inputs from the user
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# # Step 2: Try block (risky code goes here)
# try:
#     c = a / b
#     print("Result:", c)
# # Step 3: Except block (handles errors)
# except:
#     print(" Error: Cannot divide by zero. Please enter a valid number.")
# # Step 4: Else block (runs if no exception occurs)
# else:
#     print("Division successful. No error occurred.")
#     print("Ankit")
# # Step 5: Finally block (always runs)
# finally:
#     print("🔚 Program execution completed.")



# numerator = int(input("Enter numerator: "))
# denominator = int(input("Enter denominator: "))

# # Handling division safely
# try:
#     result = numerator / denominator
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# finally:
#     print("Division attempt completed.\n")



# user_input = input("Enter a number: ")

# try:
#     number = int(user_input)
#     print("You entered the number:", number)
# except ValueError:
#     print("Invalid value! Please enter a valid integer.")
# finally:
#     print("Input check completed.\n")


# a = input("Enter a string: ")
# b = 5

# try:
#     result = a + b
#     print("Result:", result)
# except TypeError:
#     print(" Type error! Cannot add string and integer.")
# finally:
#     print(" Operation attempted.\n")



# my_list = [10, 20, 30]
# index = int(input("Enter the index to access: "))

# try:
#     print("Value at index:", my_list[index])
# except IndexError:
#     print(" Index error! List index out of range.")
# finally:
#     print(" List access attempt completed.\n")


# my_dict = {"name": "Rohit", "age": 25}
# key = input("Enter the key to look up: ")

# try:
#     print("Value:", my_dict[key])
# except KeyError:
#     print(" Key error! Key does not exist.")
# finally:
#     print("Dictionary lookup attempt completed.\n")


# try:
#     print(my_variable)  # This variable is not defined
# except NameError:
#     print(" Name error! Variable is not defined.")
# finally:
#     print("Variable check completed.\n")



# a = int(input("Enter the number:"))
# b = int(input("Enter the number:"))
# try:
#     c = a/b
#     print(c)
# except:
#     print("cannot divide by zero: Please enter a valid number")
# else:
#     print("Division successfull,No error occured")
# finally:
#     print("Program executed successfully")

# a = int(input("Enter the number:"))
# b = int(input("Enter the number:"))
# try:
#     c = a/b 
#     print(c)
# except ZeroDivisionError:
#     print("Please enter the correct number")
# finally:
#     print("Program executed successfully")

# user_input = input("Enter the number:")
# try:
#     number = int(user_input)
#     print(number)
# except ValueError:
#     print("Please enter the correct value")
# finally:
#     print("Input check completed")

# Program to handle multiple exceptions during division

# try:
#     numerator = int(input("Enter numerator: "))
#     denominator = int(input("Enter denominator: "))
#     result = numerator / denominator
#     print("Division successful! Result:", result)
# except ArithmeticError:
#     print("Arithmetic Error: Division by zero is not allowed.")
# except ValueError:
#     print("Value Error: Please enter valid integer values.")
# except Exception as e:
#     print("Unexpected Error:", e)
# finally:
#     print("Program execution completed.")


# def convert_to_fahrenheit(celsius):
#     if celsius < -273.15:
#         raise ValueError("Temperature below absolute zero is not valid.")
#     fahrenheit = (celsius * 9 / 5) + 32
#     return fahrenheit
# try:
#     celsius = float(input("Enter temperature in Celsius: "))
#     fahrenheit = convert_to_fahrenheit(celsius)
#     print(f"Temperature in Celsius: {celsius}°C")
#     print(f"Temperature in Fahrenheit: {fahrenheit}°F")

# except ValueError as e:
#     print("Invalid Argument:", e)
# except Exception:
#     print("An unknown error occurred.")


# my_dict = {"name": "Rohit", "age": 25}
# key = input("Enter the key to look up: ")
# try:
#    print("Value:", my_dict[key])
# except KeyError:
#    print("Key error! Key does not exist.")
# finally:
#    print("Dictionary lookup attempt completed.\n")


# try:
#     filename = input("Enter the filename: ")
#     with open(filename, "r") as file:
#         content = file.read()
#         print("File content:\n", content)
# except FileNotFoundError:
#     print("Error: File not found.")
# except PermissionError:
#     print("Error: Permission denied to read the file.")
# except Exception as e:
#     print("Unexpected Error:", e)
# finally:
#     print("Program execution completed.")

# try:
#     numerator = int(input("enter the number"))
#     denominator = int(input("enter the number"))
#     result = numerator/denominator
#     print(result)
# except ArithmeticError:
#     print("Arithmatic error: Division by Zero is not allowed")
# except ValueError:
#     print("Value error: Please enter a valid integer")
# except Exception as e:
#     print("Unexcepted error",e)
# finally:
#     print("Program execution completed")



