from pulp import LpMaximize, LpProblem, LpVariable

# Створення моделі
model = LpProblem(name="maximize-drinks", sense=LpMaximize)

# Змінні: кількість виробленого лимонаду (x) та фруктового соку (y)
x = LpVariable(name="lemonade", lowBound=0, cat="Integer")
y = LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

# Цільова функція: максимізувати загальну кількість напоїв
model += x + y, "Total_Products"

# Обмеження на ресурси
model += 2 * x + 1 * y <= 100, "Water_limit"
model += 1 * x <= 50, "Sugar_limit"
model += 1 * x <= 30, "Lemon_juice_limit"
model += 2 * y <= 40, "Fruit_puree_limit"

# Розв’язання
model.solve()

# Результати
print(f"Кількість лимонаду: {x.value()}")
print(f"Кількість фруктового соку: {y.value()}")
print(f"Максимальна кількість напоїв: {model.objective.value()}")
