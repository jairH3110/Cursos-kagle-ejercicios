#ejercicio1
# Your code goes here. Define a function called 'sign'
def sign(singo):
    if singo <0:
        a=-1
        return a
    elif singo >0:
        a=1
        return a
    elif singo ==0:
        a=0
        return a
    
    
print(sign(2)) 
# Check your answer
###############################################################################
#EJERCICIO 2
def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    if total_candies==1:
        print("Splitting", total_candies, "candy")
        return total_candies % 3
    else:
        print("Splitting", total_candies, "candies")
        return total_candies % 3
    

to_smash(91)
to_smash(1)
##########################################################################################
#EJERCICIO 3
def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
segundo = prepared_for_weather(False ,0 , False, False)
print(segundo)
prepared_for_weather(False ,0 , False, False)
# Check your answer
#q3.check()
##################################################################################################################
#EJERCICIO 4
def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return number <0

# Check your answer
#q4.check()
#########################################################################################
#EJERCICIO 5
def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    return not onion
def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    if ketchup==True and mustard ==True and onion == True:
        con_todo=True
        return con_todo
    else: return False
    #elif not ketchup==True and mustard ==True and onion == True:
    #    return

#######################################################################################################
#EJERCICIO 5b
def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    if ketchup== False and mustard==False and onion == False:
        return True
    else: return False

# Check your answer
#q5.b.check()
############################################################################3
#EJERCICIO 5c
def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    if  ketchup==True and mustard==True and onion==True:
        return False
    
    elif ketchup == True or mustard== True and onion ==True:
        return True
    
    if not ketchup==True and not mustard==True and not onion==True:
        return False
    
    
###########################################################################################
#EJERCICIO 6
def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    a=0 + mustard +ketchup + onion
    return a ==1 

# Check your answer
#q6.check()