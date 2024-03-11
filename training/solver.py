import matplotlib.pyplot as plt
import numpy as np


def solver(
    x0: float,
    y0: float,
    vx0: float,
    vy0: float,
    dt: float,
    t_start: float,
    t_end: float,
    fx,
    fy,
    m: float = 1,
) -> list:
    N = int((t_end - t_start)//dt) #два слеша при делении отбрасывают дробную часть числа, т.к. далее применяем range()
    x = [x0]
    y = [y0]
    vx = [vx0]
    vy = [vy0]
    for i in range(N):
        vx.append(vx[i] + dt*fx(x[i], y[i])/m)
        vy.append(vy[i] + dt*fy(x[i], y[i])/m)
        x.append(x[i] + vx[i]*dt)
        y.append(y[i] + vy[i]*dt)


    return x,y

def fx(x,y):
    return x/(x**2 + y**2)**(3/2)

def fy(x,y):
    return y/(x**2 + y**2)**(3/2)


system = []
n = 10

for i in range(n):
    phi = np.random.uniform(-np.pi/15, np.pi/15)
    v_amp = 3
    system.append(
        solver(-1, 0, v_amp*np.cos(phi), v_amp*np.sin(phi), 0.001, 0, 1, fx, fy)
    )


figure = plt.figure()
plt.grid()
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
for i in range(n):
    plt.plot(system[i][0], system[i][1])
plt.scatter(0,0,c='red')
plt.scatter(-1,0)
plt.show()
