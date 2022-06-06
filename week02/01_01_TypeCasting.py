# Type Casting Exercise

a = 7

type(a)
# 1. print the type of the variable
#   Convert integer variable to float and confirm the type cast worked (print it out)
a = float(a)
print(type(a))

# 2. Now, Convert your float variable to string and print out the type
a = str(a)
print(type(a))
# 3. Finally, Convert your string variable back to integer and print it out (the type)
a = int(float(a))
print(type(a))
