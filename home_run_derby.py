"""
HRDerby.py

Author: Cole Petersen

This simulates a home run derby! It is a work in progress, and I would like to add more to it in the future.
"""

import random
import operator
import time

"""
The likeliness of each event happening on a swing would be its value minus the previous event value, divided by 100.
For example, with current values, the one seed has a 1% chance of swinging and missing, a 2% chance of hitting a ground
ball out, a 14% chance of hitting a line drive out, a 26% chance of hitting a fly ball out, and a 57% chance of hitting
a home run when swinging. Each batter has an 80% chance of swinging.
"""

contestants = {
    1: {'name': 'The 1 seed', 'swing_and_miss': 1, 'ground_ball': 3, 'line_drive': 17, 'fly_ball': 43, 'home_runs': 0},
    2: {'name': 'The 2 seed', 'swing_and_miss': 1, 'ground_ball': 8, 'line_drive': 20, 'fly_ball': 45, 'home_runs': 0},
    3: {'name': 'The 3 seed', 'swing_and_miss': 1, 'ground_ball': 8, 'line_drive': 21, 'fly_ball': 48, 'home_runs': 0},
    4: {'name': 'The 4 seed', 'swing_and_miss': 1, 'ground_ball': 11, 'line_drive': 17, 'fly_ball': 50, 'home_runs': 0},
    5: {'name': 'The 5 seed', 'swing_and_miss': 1, 'ground_ball': 10, 'line_drive': 23, 'fly_ball': 53, 'home_runs': 0},
    6: {'name': 'The 6 seed', 'swing_and_miss': 1, 'ground_ball': 11, 'line_drive': 28, 'fly_ball': 58, 'home_runs': 0},
    7: {'name': 'The 7 seed', 'swing_and_miss': 1, 'ground_ball': 15, 'line_drive': 28, 'fly_ball': 64, 'home_runs': 0},
    8: {'name': 'The 8 seed', 'swing_and_miss': 1, 'ground_ball': 11, 'line_drive': 31, 'fly_ball': 68, 'home_runs': 0}
}

input('Press Enter to start.')

for contestant in reversed(sorted(contestants.keys())):

    seconds = 240  # Each batter gets 4 minutes
    home_runs = 0
    bonus = False  # If a batter hits a home run longer than 440 feet, they get a 30 second bonus (once)

    print(contestants[contestant]['name'] + ':')

    while seconds > 0:
        time.sleep(0.5)
        swings = random.randint(1, 5)
        if swings <= 4:  # 80% chance of swinging
            result = random.randint(1, 100)
            if result <= contestants[contestant]['swing_and_miss']:
                # Swing and miss, taking 4 seconds
                seconds = seconds - 4
                print('Swing and a miss, embarrassing! ' + str(seconds) + ' seconds remaining.')
            elif result <= contestants[contestant]['ground_ball']:
                # Ground ball, taking 6 seconds
                seconds = seconds - 6
                print('Ground ball, ' + str(seconds) + ' seconds remaining.')
            elif result <= contestants[contestant]['line_drive']:
                # Line drive, taking 6 seconds
                seconds = seconds - 6
                print('Line drive, ' + str(seconds) + ' seconds remaining.')
            elif result <= contestants[contestant]['fly_ball']:
                # Fly ball, taking 8 seconds
                seconds = seconds - 8
                print('Fly ball, ' + str(seconds) + ' seconds remaining.')
            else:
                # Home run, taking 8 seconds
                seconds = seconds - 8
                home_runs = home_runs + 1
                print('Home run! ' + str(seconds) + ' seconds remaining and ' + str(home_runs) + ' home runs!')
                distance_bonus = random.randint(1, 10)  # 10% chance of a home run being longer than 440 feet
                if distance_bonus >= 10 and not bonus:
                    bonus = True
                    seconds = seconds + 30
                    print('  That home run was more than 440 feet, so there is a 30 second bonus! ' + str(seconds) +
                          ' seconds remaining.')

        else:
            # Does not swing, taking 4 seconds
            seconds = seconds - 4
            print('Looks at a pitch, ' + str(seconds) + ' seconds remaining.')

    print(contestants[contestant]['name'] + ' hit ' + str(home_runs) + ' home runs.')
    contestants[contestant]['home_runs'] = home_runs
    input('Press Enter to continue.')
    print("\n")

standings = []
for contestant in contestants:
    entry = [contestants[contestant]['name'], contestants[contestant]['home_runs']]
    standings.append(entry)
standings.sort(key=operator.itemgetter(1), reverse=True)

print("Standings:")
for entry in standings:
    print(entry[0] + ': ' + str(entry[1]))

print('\n')
print('Thanks for playing and Go Cards!')
