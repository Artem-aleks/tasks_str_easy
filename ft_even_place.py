def ft_len(string):
    count = 0
    for i in string:
        count += 1

    return count


def ft_even_place(string):
    result_string = str()
    for i in range(ft_len(string)):
        if i % 2 == 1:
            result_string += string[i]
    return result_string
