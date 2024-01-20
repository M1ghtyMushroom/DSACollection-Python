from Node import Node

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def append(self, value):
    newNode = Node(value)

    if self.head is None:
      self.head = newNode
      self.tail = newNode
    else:
      self.tail.next = newNode
      self.tail = newNode
    self.length += 1

  def insert(self, index, value):
    if index > self.length or index < 0:
      raise IndexError("Index is out of range!")
    elif index == 0:
      newNode = Node(value, self.head)
      self.head = newNode
    else:
      i = 0
      cur = self.head
      while i < index-1:
        cur = cur.next
        i += 1

      newNode = Node(value, cur.next)
      cur.next = newNode

      if index == self.length:
        self.tail = newNode

      self.length += 1

  def update(self, index, value):
    if index > self.length:
      raise IndexError("Index is out of range!")
    else:      
      i = 0
      prev = self.head
      while i < index-1:
        prev = prev.next
        i += 1
      prev.next = Node(value, prev.next.next)
      if index == self.length:
        self.tail = prev.next

  def delete(self, index):
    if index > self.length or index < 0:
      raise IndexError("Index is out of range!")
    else:
      i = 0
      cur = self.head
      while i < index-1:
        cur = cur.next
        i += 1
      if cur.next.next is not None:
        cur.next = cur.next.next
      else:
        cur.next = None
        self.tail = cur
      self.length -= 1

  def get(self, index):
    if self.head is None:
      raise IndexError("List is empty!")
    elif index > self.length:
      raise IndexError("Index is out of range!")
    else:
      i = 0
      cur = self.head
      while i < index:
        cur = cur.next
        i += 1
        
      return cur.value

  def display(self):
    cur = self.head

    print('[', end = '')
    while cur.next != None:
      print(cur, end = ', ')
      cur = cur.next
    print(cur, end = '')
    print(']')

  def length(self):
    return self.length

  def first(self):
    return self.head.value
  
  def last(self):
    return self.tail.value
