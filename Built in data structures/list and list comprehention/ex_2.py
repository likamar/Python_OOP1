# Wczytaj od użytkownika listę ulubionych sportów, a następnie stosując slicing wypisz co drugi,
# pomijając pierwszy sport z listy.


def run_ex_2():
    favourite_sports = input("Your favourite sports: ").split(',')
    print(favourite_sports)
    print(favourite_sports[1::2])


if __name__ == "__main__":
    run_ex_2()
