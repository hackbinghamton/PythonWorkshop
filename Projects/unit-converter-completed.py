def ask_question():
    # get user input
    conversion = input(
        "Enter a choice followed by the amount which you would like to convert: ")
    conversion_list = conversion.split()
    # check if input is valid
    if len(conversion_list) == 0:
        print("Please enter a choice!")
        return True
    if not is_integer(conversion_list):
        print("Please enter an integer choice and amount!")
        return True
    # since all elements are valid integers, convert them all
    conversion_list = [int(i) for i in conversion_list]
    choice = conversion_list[0]
    # check if user wants to exit
    if choice == -1:
        return False
    amount = conversion_list[1]
    # calculate value if choice is in allowed range
    if choice > 0 and choice < 7:
        answer = convert(choice, amount)
        print(f"Answer: {answer}")
    else:
        print("Please enter a valid integer choice (between 1 and 6)")
    return True


def convert(choice, amount):
    if choice == 1:
        return (amount * (9/5)) + 32
    elif choice == 2:
        return (amount - 32) * (5/9)
    elif choice == 3:
        return (amount / 2.205)
    elif choice == 4:
        return (amount * 2.205)
    elif choice == 5:
        return (amount / 2.54)
    elif choice == 6:
        return (amount * 2.54)


def is_integer(string_list):
    """checks if all elements in list are integers"""
    for i in string_list:
        try:
            int(i)
        except ValueError:
            return False
    return True


def main():
    prompt = """
            ==============
            UNIT CONVERTER
            ==============

            What would you like to convert?

            1. Celsius to Fahrenheit
            2. Fahrenheit to Celsius
            3. Pounds (lb) to Kilograms (kg)
            4. Kilograms (kg) to Pounds (lb)
            5. Centimeters (cm) to Inches (in)
            6. Inches (in) to Centimeters (cm)

            (-1 to quit program)
            """
    print(prompt)
    # loop till user quits program
    while ask_question():
        pass
    print("\nThanks for using my unit conversion program!")


main()
