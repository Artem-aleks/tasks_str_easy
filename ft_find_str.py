def ft_len(string):
    count = 0
    for i in string:
        count += 1

    return count


def ft_find_str(str1, str2):
    if str2 in str1:
        for i in range(ft_len(str1)):
            for j in str2:
                if str1[i] == j:
                    if str1[i:ft_len(str2) + i] == str2:
                        return i
    return -1
