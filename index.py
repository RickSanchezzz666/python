import time
import random


def delayPrint(text):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(random.random() * 0.06)
    print()

eventsList = [(1957, 'Перший штучний супутник Землі, Спутник-1, був запущений радянськими вченими.'), (1961, 'Юрій Гагарін став першою людиною, яка здійснила орбітальний політ на космічному кораблі "Восток-1".'),
              (1969, 'Астронавти NASA Ніл Армстронг і Едвін Олдрін стали першими людьми, які висадилися на Місяці під час місії "Аполлон-11".'), (1971, 'Радянська місія "Союз-10" спробувала висадити астронавтів на Місяці, але зіткнулася з проблемами та повернулася на Землю без висадки.'),
              (1972, 'Американська місія "Аполлон-17" була останньою місією проекту "Аполлон" та першою та останньою місією з висадкою на Місяці в 20-му столітті.'),
              (1981, 'Перший політ космічного шаттла "Колумбія" відкрив нову еру пілотованих космічних політів.'), (1986, 'Катастрофа шатла "Челленджер" призвела до загибелі сімох астронавтів під час старту.'),
              (1998, 'Почалася міжнародна космічна станція (МКС), яка стала спільним проектом багатьох країн.'), (2011, 'По завершенню 30-річної служби, космічний шаттл "Атлантис" завершив останню місію програми "Космічний шатл".'),
              (2020, 'SpaceX запустила перший пілотований польот Crew Dragon до МКС, відновивши пілотовані космічні польоти зі Сполучених Штатів.')]

dictionaryOfEvents = dict()

def addToDictionary(year, event):
    dictionaryOfEvents[f'{year}'] = event

for i in range(len(eventsList)):
    addToDictionary(eventsList[i][0], eventsList[i][1])

def showDictionary():
    print(dictionaryOfEvents)

def deleteFromDictionary(year):
    dictionaryOfEvents.pop(f'{year}')

yearsToVisit = [1972, 1981, 1986, 2012, 2020, 2023]

def timeMachine():
    delayPrint('Зараз ви відправитесь у подорож у часі у роки, які ви вказали у вашій анкеті!')
    time.sleep(1)
    delayPrint('*Beep Beep*')
    time.sleep(1)
    delayPrint('*Bop Bop*')
    time.sleep(1)
    delayPrint('*burp*')
    time.sleep(1)
    for i in range(len(yearsToVisit)):
        try:
            dictionaryOfEvents[f'{yearsToVisit[i]}']
            delayPrint(f'{i + 1}. У році {yearsToVisit[i]} була така подія:')
            delayPrint(dictionaryOfEvents[f'{yearsToVisit[i]}'])
        except:
            delayPrint(f'{i + 1}. Такого року [{yearsToVisit[i]}] не знайдено у словнику часу!!')
            time.sleep(1)
            delayPrint('Перевірка статусу машини часу...')
            time.sleep(1)
            delayPrint('Статус стабільний, продовжуємо роботу!')
            pass

while True:
    print('\nВиберіть варіант:\n1. Додати подію до словнику\n2. Видалити подію зі словнику\n3. Показати словник\n4. Додати дату до подорожі\n5. Видалити дату до подорожі\n6. Відправитись у подорож!\n7. Завершити програму')
    choice = input('Введіть вашу відповідь: ')
    match choice:
        case '1':
            while True:
                year = input('Введіть рік який хочете додати: ')
                if(dictionaryOfEvents.get(year) is not None):
                    pass
                else:
                    event = input('Опишіть подію як тоді сталась: ')
                    addToDictionary(year, event)
                    break
        case '2':
            while True:
                year = input('Введіть рік події яку хочете видалити: ')
                if(dictionaryOfEvents.get(year) is not None):
                    deleteFromDictionary(year)
                    break
                else:
                    print('Такий рік не знайдено!')
                    break
        case '3':
            showDictionary()
        case '4':
            year = input('Введіть рік який хочете додати: ')
            yearsToVisit.append(year)
        case '5':
            year = input('Введіть рік який хочете видалити: ')
            try:
                yearsToVisit.remove(year)
            except ValueError:
                print('\nТакої дати немає у списку!')
        case '6':
            timeMachine()
        case '7':
            delayPrint('Завершую програму...')
            time.sleep(1)
            break