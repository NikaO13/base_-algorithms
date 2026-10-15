from collections import deque


class AVLNode:
  def __init__(self,key):
    self.key = key
    self.right = None
    self.left = None
    self.height = 0
    

def rotate_left(a):
  b = a.right
  middle = b.left
  b.left = a
  a.right = middle
  update_height(a)
  update_height(b)
  return b

def rotate_right(a):
    b = a.left
    middle = b.right
    b.right = a
    a.left = middle
    update_height(a)
    update_height(b)
    return b

def rebalance(node):
  update_height(node)
  balance = balance_factor(node)
  
  if balance <= -2:
    if balance_factor(node.left) > 0:
      node.left = rotate_left(node.left)
    return rotate_right(node)
  
  if balance >= 2:
    if balance_factor(node.right) < 0:
      node.right = rotate_right(node.right)
    return rotate_left(node)
  return node

def update_height(node):
  node.height = 1 + max(height(node.left), height(node.right))
           
def balance_factor(node):
  return get_height(node.left) - get_height(node.right)
  
def height(node):
  if node is None:
        return -1
  return node.height

def lvlorder(node:AVLNode):
  que = deque([[node]])
  
  while que:
    lvl = que.popleft()
    for i in range(0, len(lvl)):
      print(f'{lvl[1].key}', end='')
      
    lis = []
    for _ in lvl:
      if not _.left is None:
        lis.append(_.left)
      if not _.right is None:
        lis.append(_.right)
        
      if lis:
        que.append(lis)
    print()
    
node = AVLNode(10)
lvlorder(node)
