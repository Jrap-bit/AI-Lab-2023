import matplotlib.pyplot as plt
import numpy as np


def line_eq(point1, point2):
    (x1, y1), (x2, y2) = point1, point2
    if x2 - x1 == 0:
        return None, None
    slope = (y2 - y1) / (x2 - x1)
    intercept = y1 - slope * x1
    return slope, intercept


def Cold_membership():
    def mf(temp):
        if temp <= 20:
            return 1
        elif temp >= 30:
            return 0
        else:
            slope, intercept = line_eq((20, 1), (30, 0))
            return slope * temp + intercept

    return mf


def Hot_membership():
    def mf(temp):
        if temp <= 20:
            return 0
        elif temp >= 30:
            return 1
        else:
            slope, intercept = line_eq((20, 0), (30, 1))
            return slope * temp + intercept

    return mf


if __name__ == "__main__":
    cold = Cold_membership()
    hot = Hot_membership()
    x = np.linspace(0, 30, 1000)
    y_cool = [cold(t) for t in x]
    y_hot = [hot(t) for t in x]
    y_union = np.maximum(y_cool, y_hot)
    y_intersection = np.minimum(y_cool, y_hot)
    y_complement = [1 - y for y in y_cool]

    plt.plot(x, y_cool, label="Cold")
    plt.plot(x, y_hot, label="Hot")
    plt.legend()
    plt.show()

    plt.plot(x, y_union, label='Union')
    plt.plot(x, y_intersection, label='Intersection')
    plt.plot(x, y_complement, label='Complement of "Cool"')

    plt.xlabel('Temperature (°C)')
    plt.ylabel('Membership degree')
    plt.legend()
    plt.show()
