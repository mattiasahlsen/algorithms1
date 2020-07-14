import random

class Node:
  def __init__(self):
    self.parent = self

  def get_root(self):
    if self.parent == self:
      return self
    else:
      # make all parents root to make the tree more shallow
      root = self.parent.get_root()
      self.parent = root
      return root

  def connected_to(self, node):
    return self.get_root() == node.get_root()
  
  def connect_to(self, node):
    root = self.get_root()
    root.parent = node.get_root()



class Percolation:
  def __init__(self, n):
    self.nodes = [Node() for i in range(n * n + 2)]
    for node in self.nodes:
      node.is_open = False

    self.top_node = self.nodes[0]
    self.bottom_node = self.nodes[-1]

    for node in self.nodes[1:n + 1]:
      node.connect_to(self.top_node)

    for node in self.nodes[-n - 1:]:
      node.connect_to(self.bottom_node)

    self.n = n

  def open(self, row, col):
    node = self.nodes[self.pos(row, col)]
    node.is_open = True

    surrounding = []
    if row > 0: surrounding.append(self.pos(row - 1, col))
    if row < self.n - 1: surrounding.append(self.pos(row + 1, col))
    if col > 0: surrounding.append(self.pos(row, col - 1))
    if col < self.n - 1: surrounding.append(self.pos(row, col + 1))

    for adjacent_node in [self.nodes[p] for p in surrounding]:
      if adjacent_node.is_open:
        node.connect_to(adjacent_node)

  def is_open(self, row, col):
    node = self.nodes[self.pos(row, col)]
    return node.is_open

  def is_full(self, row, col):
    node = self.nodes[self.pos(row, col)]
    return node.connected_to(self.top_node)

  def number_of_open_sites(self):
    return [node.is_open for node in self.nodes].count(True)

  def percolates(self):
    return self.bottom_node.connected_to(self.top_node)

  def percolate(self):
    while not self.percolates():
      self.open_random()

  def open_random(self):
    row, col = random.randint(0, self.n - 1), random.randint(0, self.n - 1)
    self.open(row, col)



  def pos(self, row, col):
    return row * self.n + col + 1
    


