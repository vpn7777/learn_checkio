def column_number(name: str) -> int:
    my_dic = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = 0
    for i in range(len(name) - 1, -1, -1):
        num += (26 ** i * my_dic.index(name[::-1][i]))
    return num


print("Example:")
print(column_number("ZY"))

# These "asserts" are used for self-checking
assert column_number("A") == 1
assert column_number("Z") == 26
assert column_number("AB") == 28
assert column_number("ZY") == 701

print("The first mission is done! Click 'Check' to earn cool rewards!")
