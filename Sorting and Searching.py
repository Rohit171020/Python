# import math
# print(math.sqrt(25))
# print(math.floor(5.4))
# print(math.factorial(6))
# print(math.ceil(4.3))

# import random
# num = random.randint(1,90)
# print(num)


# import random
# names  = ["Govind","Pranitha","Daksh","Vaishanvi","Aryan"]
# random.shuffle(names)
# print(names)


# import datetime
# now  = datetime.datetime.now()
# print(now)

# import datetime
# now  = datetime.date.today()
# print(now.month)
# print(now.year)
# print(now.day)

# Create a module currency_converter.py containing a 
# function usd_to_inr(usd) that converts USD to INR (1 USD = ₹83.2).
# Then use it in another file.

# import currency_converter
# print(currency_converter.usd_to_inr(100))

# Find the area of a circle with radius = 7 using the math module.

# import math
# radius = 8
# area = math.pi*math.pow(radius,2)
# print(area)

# Find the greatest integer less than or
# equal to 8.7 and smallest integer greater than or equal to 8.7.


#Find your age in years and days if your birth date is 18 May 1947.

# import datetime
# dob = datetime.date(1947,5,18)
# today= datetime.date.today()
# age_days = (today-dob).days
# age_years =  age_days //365
# print(age_years)
# print(age_days)


# Create a Scientific Calculator using a User-Defined Module
#  Task:
# Make a module scientific_calc.py with functions to find:
# square root
# power
# sine of an angle
# factorial
# Then use it from another Python file
# import scientific_calc as sc
# print(sc.square_root(54))
# print(sc.pow(2,3))
# print(sc.factorial(6))
# print(sc.sin(13))


# Create a Python program that acts as a Random Quiz Game.
#  Your program should:
# Have a list of multiple-choice questions (at least 3–5).
# Randomly select one question each time the program runs.
# Display the question and the available options (A, B, C, D).
# Accept user input (their selected option).
# Check if the answer is correct and print whether it’s  Correct or Wrong.
# Show the correct answer if the user chooses the wrong option.
# import random
# quiz = [
#     { 
#         "question1":"what is the capital of India?",
#         "options":{
#             "a":"Mumbai",
#             "b":"Chennai",
#             "c":"New Delhi",
#             "d":"Kolkata"
#         },
#         "answer": "c"
#     },
#     {
#         "question2":"who is develooed python?",
#         "options":{
#             "a":"Guido van Rossum",
#             "b":"Elon Musk",
#             "c":"Bill Gates",
#             "d":"Mark Zuckerberg"
#     }
#     "answer": "a"
#     },
# ]
# selected_questions = random.choice(quiz)
# print(selected_questions)
# for key,value in selected_questions["options"].items():
#     print(f"{key}: {value}")
# user_answer = input("enter your option:(A/B/C/D)").upper()
# if user_answer == selected_questions["answer"]:
#     print("Correct!")
# else:
#     correct_option = selected_questions["answer"]
#     print("wrong answer")
#     print(f"The correct answer is option{correct_option}.{selected_questions['options'][correct_option]}")




# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0,n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#                 swapped = True
#         if not swapped:
#             break
#     return arr
# print(bubble_sort([5,3,8,4,2]))

# def selection_sort(arr):
#     n= len(arr)
#     for i in range(n-1):
#         min_idx = i
#         for j in range(i+1,n):
#             if arr[j]<arr[min_idx]:
#                 min_idx = j
#         arr[i],arr[min_idx] = arr[min_idx],arr[i]
#     return arr
# arr = [5,3,8,4,2]
# sorted_arr = selection_sort(arr)
# print(sorted_arr)

# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         key = arr[i]
#         j = i- 1
#         while j>=0 and arr[j]>key:
#             arr[j+1] = arr[j]
#             j-=1
#         arr[j+1] = key
#         print(arr)
#     print(arr)
#     return arr
# insertion_sort([5,3,4,8,2])

# def linear_search(arr,target):
#     for i in range(len(arr)):
#         if arr[i]== target:
#             return i
#     return -1
# numbers = [2,4,8,1,90]
# target = 4
# result = linear_search(numbers,target)
# if result!=-1:
#     print("element found correct index")
# else:
#     print("element not found at correct index")
    
# def binary_search(arr,target):
#     low = 0
#     high = len(arr)-1
#     while low<=high:
#         mid = (low+high)//2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid]<target:
#             low = mid+1
#         else:
#             high = mid-1
#     return -1
    













