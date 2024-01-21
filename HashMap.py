# ===== Notes ===== #
# a bad hash was used just for learning purposes and may cause collisions

# down there is another methods to set and get items from the hashmap using magic methods
# def __setitem__(self, key, value):
#   hash = self._getHash(key)
#   self.arr[hash] = value
# def __getitem__(self, key):
#   hash = self._getHash(key)
#   return self.arr[hash]
# __setitem__ and __getitem__ are magic methods that allow us to use the [] operator on our HashMap class. e.g. myHashMap['key'] = 'value'
# ================= #

class HashMap:
  def __init__(self, size=10):
    self.size = size
    self.arr = [None] * size

  def _getHash(self, key):
    h = hash(key) % self.size
    return h
  
  def set(self, key, value):
    h = self._getHash(key)
    self.arr[h] = value

  def get(self, key):
    h = self._getHash(key)
    return self.arr[h]
  
  def delete(self, key):
    h = self._getHash(key)
    self.arr[h] = None
