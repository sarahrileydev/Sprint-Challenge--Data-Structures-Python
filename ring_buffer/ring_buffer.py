class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current < self.capacity:
      self.storage[self.current] = item
    else:
      self.current = 0 
      self.storage[self.current] = item
    self.current += 1
    

  def get(self):
    list = []
    for item in self.storage:
      if item is not None:
        list.append(item)
    return list 
