def from_camel_case(name: str) -> str:
     return name[0].lower() + ''.join(["_" + i.lower() if i.isupper() else i for i in name[1::]])


print("Example:")
print(from_camel_case("MyFunctionName"))

# These "asserts" are used for self-checking
assert from_camel_case("MyFunctionName") == "my_function_name"
assert from_camel_case("IPhone") == "i_phone"

print("The mission is done! Click 'Check Solution' to earn rewards!")
