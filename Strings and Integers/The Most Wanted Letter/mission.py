def checkio(text: str) -> str:
    lst = [i for i in sorted(text.lower()) if i.isalpha()]
    counter = 0
    let = None
    for i in lst:
        if lst.count(i) > counter:
            counter = lst.count(i)
            let = i
    return let


print("Example:")
print(checkio("Hello World!"))

# These "asserts" are used for self-checking
assert checkio("Hello World!") == "l"
assert checkio("How do you do?") == "o"
assert checkio("One") == "e"
assert checkio("Oops!") == "o"
assert checkio("AAaooo!!!!") == "a"
assert checkio("abe") == "a"

print("The mission is done! Click 'Check Solution' to earn rewards!")
