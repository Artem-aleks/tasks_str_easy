def ft_len(str):
    count = 0
    for i in str:
        count += 1

    return count


def ft_equal_reverse(string):
    x = ft_len(string)
    i = 0
    x = x - 1
    k = 0
    while x - i >= i:
        if string[x - i] == string[i]:
            i += 1
        else:
            k = 1
            break
    if k == 1:
        return False
    return True
