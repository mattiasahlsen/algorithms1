import time

def benchmark(
  func,
  x_min,
  x_max,
  y_min,
  y_max,
  plot = None,
  setup = None,
  step = 1,
  runs = 1
):
  times = []

  if func is None: raise 'func function must be defined'
  # if plot is None: raise 'plot function must be defined'
  if x_min is None: raise 'x_min must be defined'
  if x_max is None: raise 'x_max must be defined'
  if y_min is None: raise 'y_min must be defined'
  if y_max is None: raise 'y_max must be defined'


  x_vals = range(x_min, x_max, step)
  for i in range(len(x_vals)):
    if setup: setup(x_vals[i])

    total_time = 0
    for _ in range(runs):
      start_time = time.process_time_ns()
      func(x_vals[i])
      end_time = time.process_time_ns()
      total_time += (end_time - start_time)

    average_time = total_time / runs
    times.append(average_time / pow(10, 6))

    if plot:
      plot(x_vals[:i + 1], times)

  return x_vals, times
