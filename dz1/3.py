import random

number = random.randint(1, 10)

attempts = 3

print("Гра 'Вгадай число'")
print("Я загадав число від 1 до 10.")
print(f"У вас є 3 спроби.")

for i in range(attempts):
    guess = int(input("Введіть ваше число: "))

    if guess == number:
        print("Ви вгадали число!")
        break
    elif guess > number:
        print("Менше")
    else:
        print("Більше")

    print(f"Залишилось спроб: {attempts - i - 1}")

else:
    print(f"Ви програли. Загадане число було: {number}")