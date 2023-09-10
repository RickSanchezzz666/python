def arithmeticOperations(num1, num2):
    print(
        '\n1. Додавання - "+"\n2. Віднімання - "-"\n3. Множення - "*"\n4. Ділення - "/"'
    )
    chooseOperation = str(input("\nВиберіть операцію: "))

    if chooseOperation == "+":
        output = num1 + num2

    elif chooseOperation == "-":
        output = num1 - num2

    elif chooseOperation == "*":
        output = num1 * num2

    elif chooseOperation == "/":
        output = num1 / num2

    else:
        print("\nВи ввели невірну операцію!\n")

    print(f"Результат: {output}")


def compareNumbers(num1, num2):
    if num1 == num2:
        print('\nЧисла рівні!\n')
    elif num1 > num2:
        print(f'\nЧисло {num1} більше за число {num2}\n')
    elif num1 < num2:
        print(f'\nЧисло {num1} менше за число {num2}\n')
    else:
        print('\nПомилка!\n')

def changetype(num1, num2):
    print(
        '\n1. Integer - "1"\n2. Float - "2"'
    )
    chooseOperation = int(input("\nВиберіть на який тип змінити: "))

    if chooseOperation == 1:
        newNum1 = int(num1)
        newNum2 = int(num2)
    elif chooseOperation == 2:
        newNum1 = float(num1)
        newNum2 = float(num2)
    else:
        print('\nТакої операції не існує!\n')

    print(f"Результат: оновлене число 1: {newNum1}, оновлене число 2: {newNum2}")
def evenOdd(num1, num2):
    if num1 % 2 == 0:
        print(f'Число {num1} парне!')
    else:
        print(f'Число {num1} непарне!')

    if num2 % 2 == 0:
        print(f'Число {num2} парне!')
    else:
        print(f'Число {num2} непарне!')

num_1 = float(input("Введіть перше число: "))
num_2 = float(input("Введіть друге число: "))

print('\nОперації:\n1. Арифметичні операції - "1"\n2. Порівняти числа - "2"\n3. Перетворити на інший тип даних - "3"\n4. Перевірити на парність - "4"')

chooseOperation = int(input('\nВиберіть операцію: '))

if chooseOperation == 1:
    arithmeticOperations(num_1, num_2)
elif chooseOperation == 2:
    compareNumbers(num_1, num_2)
elif chooseOperation == 3:
    changetype(num_1, num_2)
elif chooseOperation == 4:
    evenOdd(num_1, num_2)
else:
    print('\nТакої операції не існує!\n')
