import matplotlib.pyplot as plt
import numpy as np

# a = (1,2,3,4,5)

# # for i in a:
# #     print(i)

# for i in range(len(a)):
#     a[i] = a[i]**2

# print(a)


# def func(a: list, k: int) -> list: 
#     b = []
#     for i in a:
#         b.append(i**k) 
#     return b

# print(func([1,2,3], 3))


def trigonometry(x: np.ndarray) -> np.ndarray:
    return np.sin(x)**2 + np.cos(x)**2

figure = plt.figure(dpi=300)
x = np.linspace(0, np.pi, 1000)
plt.grid()
plt.xlabel('x')
plt.ylabel(r'$sin(x)^{2} + cos(x)^{2}$')
plt.plot(x, trigonometry(x))
plt.show()