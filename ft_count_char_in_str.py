def ft_count_char_in_str(char, string):
    count = 0
    for i in string:
        if i == char:
            count += 1
    return count
