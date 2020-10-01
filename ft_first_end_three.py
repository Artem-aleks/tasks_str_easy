def ft_len(str):
    count = 0
    for i in str:
        count += 1
    return count


def ft_first_end_three(string):
    if ft_len(string) > 5:
        return string[0] + string[1] + string[2]\
               + string[-3] + string[-2] + string[-1]
    return string[0] * ft_len(string)
