import time
import random

def delay_print(text):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(random.random() * 0.06)
    print()

def delay_print_choice(text):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(random.random() * 0.06)
    return ''

name = input(delay_print_choice("Введіть ваше ім'я: "))

end = [
    [f"Вітання, {name}! Після смерті Священника ви стали Богом!\nP.S. Great option!", "Ви померли(", f"Вітання, {name}! Ви далі алкаш але щасливий до кінця дня!"],
    [f"Вітання, {name}, вам уже нічого не допоможе!", f"Вітання, {name}! Ви у Раю, не дякуйте!", f"Вітання, {name}! Ви живий  і з Жигульом ^_^\nP.S. Best option!"]
    ]

delay_print('Вітаю, ' + name + '! Зараз почнеться сама екшонова історія яку ти бачив у своєму житті. Кінцівки та розвиток сюжету залежать повністю від тебе! Удачі!')

delay_print("\nУ великому місті, де вулиці блищали яскравими неоновими рекламами та сяяли вогнями нічних клубів.\nВи прокидаєтеся у розхарканому гаражі. Ваш персонаж - це колишній успішний бармен, який втратив все через свою алкогольну залежність.\nВи розумієте, що вам потрібно щось змінити у своєму житті, і ви вирішуєте вийти на вулицю і почати свій шлях до зміни.")

delay_print("\nУ вас є два варіанти: \n1. Спокутати всі гріхи та знайти новий шлях\n2. Продовжите своє спіралеподібне занурення в алкогольну безодню")

input_answer = input(delay_print_choice('\nВведіть свою відповідь: '))

question_index = 0

answers_array = []

def answer_1(ans):
    match ans:
        case '1':
            delay_print('\nВи вибрали викупити своє минуле і знайти новий шлях.')
        case '2':
            delay_print('\nВи віришили продовжите своє занурення в алкогольну безодню.')
        case _:
            while ans not in ["1", "2"]:
                delay_print('\nВажко було попасти по 1 чи 2? ~_~')
                ans = input(delay_print_choice('\nСпробуй ще раз: '))
            answer_1(ans)
    return ans

answer = answer_1(input_answer)

answers_array.append(answer)

previous_answer = answers_array[question_index]

question_index += 1

match previous_answer:
    case '1':
        delay_print('\nВи взяли тряпочку яка висіла поряд та протерли очі.\nУ вас будун але ви вирішили покінчити з цим та звернутись за допомогою.')
        delay_print("\nВийшовши на вулиці ви бачите трьох людей: \n1. Батюшка Володя з запахом дешевих духів та торчащою фляжкою з горілкою з його карману.\n2. Баба Вєра, яку ви уже заєбали так, що вона вам бажає тільки смерті.\n3. Толік, ваш дружбан, якому від вас тількі потрібні розмови про те, як у '94 було піздато і ви держали весь район.")

        input_answer = input(delay_print_choice('\nВведіть свою відповідь: '))
    case '2':
        delay_print('\nВи протерли свої очні яблука грязкими руками та занесли ще одну інфекцію(Яких і так вистачає)\nУ вас будун і вам потрібно купити ще горілки але на руках у вас тількі полтос (50 грн)')
        delay_print('\nЯк ви поступите: \n1. Спіздите бутилку в супермаркеті. \n2. Попросите "мєлочі" в прохожих. \n3. Змиритесь та купите бутилку Жигулівського.')

        input_answer = input(delay_print_choice('\nВведіть свою відповідь: '))
    case _:
        print('\n-\n--\n---\nbrav how da FUC-\n---\n--\n-\n')

def answer_2(ans):
    match previous_answer:
        case '1':
            match ans:
                case '1':
                    delay_print('\nВи підійшли і спитали у Володі чи можна якось спокутати ваші гріхи у церкві.')
                    delay_print('\n-Бля, Вов. Я незнаю вже шо робити, жінка пішла і просе аліменти. А в мене в кармані хуй з повидлом...\n\n-Ааа... Ти хто вобще такій? -_-')
                    delay_print('\n-' + name + "..")
                    delay_print('\n-Саньок, піздуй отсюда. У мене своїх проблем по горло.\n\n*Батюшка дістав флягу та почав пити водяру.*\n*У вас течуть слюнки, ви себе не контролюєте і вириваєте флягу з рук Вована і починаєте хлебтати його добро*\n\n-ТИ ШО СУКА! - викрикнув Священик і пізданув вас в грязне око')
                    delay_print("\nВи в'єбали Вовану, у відповідь, флягой по голові. У Коляна пішла кров і він упав намертво на землю.")
                    delay_print('\n' + end[int(previous_answer) - 1][int(ans) - 1] + '\n')
                case '2':
                    delay_print('\nВи злякано підходите до Вєрочкі..')
                    delay_print('\n-СУКА ТИ, МРАЗЬ МАЛОЛЄТНЯ - кричить Баба Вєра')
                    delay_print('\n-Да Вєр, всьо нормас я чисто перетерти')
                    delay_print('\n-Я ТЕБЕ НАХУЙ НА ПОРОШОК ПЕРЕТРУ, піздуй отсюда. Уйобок')
                    delay_print('\nВи помаленьку підійшли до Вєри. Кліпнули очима та бачите перед собою летючу сумку. Вона летить прямо вам в єбало іі...')
                    delay_print("Вас вирубає у вічний сон. Бабу Вєру пов'язала поліція. Їй світить довічне.")
                    delay_print('\n' + end[int(previous_answer) - 1][int(ans) - 1] + '\n')
                case '3':
                    delay_print('\n-ТОЛІК, старий ти хрєн. Шуруй сюди! - вигукнули ви до Толяна')
                    delay_print('\n-Шо там братуха, як житуха, нассау в ухо')
                    delay_print('\n-Закрий рота і позич мені 20 грівен, мені на чікушку не вистачає пж')
                    delay_print('\n-' + name + '.. Ти мій найкращий друг, ти знаєш. Але броу, в мене самого щас голяк(((')
                    delay_print("\nВи не повірили Толіку, бо він ще такій піздабол, в'єбали йому в кадик і він упав задихаючись.")
                    delay_print("Ви спіздили пару гривень в Толіка і побігли купляти горілку. Толік мав заначку і вам вистачило на 0.5 Nemiroff.")
                    delay_print('\n' + end[int(previous_answer) - 1][int(ans) - 1] + '\n')
                case _:
                    while ans not in ["1", "2", "3"]:
                        delay_print('\nВажко було попасти по 1, 2 чи 3? ~_~')
                        ans = input(delay_print_choice('\nСпробуй ще раз: '))
                    answer_2(ans)
        case '2':
            match ans:
                case '1':
                    delay_print('\nВи обережно зайшли в супермаркет та аналізуєте де тут алкогольний відділ..')
                    delay_print('\nПройшовши далі по стендам ви бачите те, що вам потрібно. Козацька рада ^-^ ')
                    delay_print('\nОглянувшись довкола, ви швиденько зхватили бутилочку і направились до каси')
                    delay_print('\nВзяли собі жвачку по рублю і підійшли до каси')
                    delay_print('\n-Пакети потрібен? - каже касир')
                    delay_print("\n-Який нахуй пакетик, у мене одна жувачка..")
                    delay_print('\n-Потрібен чи ні?\n\n-Ні, дякую.\n\n-Маєте карту клієнта?\n\nВи гучно здихаєте та відповідаєте "ні"\n\n-У нас кокос по акції, не бажаєте придбати?\n\n*У вас уже здають нерви та тіче слина*')
                    delay_print('-Продайте уже жувачку - сказали Ви агресивно\n\n-Налік, аналік чи карта?\n\n-Налічка\n\n-Бажаєте оформити карту клієнта з кешбеком\n\n*Ви вже в рот єбали це слухать, дістали бутилку з карману і почали хлебтати її перед усіма*')
                    delay_print('\nПрибігла охорона та скрутила вас, визвавши поліцію. Вас посадять на 15 суток в нарко-диспансер і ви повинні заплатити штраф 2000 грн.')
                    delay_print('\n' + end[int(previous_answer) - 1][int(ans) - 1] + '\n')
                case '2':
                    delay_print('\nВи віришили, що ви нічим не хуже циганів тому вийшли на вулицю та стали просити гроші')
                    delay_print('\n-Подайте бідному роботязі на життя, не вистачає на хліб. Люди добрі!')
                    delay_print('\n*Хуйло* - пролунало десь із товпи')
                    delay_print('\n-поможіть пжпжпжпжпж')
                    delay_print('\nДо вас підійшов якісь багатий чувак в костюмі та каже: ')
                    delay_print("-Або ти сьобуєш по хороijму або мої хлопці тебе порішають\nВи обісрано відповіли йому: \n\n-А що ти зробиш попуск?\n\n*Прибігли два спортіка і останнє, що ви побачили це шкаф 2 на 2 рука якого летить вам в око*")
                    delay_print('\n' + end[int(previous_answer) - 1][int(ans) - 1] + '\n')
                case '3':
                    delay_print('\nВи вирішили поступити розумно')
                    delay_print('\nВи зайшли в магазин та придбали Жигуля, ви крутий!')
                    delay_print('\n' + end[int(previous_answer) - 1][int(ans) - 1] + '\n')
                case _:
                    while ans not in ["1", "2", "3"]:
                        delay_print('\nВажко було попасти по 1, 2 чи 3? ~_~')
                        ans = input(delay_print_choice('\nСпробуй ще раз: '))
                    answer_2(ans)
        case _:
            print('\n-\n--\n---\nnah brav fr, how da fuck did you came here?! *-*\n---\n--\n-\n')
    return ans

answer = answer_2(input_answer)

answers_array.append(answer)

previous_answer = answers_array[question_index]


delay_print('Ваша кінцівка: ')

end_string = ''

for answer in answers_array:
    delay_print(answer)
    delay_print('|')
    delay_print('V')
delay_print(end[int(answers_array[0]) - 1][int(answers_array[1]) - 1] + '\n')

delay_print('Чи сподобалсь вам гра? \n1. Так\n2. Не дуже\n3. ху-є-та')
feedback = input(delay_print_choice('Введіть вашу відповідь: '))