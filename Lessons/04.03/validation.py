def validation(control_number):
    while True:
        x = input(f"Input your value higher than {control_number}\n")

        try:
            x = int(x)

            if x <= control_number:
                raise RuntimeError(f"The number is less than {control_number}, please try again")

            return x

        except ValueError:
            print("Please enter a valid number")
            continue
        except RuntimeError as err_msg:
            print(err_msg)
            continue

num = validation(40)
print(type(num))