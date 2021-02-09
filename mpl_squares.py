import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]    # Значения по оси х
squares = [1, 4, 9, 16, 25]    # Значения по оси у
plt.style.use("seaborn")    # Выбор стиля оформления (чтобы узнать, какие доступны plt.style.available)
fig, ax = plt.subplots()    # Генерирует диаграмму
ax.plot(input_values, squares, linewidth=3)   # Задает толщину линии

# Назначение заголовка диаграммы и меток осей.
ax.set_title("Square Numbers", fontsize=24)    # Задает заголовок диаграммы
ax.set_xlabel("Value", fontsize=14)    # Заголовок оси х
ax.set_ylabel("Square of Value", fontsize=14)    # Заголовок оси у

# Назначение размера шрифта делений на осях.
ax.tick_params(axis="both", labelsize=14)

plt.show()
