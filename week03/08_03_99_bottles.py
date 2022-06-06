# write a script that will "sing" a song that goes like this
#  "there are 100 jars of payasam on the counter ...... now i ate one!"
# "there are 99 jars of payasam on the counter ... now I ate one!"
#
#
# "there are 0 jars of payasam on the counter - none left to eat!"
# "now I will go vomit...."

# you must use a while loop to do it
payasam_jars = 100
while payasam_jars>0:
    print(f"there are {payasam_jars} jars of payasam on the counter ...... now i ate one!")
    payasam_jars -=1

print("there are 0 jars of payasam on the counter - none left to eat!")
print("now I will go vomit....")