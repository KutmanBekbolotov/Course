import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def dumoulin_integral(X0, sigma, T, dt):
    """
    Моделирование интеграла типа Дюмала
    :param X0: начальное значение процесса (начальная цена акций)
    :param sigma: функция волатильности (мера волатильности цены акций)
    :param T: время моделирования
    :param dt: шаг по времени
    :return: массив значений процесса
    """
    num_steps = int(T / dt)
    t = np.linspace(0.0, T, num_steps)
    dW = np.sqrt(dt) * np.random.randn(num_steps)
    X = np.zeros(num_steps)
    X[0] = X0
    for i in range(1, num_steps):
        X[i] = X[i - 1] + sigma(t[i - 1]) * dW[i - 1]
        yield t[:i+1], X[:i+1]

# Пример функции волатильности
def sigma(t):
    return 0.2  # просто константа для примера (вместо этой константы, вы можете использовать измеренную волатильность цен акций)

# Параметры моделирования
X0 = 171.19  # начальное значение процесса (начальная цена акций Apple)
T = 12.0  # время моделирования (в месяцах)
dt = 1/30  # шаг по времени (в месяцах)

# Создание фигуры и осей для графика
fig, ax = plt.subplots()
ax.set_title("Цены акций Apple", fontsize=18, fontweight='bold', color='black')
ax.set_xlabel("Время (месяцы)", fontsize=14, fontweight='bold', color='black')
ax.set_ylabel("Цена акций (USD)", fontsize=14, fontweight='bold', color='black')
ax.grid(True)

# Пустой график
line, = ax.plot([], [], lw=2)

# Создание и размещение ползунка
ax_time = plt.axes([0.1, 0.01, 0.8, 0.03], facecolor='lightgoldenrodyellow')
slider_time = Slider(ax_time, 'Отрезок времени (месяцы)', 0.1, T, valinit=T)

# Функция для обновления графика при изменении положения ползунка
def update(val):
    t_value = slider_time.val
    for t, X in dumoulin_integral(X0, sigma, t_value, dt):
        line.set_data(t, X)
        ax.relim()
        ax.autoscale_view()
        plt.draw()

slider_time.on_changed(update)  # Подключение обработчика событий для ползунка

plt.show()
