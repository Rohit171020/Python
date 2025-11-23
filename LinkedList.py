# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_at_end(self, val):
#         new_node = Node(val)
#         if self.head is None:
#             self.head = new_node
#             return
#         temp = self.head
#         while temp.next is not None:
#             temp = temp.next
#         temp.next = new_node

#     def traverse(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print("None")

# # Example usage:
# ll = LinkedList()
# ll.insert_at_end(10)
# ll.insert_at_end(20)
# ll.insert_at_end(30)
# ll.traverse()   # Output: 10 -> 20 -> 30 -> None



# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def traverse(self):
#         temp = self.head          # Step 1: start from head
#         while temp is not None:   # Step 2: repeat until end
#             print(temp.data, end=" -> ")
#             temp = temp.next      # Step 3: move to next node
#         print("None")
# ll = LinkedList()
# ll.head = Node(10)
# ll.head.next = Node(20)
# ll.head.next.next = Node(30)
# ll.traverse()

# class Node:
#     def __init__(self,val):
#         self.data = val
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def traverse(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.data)
#             temp = temp.next
#         print("None")
# li = LinkedList()
# li.head = Node(10)
# li.head.next = Node(20)
# li.head.next.next = Node(30)



        