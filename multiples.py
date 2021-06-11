# If we list all the natural numbers below 10 that are 
# multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000. 

# declare a counter to keep track of the total
# declare a variable, num, is 1000
# declare a var, numLength, to find range and length of num. 
# declare var, eachNum, for each index of numLength
# while numLength is less than 1000: 
# set a var, prime, to equal divide eachNum by 3 or 5  
# if no remainder, add eachNum to total
# return total


def Multiples(param):
    total = 0
    for i in range(param):
        if (i % 3 == 0) or (i % 5 == 0):
            total += i
    return total

print(Multiples(1000))
