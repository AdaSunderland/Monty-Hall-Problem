# Calculate winning probability in Monty Hall
# Have k doors and Zonk opens s doors
# Note: In order to see the tables, please use <pip install tabulate> to get this table package first

from __future__ import division
from tabulate import tabulate
import random

n = 10000

##############################
##### Set Game Function ######
##############################

# ----------let guest and Zonk pick the door----------
def pick_door(k, s):
    doors = ['goat'] * (k - 1) + ['car'] * 1  # set k doors, only one contains prize
    random.shuffle(doors)
    guest_pick = doors.pop(random.randrange(0, len(doors)))  # Guest randomly pick a door
    for i in range(s):
        del doors[doors.index('goat')]   # Zonk must pick s goat doors
    switch_door = doors.pop(random.randint(0, len(doors) - 1))  # The switched door is picked from the rest doors
    # if guest doesn't switch the door
    stay = guest_pick

    return stay, switch_door

# ----------choose whether to stay or switch and count the winning times----------
def switch_or_not(num, k, s):
    stay_wins = 0
    stay_lose = 0
    switch_wins = 0
    switch_lose = 0
    switch = num
    for i in range(n):
        stay, switch_door = pick_door(k, s)
        if switch == 0:  # choose to stay
            if stay == 'car':
                stay_wins += 1
            else:
                stay_lose += 1
        elif switch == 1:  # choose to switch
            if switch_door == 'car':
                switch_wins += 1
            else:
                switch_lose += 1

    return stay_wins, stay_lose, switch_wins, switch_lose

# ----------calculate the probabilities for stay and switch----------
def probability():
    # if stay
    stay_wins0, stay_lose0, switch_wins0, switch_lose0 = switch_or_not(0, k, s)
    stay_prob = float(stay_wins0)/(stay_wins0 + stay_lose0)
    # if switch
    stay_wins1, stay_lose1, switch_wins1, switch_lose1 = switch_or_not(1, k, s)
    switch_prob = float(switch_wins1)/(switch_wins1 + switch_lose1)

    return stay_prob, switch_prob


##############################
######## Main Program ########
##############################

door_num = [3, 4, 5, 6, 7, 8, 9, 10]
zonk_open = [2, 3, 4, 5]

stay_list = []
switch_list = []

for s in zonk_open:
    for k in door_num:
        # if the existing doors are equal to Zonk picked doors, then this game doesn't work
        if k < s + 1:
            stay_prob = 'N/A'
            switch_prob = 'N/A'
            stay_list.append(stay_prob)
            switch_list.append(switch_prob)
        # guest must pick the prize door and Zonk picks all goat doors, otherwise this game doesn't work
        elif k == s + 1:
            stay_prob = str('{0:.0%}'.format(1)) + ' or N/A'
            switch_prob = 'N/A'
            stay_list.append(stay_prob)
            switch_list.append(switch_prob)
        # begin normal game
        elif k > s + 1:
            stay_prob, switch_prob = probability()
            stay_list.append('{0:.2%}'.format(stay_prob))
            switch_list.append('{0:.2%}'.format(switch_prob))

stay_row_list = [stay_list[i:i+8] for i in range(0, len(stay_list), 8)]
switch_row_list = [switch_list[i:i+8] for i in range(0, len(switch_list), 8)]

# ----------draw the tables----------
for s in zonk_open:
    stay_row_list[zonk_open.index(s)].insert(0, str(s))
    switch_row_list[zonk_open.index(s)].insert(0, str(s))

print tabulate(stay_row_list, headers=['STAY', 3, 4, 5, 6, 7, 8, 9, 10], tablefmt='pipe')
print '\n'
print tabulate(switch_row_list, headers=['SWITCH', 3, 4, 5, 6, 7, 8, 9, 10], tablefmt='pipe')
