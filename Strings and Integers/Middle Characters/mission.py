def middle(text: str) -> str:
    # replace this for solution
    return text[len(text) // 2] if len(text) % 2 != 0 else text[len(text) // 2 - 1:len(text) // 2 + 1]


print("Example:")
print(middle("test"))

# These "asserts" are used for self-checking
assert middle("example") == "m"
assert middle("test") == "es"

print("The mission is done! Click 'Check Solution' to earn rewards!")
