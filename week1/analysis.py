from percolation import Node, Percolation
import sys
import random
import time
import matplotlib.pyplot as plt



class PercolationStats:
  def __init__(self, n, trials):
    self.percs = []
    self.n = n
    self.trials = trials

    thresholds = []

    for i in range(trials):
      perc = Percolation(n)
      self.percs.append(perc)

      perc.percolate()

      threshold = perc.number_of_open_sites() / (n * n)
      print(f'trial {i} complete, percolation threshold: {threshold}')

      print('i: ' + str(i) + ', threshold: ' + str(threshold))

      thresholds.append(threshold)

      plt.clf()
      plt.title('Percolation Thresholds')
      plt.xlabel('Trial #')
      plt.ylabel('Threshold')
      plt.axis([1, trials, 0, 1])
      plt.plot(range(i + 1), thresholds, '-')
      plt.pause(0.05)

    plt.show()


  def mean(self):
    return sum([
      perc.number_of_open_sites() / (perc.n * perc.n)
      for perc in self.percs
    ]) / self.trials

  def stddev(self):
    mean = self.mean()
    deviations = [
      (perc.number_of_open_sites() / (perc.n * perc.n)) - mean
      for perc in self.percs
    ]
    deviations_squared = [pow(deviation, 2) for deviation in deviations]
    mean_deviations_squared = sum(deviations_squared) / len(deviations)
    return pow(mean_deviations_squared, 0.5)


n = int(input('n: '))
trials = int(input('number of trials: '))

start_time = time.monotonic()

percolation_stats = PercolationStats(n, trials)

print('seconds spent: ',(time.monotonic() - start_time))

print('mean: ' + str(percolation_stats.mean()))
print('standard deviation: ' + str(percolation_stats.stddev()))
      
