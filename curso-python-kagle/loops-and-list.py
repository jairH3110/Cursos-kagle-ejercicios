##################################################################################
#EJERCICIO 1
def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        print(num)
        if num % 7 == 0:
            return True
    return False       
print(has_lucky_number([2,3,3,7])) 


# Check your answer
#q1.check()


#########################################################################################3
#EJERCICIO 2

def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    n =[]
    
    for i in L:
        n.append(i>thresh)
        
    return n


# Check your answer
#q2.check()

#######################################################################################
#EJERCICIO 3
def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    a=[]
    b=[]
    
    x=0
    for i in meals:
        a.append(i)
        b.append(i)   
    c=len(a)
    d=c-1
    for h in range(d):
        x+=1
        print(x)
        if a[h]== a[x]:
            return True
        
    print(a)
    print(b)
    
    return False
    

# Check your answer
#q3.check()

##################################################################################################
#EJERCICIO 4

def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    xd= []
    a=20
    for i in range(n_runs):
        estimate_average_slot_payout()
        
        xd.append[i]
    suma= sum(xd)
    
    result =suma/a 
    print(result)
    return result


######################################################################################################
