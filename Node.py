class Node :
  def __init__(self, value, next = None, prev = None) :
    self.value = value
    self.next = next
    self.prev = prev

  def getValue(self) :
    return self.value

  def getNext(self) :
    return self.next
  
  def setValue(self, value) :
    self.value = value

  def setNext(self, next) :
    self.next = next

  def __str__ (self) :
    return str(self.value)
