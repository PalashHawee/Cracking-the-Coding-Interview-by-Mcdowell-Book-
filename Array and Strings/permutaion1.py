def is_permutation(first_string, other_string):
    if len(first_string) != len(other_string):
        return False

    count_first = {}
    count_other = {}

    for char in first_string:
        if char in count_first.keys():
            count_first[char] += 1
        else:
            count_first[char] = 1

    for char in other_string:
        if char in count_other.keys():
            count_other[char] += 1
        else:
            count_other[char] = 1

    for char in count_first.keys():
        if char not in count_other.keys():
            return False
        elif count_first[char] != count_other[char]:
            return False

    return True