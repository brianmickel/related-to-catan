# input:
# player
#  settlement/city
#   adj resources
#    number
"""
input = [[playernumber settlement/city [adjresources] [adjnumbers]],
[playernumber settlement/city [adjresources] [adjnumbers]],
[playernumber settlement/city [adjresources] [adjnumbers]]]
settlement/city:
0 - settlement
1 - city
resources:
lumber, brick, wool, wheat, ore
probabilities:
2 - 1/36
3 - 2/36
4 - 3/36
5 - 4/36
6 - 5/36
!!7!!
8 - 5/36
9 - 4/36
10 - 3/36
11 - 2/36
12 - 1/36

not realistic example:
list_of_buildings = [
[1, settlement, ['lumber','brick','ore'], [2,11,6]],
[1, settlement, ['lumber','brick','ore'], [2,11,6]],
[2, city, ['lumber','wool','wheat'], [9,10,11]],
[3, city, ['lumber','wool'], [6,8]],
[4, settlement, ['lumber','lumber'], [4,5]]
]


"""

probabilities = {
2: 1/36,
3: 2/36,
4: 3/36,
5: 4/36,
6: 5/36,
7: 6/36,
8: 5/36,
9: 4/36,
10: 3/36,
11: 2/36,
12: 1/36
}

def calculateExpectedValue(list_of_buildings):
    output = {1: {
    'lumber': 0,
    'brick': 0,
    'wool': 0,
    'wheat': 0,
    'ore': 0
    },
    2: {
    'lumber': 0,
    'brick': 0,
    'wool': 0,
    'wheat': 0,
    'ore': 0
    },
    3: {
    'lumber': 0,
    'brick': 0,
    'wool': 0,
    'wheat': 0,
    'ore': 0
    },
    4: {
    'lumber': 0,
    'brick': 0,
    'wool': 0,
    'wheat': 0,
    'ore': 0
    }
    }

    for villageData in list_of_buildings:
        playerNumber = villageData[0]
        settlementType = 1 if villageData[1] == 'settlement' else 2
        for i in range(len(villageData[2])):
            adjResource = villageData[2][i]
            adjResourceNumber = villageData[3][i]
            if adjResource == 'lumber':
                output[playerNumber]['lumber'] += probabilities[adjResourceNumber]*settlementType
            elif adjResource == 'brick':
                output[playerNumber]['brick'] += probabilities[adjResourceNumber]*settlementType
            elif adjResource == 'wool':
                output[playerNumber]['wool'] += probabilities[adjResourceNumber]*settlementType
            elif adjResource == 'wheat':
                output[playerNumber]['wheat'] += probabilities[adjResourceNumber]*settlementType
            elif adjResource == 'ore':
                output[playerNumber]['ore'] += probabilities[adjResourceNumber]*settlementType
    return output

list_of_buildings = [
[1, 'settlement', ['lumber','brick','ore'], [2,11,6]],
[1, 'settlement', ['lumber','brick','ore'], [2,11,6]],
[2, 'city', ['lumber','wool','wheat'], [9,10,11]],
[3, 'city', ['lumber','wool'], [6,8]],
[4, 'settlement', ['lumber','lumber'], [4,5]]
]

expected_value = calculateExpectedValue(list_of_buildings)
for i in range(1,5):
    print(i)
    print(expected_value[i])

"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt


n_groups = 4

expected_values_lumber = (expected_value[1]['lumber'],expected_value[2]['lumber'],expected_value[3]['lumber'],expected_value[4]['lumber'])
expected_values_brick = (expected_value[1]['brick'],expected_value[2]['brick'],expected_value[3]['brick'],expected_value[4]['brick'])
expected_values_wool = (expected_value[1]['wool'],expected_value[2]['wool'],expected_value[3]['wool'],expected_value[4]['wool'])
expected_values_wheat = (expected_value[1]['wheat'],expected_value[2]['wheat'],expected_value[3]['wheat'],expected_value[4]['wheat'])
expected_values_ore = (expected_value[1]['ore'],expected_value[2]['ore'],expected_value[3]['ore'],expected_value[4]['ore'])

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 1/8
opacity = 0.4

rects1 = plt.bar(index, expected_values_lumber, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Lumber')

rects2 = plt.bar(index + 1*bar_width, expected_values_brick, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Brick')
rects3 = plt.bar(index + 2*bar_width, expected_values_wool, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Wool')

rects4 = plt.bar(index + 3*bar_width, expected_values_wheat, bar_width,
                 alpha=opacity,
                 color='c',
                 label='Wheat')

rects5 = plt.bar(index + 4*bar_width, expected_values_ore, bar_width,
                 alpha=opacity,
                 color='m',
                 label='Ore')


plt.xlabel('Player')
plt.ylabel('Expected Value')
plt.title('Expected Value by player by resource')
plt.xticks(index, ('Player 1', 'Player 2', 'Player 3', 'Player 4'))
plt.legend()

#plt.tight_layout()
plt.show()
