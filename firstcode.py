import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
import operator

type_of_eq = input('What is your equation? O or ODE, P or PDE: ')

if type_of_eq == 'O':
	ODE = input('Please type your equation here: ')
	def f(x,y):
		dydt = eval(ODE)
		return dydt
	x = np.linspace(0,4)
	y0 = 0
	y = odeint(f,y0,x)

	plt.plot(x,y)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.show()


	