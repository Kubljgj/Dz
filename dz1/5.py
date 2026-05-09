number = int(input("Введіть число: "))

for i in range(number, 0, -1):
    if i % 2 == 0:
        print(i, end=" ")