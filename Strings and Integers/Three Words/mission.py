def checkio(words: str) -> bool:
    flag = 0
    for word in words.split():
        if word.isdigit():
            flag = 0
        else:
            flag += 1
        if flag == 3:
            return True
    return False


print("Example:")
print(checkio("Hello World hello"))

# These "asserts" are used for self-checking
assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
assert checkio("Hi") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
