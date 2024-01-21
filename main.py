# from Node import Node
# first = Node(5) # the end of the list
# second = Node(6, first)
# print(second.getNext())
# ================================ #
# from DoublyLinkedList import DoublyLinkedList
# x = DoublyLinkedList()
# x.append(1)
# x.append(2)
# x.append(3)
# x.delete(0)
# x.display()
# x.displayReverse()
# print(x.isEmpty())
# ================================ #
# from Queue import Queue
# x = Queue()
# x.enqueue(1)
# x.enqueue(3)
# x.enqueue(5)
# print(x.peek())
# x.dequeue()
# print(x.peek())
# x.display()
# ================================ #
# from Stack import Stack
# x = Stack()
# x.pop()
# x.display()
# ================================ #
from HashMap import HashMap

x = HashMap() # default size is 10, you can change it by passing a size to the constructor
x.set('name', 'omar')
x.set('age', 20)
x.set('name', 'ali')

print(x.get('name'))
print(x.get('age'))

x.delete('name')

print(x.get('name'))