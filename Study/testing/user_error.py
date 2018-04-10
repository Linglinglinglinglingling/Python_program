def get_age():
    age=int(input('enter a age greater than 18 '))
    if age<19:
        raise ValueError('age need to be greater than 18.')
    return age

get_age()