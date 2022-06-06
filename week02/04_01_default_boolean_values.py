# Boolean Exercise_1
# Let's check all the default boolean values of the types we know

# make
# an int
# a float
# a string
# the int 0
# the int 1
# the int 1000
integer = 10
float_value = 1.2
string = "yo!"

print(f"int value: {bool(integer)}")
print(f"float_value: {bool(float_value)}")
print(f"string value: {bool(string)}")

int_val = 0
print(f"int_value 0: {bool(int_val)}")
int_val = 1
print(f"int_value 1: {bool(int_val)}")
int_val = 1000
print(f"int_value 1000: {bool(int_val)}")

# now print out all the `bool()` values using the bool() function
# are you surprised at the default boolean value for any python type?
# # Yes! By the value of int_value 0 is False.
# When converting a bool to an int, the integer value is always 0 or 1,
# but when converting an int to a bool, the boolean value is True for all integers except 0.