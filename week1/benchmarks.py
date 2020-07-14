from percolation import Node, Percolation
import sys
import random
import matplotlib.pyplot as plt
import math
import numpy as np
from benchmark import benchmark

from keras.layers import Dense, BatchNormalization
from keras.models import Sequential


def normalize(values):
  min_v, max_v = min(values), max(values)
  return [(v - min_v) / (max_v - min_v) * 0.9 + 0.1 for v in values]


# initialize
def benchmark_percolation():
  x_min, x_max = 10, 500
  y_min, y_max = 0, 2000
  epochs = 10000
  step, runs = 10, 10

  plt.figure(0)

  def plot(x_vals, y_vals):
    plt.clf()
    plt.title('Benchmarks Percolation()')
    plt.xlabel('n')
    plt.ylabel('execution time (ms)')
    plt.axis([x_min, x_max, y_min, y_max])
    plt.plot(x_vals, y_vals, '-')
    plt.pause(0.05)


  def run_benchmark(n):
    perc = Percolation(n)

  n_vals, times = benchmark(
    func = run_benchmark,
    x_min = x_min,
    x_max = x_max,
    y_min = y_min,
    y_max = y_max,
    plot = plot,
    step = step,
    runs = runs
  )

  n_vals, times = normalize(n_vals), normalize(times)

  # 5 inputs:
  # ln(x)
  # x
  # x^2
  # x^3
  # x^4

  output_layer = Dense(1, input_dim=5)
  model = Sequential([
    output_layer
  ])
  model.compile(
    optimizer='adam', 
    loss='mean_squared_error',
  )
  #model.summary()


  x_train = np.array([
    [math.log(x), x, pow(x, 2), pow(x, 3), pow(x, 4)] for x in n_vals
  ], dtype='float')

  model.fit(
    x_train,
    times,
    epochs = epochs,
    batch_size = 256,
    validation_split=0.1,
    verbose=0
  )
  [weights, biases] = output_layer.get_weights()
  model.summary()

  c_ln = weights[0][0]
  c_x = weights[1][0]
  c_x2 = weights[2][0]
  c_x3 = weights[3][0]
  c_x4 = weights[4][0]
  bias = biases[0]
  print(
    f'time = {c_ln}ln(x) {"-" if c_x < 0 else "+"} '
    f'{abs(c_x)}x {"-" if c_x2 < 0 else "+"} '
    f'{abs(c_x2)}x^2 {"-" if c_x3 < 0 else "+"} '
    f'{abs(c_x3)}x^3 {"-" if c_x4 < 0 else "+"} '
    f'{abs(c_x4)}x^4 {"-" if bias < 0 else "+"} '
    f'{abs(bias)}'
  )
  
  plt.show()


# union
def benchmark_open():
  x_min, x_max = 50000, 500000
  y_min, y_max = 0, 100
  epochs = 10000
  step, runs = 20000, 10

  plt.figure(0)

  def plot(x_vals, y_vals):
    plt.clf()
    plt.title('Benchmarks open_random()')
    plt.xlabel('n')
    plt.ylabel('execution time (ms)')
    plt.axis([x_min, x_max, y_min, y_max])
    plt.plot(x_vals, y_vals, '-')
    plt.pause(0.05)


  perc = None

  def setup(n):
    global perc
    perc = Percolation(math.floor(pow(n + 20, 0.5)))
    for _ in range(n):
      perc.open_random()



  def run_benchmark(n):
    global perc
    for _ in range(400):
      perc.open_random()

  n_vals, times = benchmark(
    func = run_benchmark,
    x_min = x_min,
    x_max = x_max,
    y_min = y_min,
    y_max = y_max,
    setup = setup,
    plot = plot,
    step = step,
    runs = runs
  )

  n_vals, times = normalize(n_vals), normalize(times)

  # 5 inputs:
  # ln(x)
  # x
  # x^2
  # x^3
  # x^4

  output_layer = Dense(1, input_dim=5)
  model = Sequential([
    output_layer
  ])
  model.compile(
    optimizer='adam', 
    loss='mean_squared_error',
  )
  #model.summary()


  x_train = np.array([
    [math.log(x), x, pow(x, 2), pow(x, 3), pow(x, 4)] for x in n_vals
  ], dtype='float')

  model.fit(
    x_train,
    times,
    epochs = epochs,
    batch_size = 256,
    validation_split=0.1,
    verbose=0
  )
  [weights, biases] = output_layer.get_weights()
  model.summary()

  c_ln = weights[0][0]
  c_x = weights[1][0]
  c_x2 = weights[2][0]
  c_x3 = weights[3][0]
  c_x4 = weights[4][0]
  bias = biases[0]
  print(
    f'time = {c_ln}ln(x) {"-" if c_x < 0 else "+"} '
    f'{abs(c_x)}x {"-" if c_x2 < 0 else "+"} '
    f'{abs(c_x2)}x^2 {"-" if c_x3 < 0 else "+"} '
    f'{abs(c_x3)}x^3 {"-" if c_x4 < 0 else "+"} '
    f'{abs(c_x4)}x^4 {"-" if bias < 0 else "+"} '
    f'{abs(bias)}'
  )

  plt.show()

# find
def benchmark_percolates():
  x_min, x_max = 50000, 500000
  y_min, y_max = 0, 10
  epochs = 10000
  step, runs = 20000, 10

  plt.figure(0)

  def plot(x_vals, y_vals):
    plt.clf()
    plt.title('Benchmarks percolates()')
    plt.xlabel('n')
    plt.ylabel('execution time (ms)')
    plt.axis([x_min, x_max, y_min, y_max])
    plt.plot(x_vals, y_vals, '-')
    plt.pause(0.05)


  perc = None

  def setup(n):
    global perc
    perc = Percolation(math.floor(pow(n, 0.5)))
    perc.percolate()



  def run_benchmark(n):
    global perc
    for _ in range(100):
      perc.percolates()

  n_vals, times = benchmark(
    func = run_benchmark,
    x_min = x_min,
    x_max = x_max,
    y_min = y_min,
    y_max = y_max,
    setup = setup,
    plot = plot,
    step = step,
    runs = runs
  )

  n_vals, times = normalize(n_vals), normalize(times)

  # 5 inputs:
  # ln(x)
  # x
  # x^2
  # x^3
  # x^4

  output_layer = Dense(1, input_dim=5)
  model = Sequential([
    output_layer
  ])
  model.compile(
    optimizer='adam', 
    loss='mean_squared_error',
  )
  #model.summary()


  x_train = np.array([
    [math.log(x), x, pow(x, 2), pow(x, 3), pow(x, 4)] for x in n_vals
  ], dtype='float')

  model.fit(
    x_train,
    times,
    epochs = epochs,
    batch_size = 256,
    validation_split=0.1,
    verbose=0
  )
  [weights, biases] = output_layer.get_weights()
  model.summary()

  c_ln = weights[0][0]
  c_x = weights[1][0]
  c_x2 = weights[2][0]
  c_x3 = weights[3][0]
  c_x4 = weights[4][0]
  bias = biases[0]
  print(
    f'time = {c_ln}ln(x) {"-" if c_x < 0 else "+"} '
    f'{abs(c_x)}x {"-" if c_x2 < 0 else "+"} '
    f'{abs(c_x2)}x^2 {"-" if c_x3 < 0 else "+"} '
    f'{abs(c_x3)}x^3 {"-" if c_x4 < 0 else "+"} '
    f'{abs(c_x4)}x^4 {"-" if bias < 0 else "+"} '
    f'{abs(bias)}'
  )

  plt.show()
  