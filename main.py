

# functions go here


def yes_no(question):

    valid = False
    while not valid:
        response = input(question).strip().lower()

        if response == "y" or response == "yes":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes or no")
