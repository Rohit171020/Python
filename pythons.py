# file = open("sample.txt", "r")
# content = file.read()
# print(content)
# file.close()


# file = open("sample.txt", "w")
# file.write("hey everyone can u please tell me something about yourself.")
# file.write("\nHey i am fine.")
# file.write("\nhey can u please help me to learn the python.")
# file.close()


# file = open("sample.txt","w")
# file.write("hey everyone can u please tell me about sri")


# file = open("samples.txt","a")
# # file.write("hey can u please tell how it your python classes going on.")
# file.write("Hey tell me more about it")
# file.close()


# file = open("samples.txt","r")
# print(file.read())
# file.close()

# file = open("samples.txt","r")
# print(file.readline())
# print(file.readline())


# file = open("samples.txt","r")
# lines = file.readlines()
# print(lines)
# file = open("samples.txt","a")
# file.write("Hey how are u")

# file = open("samples.txt","a")
# file.write("hey can u please tell me")





# file = open("samples.txt","r")
# # print(file.readline())
# # print(file.readline())
# print(file.readlines())


# file = open("samples.txt", "w")
# file.write("This is first line.")
# file.write("This is second line.")

# file = open("sample.txt", "w")
# file.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])
# file.close()

with open("sample.txt", "r") as file:
   content = file.read()
   print(content)


# with open("sample.txt", "r") as file:
#    content = file.read()
#    print(content)



# # Step 1: Write numbers into file
# numbers = ["10\n", "20\n", "30\n", "40\n", "50\n"]
# with open("numbers.txt", "w") as file:
#     file.writelines(numbers)

# # Step 2: Read numbers and calculate sum
# with open("numbers.txt", "r") as file:
#     total = 0
#     for line in file:
#         total += int(line.strip())
#     print("Sum of numbers:", total)


# Step 1: Write numbers into file
# numbers = ["10\n", "20\n", "30\n", "40\n", "60\n"]
# file = open("samples.txt", "w")     # open in write mode
# file.writelines(numbers)
# file.close()                        # close manually

# # Step 2: Read numbers and calculate sum
# file = open("samples.txt", "r")     # open in read mode
# total = 0
# for line in file:
#     total += int(line.strip())
# file.close()                        # close manually
# print("Sum of numbers:", total)


# with open("sample.txt", "r") as file:
#     text = file.read()

# lines = text.split("\n")
# words = text.split()
# characters = len(text)

# print("Lines:", len(lines))
# print("Words:", len(words))
# print("Characters:", characters)

# Step 1: Write student marks
# marks = ["85\n", "90\n", "78\n", "92\n", "88\n"]
# with open("samplez.txt", "w") as file:
#     file.writelines(marks)

# # Step 2: Read and calculate average
# with open("samplez.txt", "r") as file:
#     data = file.readlines()
#     numbers = [int(x.strip()) for x in data]
#     average = sum(numbers) / len(numbers)

# print("Average Marks:", average)


# file = open("samples.txt", "r")
# lines = file.readlines()
# file.close()

# num_lines = len(lines)
# num_words = 0
# for line in lines:
#     num_words += len(line.split())

# print("Lines:", num_lines)
# print("Words:", num_words)


# file = open("samples.txt", "r")
# text = file.read()
# file.close()
# words = text.split()
# freq = {}
# for word in words:
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1
# print("Word frequencies:", freq)


# friends = ["Amit\n", "Suman\n", "Priya\n", "Rahul\n", "Neha\n"]
# file = open("friends.txt", "w")
# file.writelines(friends)
# file.close()
# print("Friends saved in friends.txt")

# friends = ["Amit\n", "Suman\n", "Priya\n", "Rahul\n", "Neha\n"]

# with open("friendss.txt", "w") as file:
#     file.writelines(friends)

# print("Friends saved in friends.txt")


# file = open("friendss.txt", "r")
# lines = file.readlines()
# num_lines = len(lines)
# num_words = sum(len(line.split()) for line in lines)
# print("Number of lines:", num_lines)
# print("Number of words:", num_words)


# with open("friends.txt", "r") as file:
#     lines = file.readlines()
# num_lines = len(lines)
# num_words = sum(len(line.split()) for line in lines)
# print("Number of lines:", num_lines)
# print("Number of words:", num_words)


# Open the file in read mode
# with open("sample.txt", "r") as file:
#     text = file.read()  # Read the whole content
# # Split text into words
# words = text.split()  # Default splits by whitespace
# # Create an empty dictionary to store word frequency
# word_freq = {}
# # Count frequency of each word
# for word in words:
#     if word in word_freq:
#         word_freq[word] += 1
#     else:
#         word_freq[word] = 1

# # Print the result
# # for word, freq in word_freq.items():
# print(f"{word}: {word_freq}")


# Read fruits from file
# with open("fruits.txt", "r") as file:
#     lines = file.readlines()  # Get all lines

# # Loop through each fruit and check
# for line in lines:
#     fruit = line.strip()  # Remove newline character
#     if fruit.startswith("A"):  # Check if fruit starts with 'A'
#         print(fruit)


# Read numbers from file
# with open("numbers.txt", "r") as file:
#     lines = file.readlines()  # Get all lines from file
# # Initialize sum
# total = 0
# # Loop through each line
# for line in lines:
#     number = int(line.strip())  # Remove newline and convert to integer
#     total += number             # Add to total

# print("Sum of numbers:", total)

# Read marks from file
# with open("marks.txt", "r") as file:
#     lines = file.readlines()  # Get all lines
# # Initialize total
# total = 0
# # Count number of students
# num_students = len(lines)
# # Loop through each line and add marks
# for line in lines:
#     mark = int(line.strip())  # Remove newline and convert to integer
#     total += mark
# # Calculate average
# average = total / num_students
# print("Average marks:", average)
