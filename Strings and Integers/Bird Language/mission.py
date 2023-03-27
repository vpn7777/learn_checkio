def translate(text: str) -> str:
    for i in "aeiouy":
        text = text.replace(i + i + i, i)
    new_text = text[0]
    for i in range(1, len(text)):
        if text[i - 1] not in " aeiouy":
            new_text += ''
        else:
            new_text += text[i]

    return new_text


print("Example:")
print(translate("hieeelalaooo"))

# These "asserts" are used for self-checking
assert translate("hieeelalaooo") == "hello"
assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translate("aaa bo cy da eee fe") == "a b c d e f"
assert translate("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")
