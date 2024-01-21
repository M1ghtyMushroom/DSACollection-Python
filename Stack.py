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
    
  def pop(self):
    if self.length == 0:
        raise Exception("Stack is empty")
    popped = self.top.value
    self.top = self.top.next
    self.length -= 1
    return popped
  
  def peek(self):
    if self.length == 0:
        raise Exception("Stack is empty")
    return self.top.value

  def is_empty(self):
      return self.length == 0

  def display(self):
    current = self.top
    while current is not None:
      print(current.value, end=" ")
      current = current.next