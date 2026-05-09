a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
с = input("Введіть дію: ")

if с == "+":
    print("Результат:", a + b)
elif с == "-":
    print("Результат:", a - b)
elif с == "*":
    print("Результат:", a * b)
elif с == "/":
    if b == 0:
        print("Ділення на нуль")
    else:
        print("Результат:", a / b)
else:
    print("Невідома дія")
