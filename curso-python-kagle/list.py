##################################################################################
#EJERCICIO1 

def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L) <  2:
        return None
    else:
        a= L[1]
        print(a,"fff")
        return a 
 

# Check your answer
#q1.check()
#########################################################################################3
#EJERCICIO 2

def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """ 
    #print(teams[-1:])
    #print(teams[-1:][1][-4:])
    a= teams[-1:]
    print (a)
    b= a [0][1]
    print(b)
    return b

# Check your answer
#q2.check()


#######################################################################################
#EJERCICIO 3



def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    print(racers)
    a=  racers[-1:]
    print(a)
    b= racers[:1]
    print(b)
    
    racers[-1:],racers[:1] = racers[:1], racers[-1:]
    
    print(racers) 
    #c= "".join(b)
    
    #racers[0] =a
    #racers[-1:]=c
    
    #print(a,c)
    #print(racers)
    return None




##################################################################################################
#EJERCICIO 4
a = [1, 2, 3]
b = [1, [2, 3]] 
c = [] 
d = [1, 2, 3][1:]
lengths = [3,2,0,2]
#q4.check()

######################################################################################################
#EJERCICIO 5
def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    a = len(arrivals)
    a = a/2
    print(a)
    b= int(a)+1
    print(b)
    
    if name in arrivals[b:-1] and b>3:
        return True
    elif b==3 and name in arrivals[b-1:-1]:
            return True
    else:
        return False

# Check your answer
#q5.check()