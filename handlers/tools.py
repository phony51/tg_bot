REGISTRATION_DEFS = {
    'genders': {
        'male': 'Мужской',
        'female': 'Женский'
    },
    'name_regex': r'^[А-Я][а-я]{,32}|[A-Z][a-z]{,32}$',
    'min_age': 14
}


def decline_age(age_to: int):
    declined_noun = (age_to in range(5, 20)) and 'лет' or (1 in (age_to, (diglast := age_to % 10))) and 'год' or (
            {age_to, diglast} & {2, 3, 4}) and 'года' or 'лет'
    return f'{age_to} {declined_noun}'
