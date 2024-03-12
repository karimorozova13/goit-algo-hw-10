import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import random

def f(x):
    # return x**2
    return (x - 3) * (x - 5) * (x - 7) + 85
    


a = 0  
b = 2 

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='teal', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='teal', linestyle='--')
ax.axvline(x=b, color='teal', linestyle='--')
ax.set_title('Графік інтегрування f(x) = (x - 3) * (x - 5) * (x - 7) + 85 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Обчислення інтеграла
result, error = spi.quad(f, a, b)
print("Інтеграл: ", result)

def monte_carlo_simulation(f, a,b, n):
    M = 0
    
    for _ in range(n):
       x = random.uniform(a, b)
       y = f(x)
       M += (y * (b - a))
    return M / n


print(monte_carlo_simulation(f, a, b, 10)) 
print(monte_carlo_simulation(f, a, b, 10000000))    
   
