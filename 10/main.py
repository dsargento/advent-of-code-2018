import parser
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
import time

my_parser = parser.Parser("./input.txt")
plt.show()
plt.ion()
fig = plt.figure()
iteration = 10850
for i in range(iteration):
    my_parser.update_list()

while 1:
    plt.clf()
    x = my_parser.x_list
    y = my_parser.y_list
    plt.scatter(x, y)

    fig.canvas.draw()
    fig.canvas.flush_events()

    input("Press Enter to continue...")
    my_parser.update_list()
    iteration += 1
    print(iteration)
