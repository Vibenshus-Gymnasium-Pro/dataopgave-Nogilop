import numpy as np
import matplotlib.pyplot as plt

TOTAL_DOTS = 100000
rng = np.random.default_rng(seed=1700)
dots_x = rng.random(size=TOTAL_DOTS)
dots_y = rng.random(size=TOTAL_DOTS)
in_x = []
in_y = []
in_circle = 0

figure, axes = plt.subplots()

def in_circle(x, y):
    if np.sqrt(np.add(np.square(np.subtract(x, 0.5)), np.square(np.subtract(y, 0.5)))) <= 0.5:
        in_x.append(x)
        in_y.append(y)
        return 1
    return 0

def find_distance(dots_x, dots_y):
    vfunc = np.vectorize(in_circle)
    result = vfunc(dots_x, dots_y)
    return result

more_dots = find_distance(dots_x, dots_y)
in_circle = np.sum(more_dots)
print(f"Pi: {np.multiply(np.divide(in_circle, TOTAL_DOTS), 4)}")
plt.scatter(dots_x, dots_y, color = 'b')
plt.scatter(in_x, in_y, color = 'r')
axes.set_aspect(1)
axes.add_artist(plt.Circle((0.5, 0.5), 0.5, fill = False))
plt.show()