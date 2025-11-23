# file = open("sample.txt","r")
# content = file.read()
# print(content)
# file.close()

# file = open("sample.txt","w")
# file.write("Hey everyone.")
# file.write("\nhey how are u")

# file = open("sample.txt","a")
# file.write("\nHey everyone.")
# file.close()
# read()->
# file = open("sample.txt","r")
# print(file.read())


# readline()
# file = open("sample.txt","r")
# print(file.readline())
# print(file.readline())
# print(file.readline())

# file = open("sample.txt","r")
# print(file.readlines())

# write()
# file = open("sample.txt","w")
# file.write("hey how are u")

# Writelines()
# file = open("sample.txt","w")
# file.writelines(["hey How are u\n","Today we are going to Banglore"])

# with open("sample.txt","r") as file:
#     content = file.read()
#     print(content)

# Store a list of 5 friends’ names in a file using writelines().

#Count the number of words and lines in a file
# file = open("sample.txt","r")
# lines = file.readlines()
# file.close()
# num_lines = len(lines)
# num_words = sum(len(line.split()) for line in lines)
# print(num_lines)
# print(num_words)


# Read a text file and count the frequency of each word.
file = open("sample.txt","r")
lines = file.read()
file.close()
words = lines.split()
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] +=1
    else:
        word_freq[word] =1 
print(word_freq)
print(word)

# Create a file fruits.txt with a list of fruits, 
# then print only the fruits that start with the letter 'A'.

# try:
#     num = int("100")  # valid conversion
#     print("Conversion successful")
#     print("Number is:", num)
#     print("End of try block")

# try:
#     print("Starting conversion...")
#     num = int("abc")  # invalid conversion - error here
#     print("This line won't execute")
#     print("Neither will this")

# try:
#     print("Step 1: Getting user input")
#     a = int(input("Enter first number: "))
#     print("Step 2: Getting second input")
#     b = int(input("Enter second number: "))
#     print("Step 3: Performing division")
#     result = a / b
#     print("Result:", result)


# Test case 1: Valid number
# try:
#     num1 = int("25")
#     print("Converted:", num1)

# # Test case 2: Invalid number
# try:
#     num2 = int("hello")
#     print("Converted:", num2)

# # Test case 3: Decimal number
# try:
#     num3 = int("25.5")
#     print("Converted:", num3)

# try:
#     print("Attempting to open file...")
#     file = open("data.txt", "r")
#     print("File opened successfully")
#     content = file.read()
#     print("File content:", content)
#     file.close()
#     print("File closed")

# numbers = [10, 20, 30]

# try:
#     print("Accessing index 0:", numbers[0])
#     print("Accessing index 1:", numbers[1])
#     print("Accessing index 5:", numbers[5])  # This will cause error
#     print("This line won't execute")

# try:
#     num = int(input("Enter a number: "))
#     print("You entered:", num)
# except ValueError:
#     print("Error: Please enter a valid number!")

# try:
#     a = int(input("Enter numerator: "))
#     b = int(input("Enter denominator: "))
#     result = a / b
#     print("Result:", result)
# except ValueError:
#     print("Error: Invalid number format!")
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")

# try:
#     age = int(input("Enter your age: "))
#     if age < 0:
#         raise ValueError("Age cannot be negative")
#     print("Your age is:", age)
# except ValueError as error:
#     print("Input Error:", error)


# try:
#     num = int(input("Enter a number: "))
#     result = 100 / num
#     print("Result:", result)
# except ValueError:
#     print("Invalid number format")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except Exception as e:
#     print("Unexpected error:", e)

# try:
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     result = a / b
#     print(f"{a} / {b} = {result}")
# except ValueError:
#     print("Error: Please enter valid numbers only!")
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed!")



# try:
#     filename = input("Enter filename: ")
#     with open(filename, 'r') as file:
#         content = file.read()
#         print("File content:")
#         print(content)
# except FileNotFoundError:
#     print("Error: File not found!")
# except PermissionError:
#     print("Error: Permission denied to read file!")
# except Exception as e:
#     print("Unexpected error:", e)

# student_grades = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78
# }
# try:
#     name = input("Enter student name: ")
#     grade = student_grades[name]
#     print(f"{name}'s grade: {grade}")
# except KeyError:
#     print("Error: Student not found in records!")



# try:
#     num = int(input("Enter a number: "))
#     result = 100 / num
#     print("Result:", result)
# except ValueError:
#     print("Invalid input!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# finally:
#     print("Program execution completed.")

# file = None
# try:
#     file = open("data.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("File not found!")
# finally:
#     if file:
#         file.close()
#         print("File closed successfully.")


# def divide_numbers():
#     try:
#         a = int(input("Enter first number: "))
#         b = int(input("Enter second number: "))
#         return a / b
#     except ZeroDivisionError:
#         print("Division by zero!")
#         return None
#     finally:
#         print("Function execution completed.")

# result = divide_numbers()
# print("Final result:", result)

# files = []
# try:
#     files.append(open("file1.txt", "w"))
#     files.append(open("file2.txt", "w"))
    
#     # Write to files
#     files[0].write("Data in file 1")
#     files[1].write("Data in file 2")
    
#     print("Files written successfully")
    
# except IOError:
#     print("Error writing to files!")
# finally:
#     # Close all opened files
#     for file in files:
#         if file and not file.closed:
#             file.close()
#     print("All files closed.")


# n = int(input("Enter value of n: "))

# # Outer loop
# for i in range(n):
#     # Inner loop
#     for j in range(n):
#         # Block of code (constant time work)
#         print(f"i={i}, j={j}")

# n = int(input("Enter n: "))
# for i in range(n):
#     print(i)

# n = int(input("Enter n: "))
# for i in range(n):
#     for j in range(n):
#         print(i, j)


# n = int(input("Enter n: "))
# for i in range(n):
#     print(i)
# for j in range(n):
#     print(j)

# n = int(input("Enter n: "))
# i = 1
# while i < n:
#     print(i)
#     i *= 2


# for i = 0 to N
#     for j = 0 to N
#         for k = 0 to N
#             print(i)


# for i = 0 to N
#     print(i)

# for j = 0 to M
#     print(j)

# for i = 0 to N
#     for j = 0 to M
#         print(i)


# Q1.for i = 0 to N
#     print(i)
#     print(i * 2)

# n = int(input("Enter n: "))
# for i in range(n):
#     print(i)

# n = int(input("Enter n: "))
# for i in range(n):
#     for j in range(n):
#         print(i, j)


# n = int(input("Enter n: "))
# for i in range(n):
#     print(i)
# for j in range(n):
#     print(j)

#  for i = 0 to N
#     for j = 0 to N
#         for k = 0 to N
#             print(i)

# for i = 0 to N
#     print(i)

# for j = 0 to M
#     print(j)

# for i = 0 to N
#     print(i)