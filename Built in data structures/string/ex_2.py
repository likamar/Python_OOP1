# Napisz funkcję generującą losowy identyfikator. Identyfikator powinien być w formacie 00001,
# tzn. zawsze o długości pięciu znaków, dopełniony z lewej strony odpowiednią liczbą zer.

import random


def generate_id():
    random_id = random.randint(1, 99999)
    return str(random_id).zfill(5)


def run_ex2():
    print("ID:", generate_id())


if __name__ == "__main__":
    run_ex2()
