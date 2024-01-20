# Jan 20, 2024
# from Node import Node
# first = Node(5) # the end of the list
# second = Node(6, first)
# print(second.getNext())
# ================================ #
from LinkedList import LinkedList

x = LinkedList()

x.append(1)
x.append(2)
x.append(3)

x.update(1, "BOMB")
x.delete(2)

x.display()