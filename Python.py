
# * * * *
# * * * *
# * * * *
# * * * *
# n = 5
# for i in range(n):
#     for j in range(n):
#         print("*",end = " ")
#     print()


# i=0 *
# i=1 * *
# i=2 * * *
# i =3* * * *
# i =4 * * * * *

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end= " ")
#     print()


# * * * * * 0-5
# * * * *. 1-5
# * * *.   2-5
# * *.     3-5
# *.       4-5

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end = " ")
#     print()


#         * first print spaces then i = 0 me one start
#       * * i = 1 -> 2 star
#     * * *. i = 3 -> 3 star
#   * * * *. i = 4 -> 4 star
# * * * * *. i = 5 -> 5 start

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print('',end = " ")
#     for j in range(i,n):
#         print("*",end = " ")
#     print()


# n = 5
# for i in range(n):              # rows
#     for j in range(i,n):             # spaces
#         print(" ", end=" ")
#     for j in range(i+1):               # stars
#         print("*", end=" ")
#     print()

# system_running = True
# while system_running:
#     command= input("enter the command (on/off/exit)").strip().lower()
#     if command == "on":
#         print("light turned ON")
#     elif command == "off":
#         print("lights turned OFF ")
#     elif command == "exit":
#         print("smart home system shutting down")
#     else:
#         print("invalid input")

# s = set((1,2,3))
# print(s)

s = {{1,2,3}}
print(s)