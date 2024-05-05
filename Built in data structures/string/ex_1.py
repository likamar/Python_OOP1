# Napisz funkcję, która wczyta od użytkownika jej/jego imię i nazwisko,
# “wyczyści je” z białych znaków na początku i końcu tekstu,
# a następnie wypisze jakieś zdanie z tymi danymi
# np. “Nazywasz się {first_name} {last_name} - jak miło Cię poznać :)”


def hello_user() -> None:
    user_first_name_input = input("First name: ")
    user_last_name_input = input("Last name: ")
    user_first_name_formatted = user_first_name_input.strip()
    user_last_name_formatted = user_last_name_input.strip()
    print(f"Hello {user_first_name_formatted} {user_last_name_formatted}, it's nice to meet you :)")


def run_ex_1():
    hello_user()


if __name__ == "__main__":
    run_ex_1()