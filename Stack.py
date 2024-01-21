from Node import Node

class Stack():
  def __init__ (self):
    self.top = None
    self.length = 0

  def push(self, value):
    newNode = Node(value)
    if self.length == 0:
      self.top = newNode  
    else:
      newNode.next = self.top
      self.top = newNode
    self.length += 1
    
  def pop(self): # removes the top element and returns it
    if self.length == 0:
        return
    popped = self.top.value
    self.top = self.top.next
    self.length -= 1
    return popped
  
  def peek(self):
    if self.length == 0:
        return
    return self.top.value

  def isEmpty(self):
      return self.length == 0

  def display(self):
    current = self.top
    while current is not None:
      print(current.value, end=" ")
      current = current.next