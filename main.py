# Jan 20, 2024
# from Node import Node
# first = Node(5) # the end of the list
# second = Node(6, first)
# print(second.getNext())
# ================================ #
from DoublyLinkedList import DoublyLinkedList

x = DoublyLinkedList()

x.append(1)
x.append(2)
x.append(3)

x.delete(0)
x.display()
# x.displayReverse()
print(x.isEmpty())
