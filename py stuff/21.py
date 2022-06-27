import random

def get_avaiable_option(total):
    available_options = []
    current_option = 1
    while (total + current_option) <= 21 and current_option <= 3:
        available_options.append(current_option)
        current_option += 1
    return available_options

total = 0
while True:
    invalid_input = False
    try:
        user_int = int(input("Your Number? "))
    except Exception:
        invalid_input = True

    if user_int not in get_avaiable_option(total) or invalid_input:
        print('Enter Valid Input.')
        continue
    total = total + user_int
    if total >= 21:
        print("YOU LOOSE!!!")
        exit()

    available_options = get_avaiable_option(total)

    comp_int = random.randint(min(available_options),max(available_options))
    print('Computer Played:', comp_int)
    total = total + comp_int
    if total>=21:
        print("YOU WIN!!!")
        exit()
    print("Total:", total, "\n")