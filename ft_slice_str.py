def ft_len(str):
    count = 0
    for i in str:
        count += 1

    return count


def ft_slice_str(string, start, stop):
    result_string = ''
    for i in range(start, stop):
        result_string += string[i]
    return result_string
