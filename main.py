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

# Начальное распределение температуры
u[0, :] = np.exp(-((x - L/2) ** 2))  # Гауссово распределение

# Численное решение уравнения теплопроводности методом конечных разностей
for n in range(Nt - 1):
    for i in range(1, Nx - 1):
        u[n + 1, i] = u[n, i] + alpha * dt / dx**2 * (u[n, i+1] - 2*u[n, i] + u[n, i-1])

# Визуализация результатов
plt.figure(figsize=(8, 6))
plt.imshow(u, aspect='auto', extent=[0, L, 0, T], cmap='hot', origin='lower')
plt.colorbar(label='Температура')
plt.title('Распределение температуры в стержне')
plt.xlabel('Координата x')
plt.ylabel('Время t')
plt.show()
