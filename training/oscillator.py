import numpy as np
import matplotlib.pyplot as plt
from solver import solver #можем использовать функции из solver-а

def fx(x,y):
    return -x

def fy(x,y):
    return 0

x, _, px, _ = solver(0,0,1,0,0.001,0,1000,fx,fy)

plt.figure()
plt.grid()
plt.plot(x, px, alpha=0.3)  #alpha=прозрачность
plt.xlabel(r'$x$')
plt.ylabel(r'$p_{x}$')
plt.show()

#стенки эллипса=фазового объема едут при большом кол-ве шагов, т.е. фазовый объем не сохраняется (схема Эйлера)

#Теперь схема Верле:

def solver_Verlet(
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
