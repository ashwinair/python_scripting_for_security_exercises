# use a for loop with enumerate to go over the long word and
# sum all the indices for every single vowel

# example:
#
# input: "hi I me
# i=1, I=3, e = 6,
# the sum is: 10

a_long_word = "the quick brown fox jumped over the lazy dog and then ran around and got very happy happy happy yes!"
# the sum should be 1147 (you can check your code with this)
sum_of_words = 0
for word in enumerate(a_long_word):
    # print(word[1], end="")
    if word[1] == ' ':
        # print(word[1], end =" ")
        val = word[0] - 1
        sum_of_words += val
print(sum_of_words)