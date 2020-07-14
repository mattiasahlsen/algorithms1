import unittest
from percolation import Node, Percolation

class TestQuickUnion(unittest.TestCase):
  def setUp(self):
    self.nodes = [Node() for i in range(20)]
    self.nodes[0].connect_to(self.nodes[1])
    self.nodes[10].connect_to(self.nodes[1])
    

  def test_data(self):
    node = Node()
    node.is_open = False
    self.assertEqual(node.is_open, False)

  def test_root(self):
    self.assertEqual(self.nodes[0].get_root(), self.nodes[1].get_root())
    self.assertEqual(self.nodes[1].get_root(), self.nodes[10].get_root())
    self.assertEqual(self.nodes[0].get_root(), self.nodes[10].get_root())

    self.assertNotEqual(self.nodes[0].get_root(), self.nodes[2].get_root())
    self.assertNotEqual(self.nodes[2].get_root(), self.nodes[3].get_root())

  def test_connected(self):
    self.assertTrue(self.nodes[0].connected_to(self.nodes[1]))
    self.assertTrue(self.nodes[0].connected_to(self.nodes[10]))

    self.assertFalse(self.nodes[0].connected_to(self.nodes[9]))

class TestPercolation(unittest.TestCase):

  def test_init(self):
    perc = Percolation(20)
    self.assertEqual(perc.n, 20)
    self.assertEqual(len(perc.nodes), 20 * 20 + 2)

  def test_open(self):
    perc = Percolation(20)
    perc.open(15, 15)
    self.assertTrue(perc.nodes[15 * 20 + 15 + 1].is_open)
    self.assertTrue(perc.is_open(15, 15))

  def test_full(self):
    perc = Percolation(20)
    perc.open(1, 2)
    self.assertFalse(perc.is_full(1, 2))

    perc.open(0, 2)
    self.assertTrue(perc.is_full(0, 2))
    self.assertTrue(perc.is_full(1, 2))

  def test_number_of_open(self):
    perc = Percolation(20)
    self.assertEqual(perc.number_of_open_sites(), 0)

    perc.open(1, 2)
    perc.open(1, 3)
    self.assertEqual(perc.number_of_open_sites(), 2)

  def test_percolates(self):
    perc = Percolation(5)
    self.assertFalse(perc.percolates())
    perc.open(0, 0)
    perc.open(1, 0)
    perc.open(2, 0)
    perc.open(3, 0)
    self.assertFalse(perc.percolates())
    
    perc.open(4, 0)
    self.assertTrue(perc.percolates())






if __name__ == '__main__':
    unittest.main()
