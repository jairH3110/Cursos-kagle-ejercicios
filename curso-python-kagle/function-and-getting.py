################################################################################################################################
#EJERCICIO1

def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    resultado = round(num, 2)
    return resultado
    

# Check your answer
##########################################################################
#EJERCICIO2

round(21231.654457456,-2)

###########################################################################################
#EJERCICIO 3
def to_smash(total_candies,n=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % n

#############################################################################################3
#EJERCICIO 4 OPTIONAL
#ruound_to_two_places(9.9999)
# x = -10
# y = 5
# # Which of the two variables above has the smallest absolute value?
# smallest_abs = min(abs(x, y))
# def f(x):
#     y = abs(x)
# return y

# print(f(5))