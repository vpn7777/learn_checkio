def cut_sentence(line: str, length: int) -> str:
    if len(line) <= length:
        return line
    elif line[length] == " ":
        return line[:length].strip() + "..."
    elif len(line[:line.find(' ')]) > length:
        return '...'
    else:
        return line[:line[:length].rfind(' ')].strip() + "..."


print("Example:")
print(cut_sentence("Hi my name is Alex", 4))

# These "asserts" are used for self-checking
assert cut_sentence("Hi my name is Alex", 8) == "Hi my..."
assert cut_sentence("Hi my name is Alex", 4) == "Hi..."
assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex"
assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"

print("The mission is done! Click 'Check Solution' to earn rewards!")
