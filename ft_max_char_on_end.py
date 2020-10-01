def ft_len(string):
    count = 0
    for i in string:
        count += 1

    return count


def ft_max_char_on_end(string):
    length_seq = 1
    count = 1
    for i in range(1, ft_len(string)):
        if string[i] == string[i - 1]:
            count += 1
        if string[i] != string[i - 1]:
            length_seq = count
            count = 1
    return length_seq
