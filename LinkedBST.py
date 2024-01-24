from TreeNode import TreeNode

class LinkedBST :
  def __init__(self):
    self.root = None

  def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert(value, self.root)

  def _insert(self, value, node):
    if value < node.value:
      if node.left:
        self._insert(value, node.left)
      else:
        node.left = TreeNode(value)
    else:
      if node.right:
        self._insert(value, node.right)
      else:
        node.right = TreeNode(value)
    
  def _view(self, node):
    if node:
      self._view(node.left)
      print(node.value, end=" ")
      self._view(node.right)

  def view(self):
    if self.root:
      self._view(self.root)
