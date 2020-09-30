def ft_len(string):
    count = 0
    for i in string:
        count += 1

    return count


def ft_three_str(str1, str2, str3):
    # result_str = str()
    # if str2 in str1:
    #     for i in range(ft_len(str1)):
    #         for j in str2:
    #             if str1[i] == j:
    #                 if str1[i:ft_len(str2) + i] == str2:
    #                     result_str = str1[:i] + str3 + str1[ft_len(str3) + i:]
    # return result_str
    return str1.replace(str2, str3)
