def get_attribute(query, default):
    question = query + ' [' + default + ']? '
    answer = input(question)
    if (answer == ''):
        answer = default
    print('You choose ' + answer)
    return answer

hair = get_attribute('What hair colour', 'brown')
hair_length = get_attribute('What hair length', 'short')
eye = get_attribute('What eye colour', 'blue')
gender = get_attribute('What gender', 'female')
glasses = get_attribute('Has glasses', 'no')
beard = get_attribute('Has beard', 'no')
