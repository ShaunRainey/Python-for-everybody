string = "Hi! Hello!"
x = list(string)
newString = ""
for char in x:
    if char != "!":
        newString += char
print(newString)
# type: ignore

