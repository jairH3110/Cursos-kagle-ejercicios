##################################################################################
#EJERCICIO1
# Import the jimmy_slots submodule
from learntools.python import jimmy_slots
# Call the get_graph() function to get Jimmy's graph
graph = jimmy_slots.get_graph()
graph

def prettify_graph(graph):
    """Modify the given graph according to Jimmy's requests: add a title, make the y-axis
    start at 0, label the y-axis. (And, if you're feeling ambitious, format the tick marks
    as dollar amounts using the "$" symbol.)
    """
    graph.set_title("Results of 500 slot machine pulls")
    # Complete steps 2 and 3 here
    graph.set_ylim(bottom=0)  # Set y-axis to start at 0
    graph.set_ylabel("Balance")  # Label for y-axis

graph = jimmy_slots.get_graph()
prettify_graph(graph)
graph

#########################################################################################3
#EJERCICIO2
# Import luigi's full dataset of race data
from learntools.python.luigi_analysis import full_dataset

# Fix me!
def best_items(racers):
    winner_item_counts = {}
    for rango in range(len(racers)):
        racer = racers[rango]
        if racer['finish'] == 1:
            for item in racer['items']:
                if item not in winner_item_counts:
                    winner_item_counts[item] = 0
                winner_item_counts[item] += 1

        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                rango+1, len(racers), racer['name'])
                 )
    return winner_item_counts

# Try analyzing the imported full dataset
best_items(full_dataset)



#######################################################################################
#EJERCICIO 3
def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    def hand_value(hand):
        """Calculates the value of a blackjack hand, treating all cards as numeric values."""
        value = 0
        num_aces = 0
        
        for card in hand:
            if card in 'JQK':
                value += 10
            elif card == 'A':
                num_aces += 1
                value += 11
            else:
                value += int(card)
        
        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1
        
        return value
    
    total_1 = hand_value(hand_1)
    total_2 = hand_value(hand_2)
    
    return total_1 <= 21 and (total_1 > total_2 or total_2 > 21)

    pass

# Check your answer
#q3.check()


##################################################################################################

######################################################################################################
