import matplotlib.pyplot as plt
import numpy as np

#Starting at Fanshawe college, you want to get to Toronto to watch a concert. Toronto is roughly
#200km away. You start your drive with your friend Slow McTurtle. They drive 60km/h for the
# first 45 minutes. For the remainder of the trip, you beg for your other friend Fast McRabbit to
# take the wheel. The group agrees and McRabbit drives 120km/h the remainder of the way to
# get to the concert on time.
# Create a python script that plots distance (y) vs time(x) for both the slow and the fast portion of
# the trip (separately). With a little research, do you think you can merge the two graphs
# together?
#s * t = d
#
# def straight_line(x): # definition of a straight line using a function
#     y = 2 * x - 1
#     return y # do not forget to return the y value
# x = np.linspace(-10,10,11) # 11 points equally spaced between -10 and 10
# y = straight_line(x) # generate the y values
# # inspect the data
# print(x)
# print(y)
# # plot x against y
# # indicate the color / type of line / type of marking and provide a label
# plt.plot(x, y, '-or', label='y=2x-1')
# # create a title for the graph
# plt.title('Graph of y=2x-1')
# # x label and y label
# plt.xlabel('x')
# plt.ylabel('y')
# # legend
# plt.legend(loc='upper left')
# # create the grid
# plt.grid()
# # show the p

import numpy as np
x = np.linspace(-5,5,100)
print(x)
