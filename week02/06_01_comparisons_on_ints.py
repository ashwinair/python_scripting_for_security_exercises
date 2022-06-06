# Run some basic comparisons on basic integers and floating points

# what is bigger, a or b?
a = 2
b = 10
print(a if a > b else b)
# What is smaller , c or d?
c = 2.02
d = 2.01119999
print(c if c < d else d)
# what is bigger e or f?
e = float("inf")
f = 12912912912091928312903713582043754302895723048957
print(e if e > f else f)
# are these equal?

g = 1.02020202020
i = 1.0202020202011111
print(g == i)
