def ft_len(str):
    count = 0
    for i in str:
        count += 1

    return count


def ft_reverse_str(string):
    result_string = ''
    for i in range(-1, -ft_len(string)-1, -1):
        result_string += string[i]
    return result_string
