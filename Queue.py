from Node import Node

class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
    self.length = 0

  def enqueue(self, value):
    newNode = Node(value)

    if self.length == 0:
      self.front = newNode
      self.rear = newNode
    else:
      self.rear.next = newNode
      self.rear = newNode

    self.length += 1

  def dequeue(self):
    if self.length <= 0:
      raise Exception("Queue is empty")
    else:
      self.front = self.front.next

    self.length -= 1

  def peek(self):
    return self.front.value
  
  def display(self):
    current = self.front
    while current is not None:
      print(current.value, end=" ")
      current = current.next