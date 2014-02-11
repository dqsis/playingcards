# Purpose:
#     For developers we ran tests - if you can solve this in ten minutes
#     you are a match: Write a function which takes five playing cards as
#     input and checks if it is a two pair.
 
# Deck cards - suit does not matter
cards = ['A', '2', '3', '4', '5',
         '6', '7', '8', '9', 'J', 'Q', 'K']

# Input (either random or user-specific)
#hand = random.sample(cards, 5)
hand = ['2','2','7','7','9',]

# Function
def twopairs(hand):
    """ Check if there are 2 pairs in the hand """
    pairs = set([x for x in hand if hand.count(x) == 2])    
    return pairs 
        
# Call function    
control = twopairs(hand)

# Control and dutput results
if len(control) == 2:
    print('There are 2 pairs in your hand!', )
    print(control)
else:
    print('There are not 2 pairs in your hand!')