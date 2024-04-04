import numpy as np
import matplotlib.pyplot as plt

# Определение параметров
L = 1.0  # Длина стержня
T = 1.0  # Время моделирования
alpha = 0.01  # Коэффициент теплопроводности

# Определение параметров сетки
Nx = 100  # Количество узлов по координате x
Nt = 1000  # Количество временных шагов
dx = L / (Nx - 1)  # Шаг по координате x
dt = T / Nt  # Шаг по времени

# Инициализация сетки
x = np.linspace(0, L, Nx)  # Сетка по координате x
u = np.zeros((Nt, Nx))  # Массив для хранения решения

# Начальное распределение температуры (базовая функция)
def base_function(x, t):
    return np.exp(-x**2 / (4*alpha*t)) / np.sqrt(4*np.pi*alpha*t)

# Неоднородность (начальное распределение температуры)
def nonhomogeneity(x):
    return np.sin(np.pi * x / L)

# Решение методом Дюамеля
for n in range(Nt):
    t = (n + 1) * dt  # Текущее время
    for i in range(Nx):
        for j in range(Nx):
            u[n, i] += base_function(x[i] - x[j], t) * nonhomogeneity(x[j]) * dx

# Визуализация результатов
plt.figure(figsize=(8, 6))
plt.imshow(u, aspect='auto', extent=[0, L, 0, T], cmap='hot', origin='lower')
plt.colorbar(label='Температура')
plt.title('Распределение температуры в стержне (метод Дюамеля)')
plt.xlabel('Координата x')
plt.ylabel('Время t')
plt.show()
