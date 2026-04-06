import numpy as np
import matplotlib.pyplot as plt

TOTAL_DOTS = 1000
rng = np.random.default_rng(seed=1700)
dots_x = rng.random(size=TOTAL_DOTS)
dots_y = rng.random(size=TOTAL_DOTS)
dots_x_in = []
dots_y_in = []
amount_in_circle = 0
amount_out_circle = 0

figure, axes = plt.subplots()

def in_circle(x, y):
    if np.sqrt(np.add(np.square(np.subtract(x, 0.5)), np.square(np.subtract(y, 0.5)))) <= 0.5:
        dots_x_in.append(x)
        dots_y_in.append(y)
        return 1
    return 0

def find_distance(dots_x, dots_y):
    vfunc = np.vectorize(in_circle)
    result = vfunc(dots_x, dots_y)
    return result


more_dots = find_distance(dots_x, dots_y)



amount_in_circle = np.sum(more_dots)
print(amount_in_circle)
print(np.multiply(np.divide(amount_in_circle, TOTAL_DOTS), 4))
plt.scatter(dots_x, dots_y, color = 'b')
plt.scatter(dots_x_in, dots_y_in, color = 'r')
axes.set_aspect(1)
axes.add_artist(plt.Circle((0.5, 0.5), 0.5, fill = False))
plt.show()