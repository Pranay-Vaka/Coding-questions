import math
import matplotlib.pyplot as plot
import numpy as np

# All trigonometric values are in radians

def function(i_0: float, t_0: float, t: float) -> float: # This holds the function that will be used plot the graph 
    return R * ((i_0 * math.e ** (-t / t_0)) * (math.sin((2 * t) / t_0))) ** 2


# This holds the values that are points on the graph, which can then be plotted
x_points = []
y_points = []


h = 0.0001 # This is the step between the x values on the graph
R = 0.5
t_0 = 0.01


for i in np.arange(0, 1, h): # Between 0 and 1
    x_points.append(i)
    y_points.append(function(100, t_0, i))

def area(h: float, y_values) -> float: # Returns the area under the graph using the trapezium rule 
    return h * ((y_points[0] + y_points[-1]) + 2 * (sum(y_points[1:-1])))


plot.plot(x_points, y_points)

plot.title("Time against Current")
plot.xlabel("Time(s)")
plot.ylabel("Current(A)")

plot.show()

E = R * area(h, y_points)

print(E)

"""
The Value for energy that was caluculated was 9.999999966665593J which can be safely
rounded up to 10J
"""
