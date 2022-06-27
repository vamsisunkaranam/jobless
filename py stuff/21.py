
import random

total = 0
while True:
    available_options = []
    current_option = 1
    while (total + current_option) <= 21 and current_option <= 3:
        available_options.append(current_option)
        current_option += 1

    invalid_input = False
    try:
        user_int = int(input("Your Number? "))
    except Exception:
        invalid_input = True

    if user_int not in available_options or invalid_input:
        print('Enter Valid Input.')
        continue
    total = total + user_int
    if total >= 21:
        print("YOU LOOSE!!!")
        exit()

    available_options = []
    current_option = 1
    while (total + current_option) <= 21 and current_option <= 3:
        available_options.append(current_option)
        current_option += 1

    comp_int = random.randint(min(available_options),max(available_options))
    print('Computer Played:', comp_int)
    total = total + comp_int
    if total>=21:
        print("YOU WIN!!!")
        exit()
    print("Total:", total, "\n")