import doctest
import numpy as np
import matplotlib.pyplot as plt

def true_function(x):
    """
    引数として受けた数値を計算し、
    真の関数として y = sin(pi * x * 0.8)の結果を返す。

    UnitTesting
    -------
    >>> true_function(0)
    0.0
    """
    y = np.sin(np.pi * x * 0.8)
    return y

x = np.array([-1,1])
plt.plot(x,true_function(x), label = "y = sin(pi * x * 0.8)")
plt.legend()
plt.show()
fig = plt.figure()
fig.savefig("ex1.1.png")

if __name__ == '__main__':
    doctest.testmod()