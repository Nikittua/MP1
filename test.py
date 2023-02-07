def common_elements(a, b):
    common = []
    for el in a:
        if el in b and el not in common:
            common.append(el)
    return common

a = [7, 17, 1, 9, 1, 17, 56, 56, 23]
b = [56, 17, 17, 1, 23, 34, 23, 1, 8, 1]
print(common_elements(a, b))

