def find_max(list):
    max = list[0]
    for items in list:
        if max < items:
            max = items
    return max