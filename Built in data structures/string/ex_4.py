# Zmodyfikuj rozwiązanie zadania pierwszego, tak aby do wypisywania wykorzystać metodę format.

def hello_user() -> None:
    user_first_name_input = input("First name: ")
    user_last_name_input = input("Last name: ")
    user_first_name_formatted = user_first_name_input.strip()
    user_last_name_formatted = user_last_name_input.strip()
    print("Hello {first_name} {last_name}, it's nice to meet you :)".format(first_name=user_first_name_formatted, last_name=user_last_name_formatted))


def run_ex_1():
    hello_user()


if __name__ == "__main__":
    run_ex_1()