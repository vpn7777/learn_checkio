def checkio(food: int) -> int:
    current_number_pigeons = 1
    incoming_pigeons = 1
    while food >= current_number_pigeons:
        food -= current_number_pigeons
        incoming_pigeons += 1
        if current_number_pigeons + incoming_pigeons == food:
            return current_number_pigeons + incoming_pigeons
        elif current_number_pigeons + incoming_pigeons > food:
            return current_number_pigeons if food < current_number_pigeons else food
        else:
            current_number_pigeons += incoming_pigeons


print("Example:")
print(checkio(5))

# These "asserts" are used for self-checking
assert checkio(1) == 1
assert checkio(3) == 2
assert checkio(5) == 3
assert checkio(10) == 6

print("The mission is done! Click 'Check Solution' to earn rewards!")
