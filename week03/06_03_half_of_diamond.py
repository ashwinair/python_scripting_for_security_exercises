# Exercise

# Write a Python program to construct the following pattern, using a nested for loop.
"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""
no_of_stars = int(input("Total no of stars you want is?: "))

for stars in range(0, no_of_stars):
    if stars > no_of_stars/2:
        stars = no_of_stars - stars

    for star in range(0, stars):
        print('*', end="")
    print('\n')
