# Używając list comprehensions wygeneruj listy zawierające liczby od 1 do 30 podzielne kolejno przez 3 oraz przez 5.
# To znaczy, że na pierwszej liście powinny znaleźć się liczby od 1 do 30 podzielne przez 3,
# a na drugiej liście liczby od 1 do 30 podzielne przez 5.
# Następnie, połącz obie listy w jedną i wypisz wynik.


def run_ex_1():
    integers_divided_by_3 = [integer for integer in range(1, 31) if integer % 3 == 0]
    integers_divided_by_5 = [integer for integer in range(1, 31) if integer % 5 == 0]
    merged_integers = integers_divided_by_3 + integers_divided_by_5

    print(integers_divided_by_3)
    print(integers_divided_by_5)
    print(merged_integers)


if __name__ == "__main__":
    run_ex_1()