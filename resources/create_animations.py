import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

import matplotlib.animation as anim

# Anzahl der Knoten (Diskretisierung)
resolution = 200

# T and T+ Vektoren erstellen und mit Startwert 0 °C initialisieren
dTdt = np.zeros(resolution)
T = np.zeros(resolution)

# Simulations-Zeit
sim_time = 500
dt = 1

#Geometrie und thermische Parameter
L = 0.1  # m
dx = L / resolution  #
lambda_mat = 50 # W/(mK)
rho = 7850 # kg/m³
c = 500 # J/(kgK)
alpha = lambda_mat / (rho * c)
# alpha = 1e-7

# RB
T[0] = 10
T[-1] = 10


# Function to solve
# ----------------------------------------------
def dTdt_calc(t, T):

    dTdt[1:-1] =alpha * (T[2:] - 2 * T[1:-1] + T[:-2]) / dx**2

    dTdt[0] = 0
    dTdt[-1] = 0

    return dTdt


# %%
# Initial conditions and time scheme for solver
T0 = T[:]

t0 = 0  # Start time in hours
tf = sim_time  # End time in hours

t_eval = np.linspace(t0, tf, 100)

# ----------------------
#       Solve
# ---------------------

print('Solving the differential equation...')
sol = solve_ivp(dTdt_calc, (t0, tf), T0, t_eval=t_eval, dense_output=False, atol=1e-7, rtol=1e-5)

# print('Anzahl rechte Seite', sol.nfev)

# Input the solution as the new moisture saturation
T[:] = sol.y[:, sol.y.shape[1] - 1]

# plotting
x_pos = np.arange(0, L, dx)
plt.xlabel("x position [m]")
plt.ylabel("Temperature [°C]")
plt.grid()
plt.plot(x_pos, T)
# plt.savefig('T.png')
plt.show()

# ---------------------
# Plotting gif
# ---------------------

# x-Axis for animation needs array
x_fig = np.linspace(dx, L, num=resolution - 2)

anim_time = 8

font = {'size': 14}
# matplotlib.rc('font', **font)

fig, axes = plt.subplots(nrows=1)

fps = 20
total_frames = sol.y.shape[1]
frame_freq = int(total_frames / (fps * anim_time)) + 1
display_frames = [i * frame_freq for i in range(fps*anim_time) if i*frame_freq < sol.y.shape[1]]
display_frames.append(sol.y.shape[1]-1)

# setup figures (axes objects)
axes.grid()
axes.axis([0, 1.1 * L, 0, 1.1 * T[-1]])
axes.set_xlabel('Discretized specimen in $m$')
axes.set_ylabel('Temperature in °C')

# initial states
line1, = axes.plot(x_fig, sol.y[1:-1, 0])

# animation function
def my_animation(i):
    line1.set_ydata(sol.y[1:-1, i])

# create animation
ani = anim.FuncAnimation(fig, my_animation, frames=display_frames, interval=int(1000/fps))

# save to file
if True:
    writergif = anim.PillowWriter(fps=fps)
    ani.save('./img/T_both_sides.gif', writer=writergif)

plt.close()
