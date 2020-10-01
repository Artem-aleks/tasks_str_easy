def ft_cmp_str(str1, str2, num):
    result_string = ''
    result_string += str1[:num] + str2 + str1[num:]
    return result_string
