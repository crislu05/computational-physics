import matplotlib.pyplot as plt 
import numpy as np 
from geometric_series import geometric_series

#task2: step through a range of values and plot the value of the solution, the relative error and the number of iterations needed 


#solution 1: implemented by hand 
values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
result = [geometric_series(val) for val in values]

sol = [result[_][0] for _ in range(len(result))]
err = [result[_][1] for _ in range(len(result))]
steps = [result[_][2] for _ in range(len(result))]

print(result)

fig, (ax1,ax2,ax3) = plt.subplots(1,3, figsize=(12,6)) #three axis side by side 

ax1.plot(values, sol)
ax2.plot(values, err)
ax3.plot(values, steps)
plt.show()


#solution 2: provided by claude 
values = np.linspace(0.1,0.9,9)
results = [geometric_series(g) for g in values]

sol, err, steps = map(np.array, zip(*result)) # this is three steps, *result unpacks the list, zip() groups the elements, np.map(np.array) turns tuple into array 

fig, axes = plt.subplots(1,3, figsize = (12,6))
axes[0].plot(values, sol, 'o-') #circle marker joined by a solid line 
axes[0].plot(values, 1/(1 + values), 'k--', lw = 0.8, label = 'exact') #black dashed line 
axes[0].legend() #draws the label box 


axes[1].semilogy(values, err, 'o-') #y scale is in log 


axes[2].plot(values, steps, 'o-')
axes[2].set_ylabel("iterations")

for ax in axes:
    ax.grid(alpha = 0.3) #transparency of grid

fig.tight_layout() #nothing overlaps or clipped 
fig.savefig("convergence.png", dpi = 300)