class BinaryHeap:
  def __init__(self):
    self.data = []
    
    def __len__(self):
      return len(self.data)
    
    def peek_min(self):
      if not self.data:
        raise IndexError('empty heap')
      
    def insert(self, value):
      self.data.append(value)
      sift_up(self.data, len(self.data) - 1)
      
    def extract_min(self):
      if not self.data:
        raise IndexError('empty heap')
      
      result = self.data[0]
      last = self.data.pop()
      
      if self.data:
        self.data[0] = last
        sift_down(self.data, 0)
        
      return result
    
def sift_up(data, i):
  while i > 0:
    p = (i - 1) // 2
    if data[p] <= data[i] : break
    data[p], data[i] = data[i], data[p]
    i = p
    
def sift_down(data, i):
  n = len(data)
  while True:
    l, r, s = 2*i + 1, 2*i + 2, i
    if l < n and data[l] < data[s]: s = l
    if r < n and data[r] < data[s]: s = r
    if s == i: break
    data[i], data[s] = data[s], data[i]
    i = s
    
heap = BinaryHeap()
