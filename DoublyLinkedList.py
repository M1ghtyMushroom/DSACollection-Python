from Node import Node

class DoublyLinkedList:
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
      newNode.prev = self.tail
      self.tail.next = newNode
      self.tail = newNode
    self.length += 1

  def insert(self, index, value):
    if index > self.length or index < 0:
      raise IndexError("Index is out of range!")
    
    newNode = Node(value)
    if index == 0:
      newNode.next = self.head
      self.head.prev = newNode if self.head is not None else None
      self.head = newNode
      self.tail = newNode if self.tail is None else self.tail
    else:
      i = 0
      cur = self.head
      while i < index-1:
        cur = cur.next
        i += 1

      newNode.next = cur.next
      newNode.prev = cur
      if cur.next is not None:
        cur.next.prev = newNode
      else:
        self.tail = newNode
      cur.next = newNode
    self.length += 1

  def update(self, index, value):
    if index >= self.length or index < 0:
      raise IndexError("Index is out of range!")
    else:      
      i = 0
      cur = self.head
      while i < index:
        cur = cur.next
        i += 1
      cur.value = value

  def delete(self, index):
    if index >= self.length or index < 0:
      raise IndexError("Index is out of range!")
    elif index == 0:
      self.head = self.head.next
      self.head.prev = None
      self.length -= 1
    else:
      i = 0
      cur = self.head
      while i < index-1:
        cur = cur.next
        i += 1
      if cur.next.next is not None:
        cur.next = cur.next.next
        cur.next.prev = cur
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
    if self.head is None:
      print('[]')
    else:
      cur = self.head

      print('[', end = '')
      while cur:
        print(cur, end = '')
        print(', ', end='') if cur.next is not None else None
        cur = cur.next
      print(']')

  def displayReverse(self):
    cur = self.tail

    print('[', end = '')
    while cur:
      print(cur, end = '')
      print(', ', end='') if cur.prev is not None else None
      cur = cur.prev
    print(']')

  def length(self):
    return self.length

  def first(self):
    return self.head.value
  
  def last(self):
    return self.tail.value

  def isEmpty(self):
	  return self.head is None


