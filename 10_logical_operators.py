#10 LOGICAL OPERATORS: evaluate multiple conditions (or, and, not)
#                      or = at least one condition must be True.
#                      and= both conditions must be True.
#                      not= inverts the condition (not False, not True)

''' or'''
temp = 25
is_sunny = False
if temp >= 30 or is_sunny:
    print("the outdoor activity is cancelled.")
else:
    print("the outdoor activity is still ongoing.")

''' and '''
temp = 38
is_sunny = True
if temp >= 30 and is_sunny:
    print("It's raining.")
else:
    print("It's not raining.")

''' not '''
temp = 38
is_sunny = True
if temp >= 30 and not is_sunny:
    print("It's raining.")
else:
    print("It's not raining.")



