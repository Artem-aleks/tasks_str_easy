def ft_len(str):
    count = 0
    for i in str:
        count += 1
    return count


def ft_cmp_str(str1, str2, num):
    result_string = ''
    for i in range(num):
        result_string += str1[i]
    result_string += str2
    for i in range(num, ft_len(str1)):
        result_string += str1[i]
    return result_string
