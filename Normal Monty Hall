# Meng Jia
# Simulate Monty Hall Problem
# Have three doors and play for 10000 times

from __future__ import division
import random

n = 10000

# ----------let guest and zonk pick the door----------
def pick_door():
    doors = ['goat'] * 2 + ['car'] * 1  # set three door
    guest_pick = doors.pop(random.randrange(0, len(doors)))  # Guest randomly pick a door
    zonk_pick = doors.pop(doors.index('goat'))  # Zonk must pick a goat door
    switch_door = doors.pop(random.randint(0, len(doors) - 1))  # The switched door is picked from the rest doors
    # if guest doesn't switch the door
    stay = guest_pick

    return stay, switch_door

# ----------choose whether to stay or switch and count the winning times----------
def switch_or_not(num):
    stay_wins = 0
    stay_lose = 0
    switch_wins = 0
    switch_lose = 0
    switch = num
    for i in range(n):
        stay, switch_door = pick_door()
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
    stay_wins0, stay_lose0, switch_wins0, switch_lose0 = switch_or_not(0)
    stay_prob = float(stay_wins0)/(stay_wins0 + stay_lose0)
    # if switch
    stay_wins1, stay_lose1, switch_wins1, switch_lose1 = switch_or_not(1)
    switch_prob = float(switch_wins1)/(switch_wins1 + switch_lose1)

    return stay_prob, switch_prob

# ----------results----------
stay_prob, switch_prob = probability()
print 'Stay: %s chance to win' % '{0:.2%}'.format(stay_prob)
print 'Switch: %s chance to win' % '{0:.2%}'.format(switch_prob)
