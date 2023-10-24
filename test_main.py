import main

def test_charivna_kulka():
    assert main.charivna_kulka('Is Niggers real?') in ["Is Niggers real?, 'Yes'", "Is Niggers real?, 'No'", "Is Niggers real?, 'IDK'"]
    assert type(main.charivna_kulka('Is Niggers real?')) == str
    assert main.charivna_kulka(6) == 'Its not string, fuck off!'
    assert main.charivna_kulka('') == 'Its empty string, fuck off!'

def test_configure_magic_ball():
    new_answers = ['Almost', 'Nah bro']
    assert type(new_answers) == list
    assert type(new_answers[1]) == str
    main.configure_magic_ball(new_answers)
    assert main.answers == ['Yes', 'No', 'IDK', 'Almost', 'Nah bro']

def test_charivna_kulka_configured():
    assert main.charivna_kulka('The planet is flat?') in ["The planet is flat?, 'Yes'", "The planet is flat?, 'No'", "The planet is flat?, 'IDK'",
                                                           "The planet is flat?, 'Almost'", "The planet is flat?, 'Nah Bro'"]
    assert type(main.charivna_kulka('Grey 59')) == str
    assert main.charivna_kulka(123) == 'Its not string, fuck off!'
    assert main.charivna_kulka(' ') == 'Its empty string, fuck off!'