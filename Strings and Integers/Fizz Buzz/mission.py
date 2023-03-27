# Taken from mission Just Fizz!

def checkio(num: int) -> str:
    lst = [num % 3 == 0, num % 5 == 0]
    if all(lst):
        return "Fizz Buzz"
    elif lst[0]:
        return "Fizz"
    elif lst[1]:
        return "Buzz"
    else:
        return str(num)


print("Example:")
print(checkio(15))

# These "asserts" are used for self-checking
assert checkio(15) == "Fizz Buzz"
assert checkio(6) == "Fizz"
assert checkio(10) == "Buzz"
assert checkio(7) == "7"

print("The mission is done! Click 'Check Solution' to earn rewards!")
