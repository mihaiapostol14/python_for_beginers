from colorama import Fore

user_name = input(f"{Fore.GREEN}Enter username: ")


def generator(username):
    random_name = username[::-1]
    print(f"{Fore.GREEN}{random_name}_bot")


generator(username=user_name)
