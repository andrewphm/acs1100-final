class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"


def load_user_data(file_name):
    """
    Takes a data file and formats the data into a list of users.
    Parameters: file name (string).
    Returns: list containing users formatted into dictionaries
    """

    with open(file_name, "r") as infile:
        file_lines = infile.readlines()
        users = []
        for line in file_lines:
            line = line.strip()
            line = line.split(",")
            line = {
                "username": line[0],
                "password": line[1],
                "full_name": line[2],
                "balance": line[3],
            }
            users.append(line)

        return users


def login(username, password, users):
    """
    Prompts user for username and password and checks if they match.
    Paramters: username (string) and password (string)
    Returns: if login is found returns user else returns False
    """
    for user in users:
        if username == user["username"]:
            if user["password"] == password:
                return user

    return False


def display_user_info(user):
    """
    Displays information about a user in formatted strings.
    Parameters: user (dictionary).
    Returns: None
    """

    full_name = user["full_name"]
    balance = user["balance"]
    print(f"{bcolors.OKBLUE}Full Name: {full_name}")
    print(f"Balance: ${float(balance)}{bcolors.ENDC}")


def prompt_user(message):
    """
    Prompt user for input.
    Parameters: message (string)
    Returns: user response (string)
    """
    user_response = input(message)
    return user_response


def online_bank():
    """
    Function that prompts user for username and password and
    if they match it will display information about the user.
    """
    users = load_user_data("data.txt")

    while True:
        username = prompt_user(f"{bcolors.HEADER}Enter Username: {bcolors.ENDC}")
        password = prompt_user(f"{bcolors.HEADER}Enter password: {bcolors.ENDC}")

        user = login(username, password, users)

        if user:
            display_user_info(user)
            break
        else:
            try_again = prompt_user(
                f"{bcolors.FAIL}Username and password not found. Would you like to try again? {bcolors.WARNING}(y/n): {bcolors.ENDC}"
            )
            if try_again == "n":
                break


online_bank()
