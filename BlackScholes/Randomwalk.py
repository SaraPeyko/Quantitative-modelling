# Randomwalk.py
#
#

import math
import numpy as np
import numpy.random as npr
import scipy
import matplotlib.pyplot as plt

def brownian_motion(dt=0.1, x0=0, N=1000):

	 # W(t=0) = 0
	 # initilize W(t) with zeros
	 W = np.zeros(N+1)

	 # we create N+1 timesteps: t=0,2,3,4,...,N+1
	 t = np.linspace(0, N, N+1)

	 # we have to use cumulative sum: on every step the additional value is
	 # drawn from a normal distribution with mean 0 and variance dt*dt... N(0,dt*dt)
	 W[1:N+1] = np.cumsum(scipy.random.normal(0, dt, N))
	 # if variance dt is so small (dt=0.000001), wiener process will not drift away the zero
	 # if variance dt is big, wiener process is going to have a huge changes

	 return t, W

def plot_brownian_motion(t, W):
	 plt.plot(t, W)
	 plt.xlabel("Time(t)")
	 plt.ylabel("Wiener-process W(t)")
	 plt.title("Wiener-process")
	 plt.show()

if __name__ == "__main__":
	t, W = brownian_motion()
	plot_brownian_motion(t, W)

