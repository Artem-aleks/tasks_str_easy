UPPERCASE = 'QWERTYUIOPASDFGHJKLZXCVBNMЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
LOWERCASE = 'qwertyuiopasdfghjklzxcvbnmёйцукенгшщзхъфывапролджэячсмитьбю'


def ft_percent_lower_uppercase(string):
    count_uppercase = 0
    count_lowercase = 0
    for char in string:
        if char in UPPERCASE:
            count_uppercase += 1
        elif char in LOWERCASE:
            count_lowercase += 1
    return count_lowercase / count_uppercase
