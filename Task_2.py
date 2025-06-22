import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Функція для інтегрування
def f(x):
    return x**2

# Межі інтегрування
a, b = 0, 2
N = 100000  # Кількість випадкових точок

# Монте-Карло інтегрування
x_rand = np.random.uniform(a, b, N)
y_rand = f(x_rand)
monte_carlo_result = (b - a) * np.mean(y_rand)

# Аналітичне обчислення з scipy
quad_result, quad_error = quad(f, a, b)

# Результати
print(f"Результат методом Монте-Карло: {monte_carlo_result}")
print(f"Аналітичний результат (quad): {quad_result}")
print(f"Абсолютна похибка: {abs(monte_carlo_result - quad_result)}")

# Візуалізація
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
plt.plot(x, y, 'r', linewidth=2)
plt.fill_between(np.linspace(a, b), f(np.linspace(a, b)), color='gray', alpha=0.3)
plt.axvline(x=a, color='gray', linestyle='--')
plt.axvline(x=b, color='gray', linestyle='--')
plt.title(f"f(x) = x^2 на [{a}, {b}]")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()
