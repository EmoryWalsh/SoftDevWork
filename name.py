import random

KREWES = {
    'orpheus': ['Emily', 'Kevin', 'Vishwaa', 'Eric', 'Ray', 'Jesse', 'Tiffany', 'Amanda', 'Junhee', 'Jackie'],
    'rex': ['William', 'Joseph', 'Calvin', 'Ethan'],
    'endymion': ['Grace', 'Nahi', 'Derek', 'Jun Tao']
}


#PRECONDITION: team is one of the three team names
def getName(team):
    return random.choice(KREWES[team])



print(getName("orpheus"))
print(getName("orpheus"))
print(getName("rex"))
print(getName("endymion"))
