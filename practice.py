

values = [10, 11, 43, 453, 5, 4, 5, 66, 28]


def larget_number(val):
    return max(val)


def find_max_number(val):
    max = val[0]
    for number in val:
        if number > max:
            max = number
    return max
