num_1 = int(input('Введіть перше число: '))
num_2 = int(input('Введіть друге число: '))

print('\n1. Додавання - "+"\n2. Віднімання - "-"\n3. Множення - "*"\n4. Ділення - "/"')

chooseOperation = str(input('\nВиберіть операцію: '))

if chooseOperation == "+":
    output = num_1 + num_2

elif chooseOperation == "-":
    output = num_1 - num_2

elif chooseOperation == "*":
    output = num_1 * num_2

elif chooseOperation == "/":
    output = num_1 / num_2

else:
    print('\nВи ввели невірну операцію!\n')

print(f'Результат: {output}')    

