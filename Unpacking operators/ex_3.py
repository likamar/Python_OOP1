# Wygeneruj dwie listy zawierające losowe liczby całkowite
# i połącz je w jedną wykorzystując operator *.
import random


def generate_random_integers_list():
    random_integers_list = []
    for _ in range(0, random.randint(1, 10)):
        random_integers_list.append(random.randint(1, 100))
    return random_integers_list


def run_homework():
    integers_1 = generate_random_integers_list()
    integers_2 = generate_random_integers_list()

    integers_combined = [*integers_1, *integers_2]

    print("integers_1: ", integers_1)
    print("integers_2: ", integers_2)
    print("integers_combined: ", integers_combined)


if __name__ == '__main__':
    run_homework()
