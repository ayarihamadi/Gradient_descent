from matplotlib import pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

alpha = 0.001


def animation(points_x, points_y, title):
    it = len(points_x)
    # Scatter plot
    fig = plt.figure(figsize=(5, 5))
    axes = plt.axes(xlim=(-1, 3),
                    ylim=(-8, 4))
    plt.title(title)
    axes.text(2, 3, 'Iteration: ' + str(it))

    # initializing a line variable
    line, = axes.plot([], [], lw=3, color='b')
    point, = axes.plot([points_x[0]], [points_y[0]], 'go', color='y')

    # data which the line will
    # contain (x, y)
    def init():
        line.set_data([], [])
        return line,

    def ani(coords):
        x = np.linspace(-1, 3, 1000)
        # plots a sine graph
        y = 0.99 * x**5 - 5 * x**4 + 4.98 * x**3 + 5 * x**2 - 6 * x - 1
        line.set_data(x, y)
        point.set_data([coords[0]], [coords[1]])
        return line, point

    def frames():
        for pos_x, pos_y in zip(points_x, points_y):
            yield pos_x, pos_y

    ani = FuncAnimation(fig, ani, frames=frames, interval=1000)

    plt.show()


def f(x):
    return 0.99 * x**5 - 5 * x**4 + 4.98 * x**3 + 5 * x**2 - 6 * x - 1


def f_derivative(x):
    return 4.95 * x **4 - 20 * x ** 3 + 14.94 * x**2 + 10 * x - 6


def global_min():
    global_min_x = list()
    global_min_y = list()
    for cur_x in [0, 1, 2]:
        precision = 0.000001  # This tells us when to stop the algorithm
        previous_step_size = 1  #
        max_iters = 100  # maximum number of iterations
        iters = 0  # iteration counter
        points_x = list()
        points_y = list()
        y = f(cur_x)
        points_x.append(cur_x)
        points_y.append(y)
        while previous_step_size > precision and iters < max_iters:
            prev_x = cur_x
            f_der = f_derivative(prev_x)
            cur_x = prev_x - alpha * f_der
            previous_step_size = abs(cur_x - prev_x)  # Change in x
            iters = iters + 1  # iteration count
            if iters % 5 == 0:
                x = cur_x
                y = f(x)
                points_x.append(x)
                points_y.append(y)

        if global_min_x == [] or min(points_y) < min(global_min_y):
            global_min_x = points_x
            global_min_y = points_y
    return global_min_x, global_min_y


def global_max():
    global_max_x = list()
    global_max_y = list()
    for cur_x in [0, 1, 2]:
        precision = 0.000001  # This tells us when to stop the algorithm
        previous_step_size = 1  #
        max_iters = 100  # maximum number of iterations
        iters = 0  # iteration counter
        points_x = list()
        points_y = list()
        y = f(cur_x)
        points_x.append(cur_x)
        points_y.append(y)
        while previous_step_size > precision and iters < max_iters:
            prev_x = cur_x
            f_der = f_derivative(prev_x)
            cur_x = prev_x + alpha * f_der
            previous_step_size = abs(cur_x - prev_x)  # Change in x
            iters = iters + 1  # iteration count
            if iters % 5 == 0:
                x = cur_x
                y = f(x)
                points_x.append(x)
                points_y.append(y)

        if global_max_x == [] or max(points_y) > max(global_max_y):
            global_max_x = points_x
            global_max_y = points_y
    return global_max_x, global_max_y


def main():
    global_min_x, global_min_y = global_min()
    minimum_y = min(global_min_y)
    idx = global_min_y.index(minimum_y)
    minimum_x = global_min_x[idx]
    animation(global_min_x, global_min_y, f'GLOBAL MINIMUM : {round(minimum_x, 2), round(minimum_y,2)}')

    global_max_x, global_max_y = global_max()
    maximum_y = max(global_max_y)
    idx = global_max_y.index(maximum_y)
    maximum_x = global_max_x[idx]
    animation(global_max_x, global_max_y, f'GLOBAL MAXIMUM : {round(maximum_x, 2), round(maximum_y,2)}')


if __name__ == "__main__":
    main()




