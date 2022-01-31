while True:
    user_value = input("input your time value as hh:mm\n")

    if len(user_value) != 5:
        print("your input is incorrect, it's too long or too short")
        continue

    #if ':' not in user_value:
    if user_value[2] != ':':
        print("your input is incorrect, it does not contain : separator")
        continue

    values = user_value.split(':')
    hours, minutes = values[0], values[1]

    if not (hours.isdigit() and minutes.isdigit()):
        print("your input is incorrect, it does not contain proper digits")
        continue

    hours, minutes = int(hours), int(minutes)

    if hours > 24 or minutes > 60:
        print("your input is incorrect, it has wrong hours or minutes values")
        continue

    break

print("our main logic")