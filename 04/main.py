import parser
import guard


my_parser = parser.Parser('./input.txt')

sleepy_boi = None
regular_boi = None
slept = 0
times_slept = None

for key, currentguard in my_parser.guard_dict.items():
    if currentguard.downtime > slept:
        sleepy_boi = currentguard
        slept = currentguard.downtime
    # quel garde est le plus souvent endormi à la même minute?
    if times_slept is None or currentguard.get_most_slept_minute()[1] > times_slept:
        regular_boi = currentguard
        times_slept = currentguard.get_most_slept_minute()[1]

most_slept_minute = sleepy_boi.get_most_slept_minute()
regular_slept_minute = regular_boi.get_most_slept_minute()

print(sleepy_boi.guard_id, " x ", most_slept_minute[0], " = ", int(sleepy_boi.guard_id) * most_slept_minute[0])
print(regular_boi.guard_id, " x ", regular_slept_minute[0], " = ", int(regular_boi.guard_id) * regular_slept_minute[0])
