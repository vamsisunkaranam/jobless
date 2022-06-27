
import random

total = 0
while True:
    invalid_input = False
    try:
        user_int = int(input("\nYour Number?\n"))
    except Exception:
        invalid_input = True

    if user_int not in [1, 2, 3] or invalid_input:
        print('Enter Valid Input.')
        continue
    total = total + user_int
    if total>=21:
        print("YOU LOOSE!!!")
        exit()

    comp_int = random.randint(1,3)
    print('\nComputer Played.\n ', comp_int)
    total = total + comp_int
    if total>=21:
        print("YOU WIN!!!")
        exit()