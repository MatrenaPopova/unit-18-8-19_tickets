price = 0
tickets = (int(input("Введите количество билетов: ")))
for age in range (tickets):
    age = (int(input("Введите возраст: ")))
    if age < 18:
        price = (price + 0)
    elif 18 <= age <= 25:
        price = (price + 990)
    elif age > 25:
        price = (price + 1390)
if tickets > 3:
    discount = price / 100 * 10
    price = price - discount

print("Стоимость билетов:", price, "руб.")

