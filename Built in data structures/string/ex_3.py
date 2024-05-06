# Wczytaj od użytkownika jej/jego ulubione kolory (jako jeden napis, np. rozdzielony przecinkiem).
# Sprawdź, czy znajduje się wśród nich niebieski, a następnie wypisz odpowiedni komunikat.

def input_favourite_colors() -> str:
    colors_input = input("Your favourite color: ")
    return colors_input.lower()


def is_blue_a_fav_color(fav_colors: str) -> None:
    if "blue" in fav_colors:
        print("You like blue color.")
    else:
        print("Blue isn't your favourite color.")


def run_ex_3():
    user_fav_colors = input_favourite_colors()
    is_blue_a_fav_color(user_fav_colors)


if __name__ == "__main__":
    run_ex_3()
