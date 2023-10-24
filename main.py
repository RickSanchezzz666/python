import random

answers = ['Yes', 'No', 'IDK']

def charivna_kulka(question):
    """
    Функція charivna_kulka призначена для відповіді на питання користувача.

    Параметри:
    question (str): Питання користувача, на яке потрібно отримати відповідь.

    Повертає:
    str: Випадкова відповідь на питання користувача, в форматі "{питання}, '{відповідь}'".

    Приклад використання:
    >>> charivna_kulka("Чи сьогодні буде дощ?")
    "Чи сьогодні буде дощ?, 'Так'"

    >>> charivna_kulka("Is niggers real?")
    "Is niggers real?, 'No'"
    """
    if(type(question) is not str):
        return 'Its not string, fuck off!'
    elif(question == '' or question == ' '):
        return 'Its empty string, fuck off!'
    randomAnswer = random.choice(answers)
    return f"{question}, '{randomAnswer}'"

def configure_magic_ball(new_answers: list):
    global answers
    answers.extend(new_answers)