# Type casting Exercise - 2
# Addition of string and integer using explicit conversion

# Initialise a string variable and integer variable
a = 10
b = "10"

# After explicit conversion, use python to successfully perform
# the addition of these variables - print the result to the console
print(a + int(b))

## Now try to convert this variable
c = "ten"
int(c)
## What kind of error does python give?
# ValueError.

## What do you think the reason is?
# "We can't convert/change a string of characters into int."