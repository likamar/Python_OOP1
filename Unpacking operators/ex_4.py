# Utwórz dwa słowniki i połącz je w jeden wykorzystując operator **.
# Tak otrzymany słownik “rozpakuj” wywołując funkcję z zadania drugiego.

from ex_2 import print_call_str


def run_homework():
    dict_1 = {
        "first_name": "Marcin",
        "last_name": "Lika"
    }

    dict_2 = {
        "age": 30,
        "email": "marcin@lika.com"
    }

    dict_combined = {**dict_1, **dict_2}
    print(dict_combined)
    print_call_str(**dict_combined)


if __name__ == "__main__":
    run_homework()
