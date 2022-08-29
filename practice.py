

values = [10, 11, 43, -453, 5, 4, 5, "12", 28]


def larget_number(val):

    return max(val)


print("larget_number", larget_number(values))


def find_max_number(val):
    largest = val[0]
    for number in val:
        if number > largest:
            largest = number
    return largest


print("find_max_number", find_max_number(values))
