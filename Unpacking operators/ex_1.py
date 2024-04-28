# Napisz funkcję która przyjmie dowolną liczbę argumentów pozycyjnych
# i zwróci napis powstały z połączenia ich z wykorzystaniem myślnika
# jako łącznika pomiędzy poszczególnymi argumentami.


def connect_strings(*args):
    return "-".join(args)


string_1 = "Hello"
string_2 = "my"
string_3 = "friend"

print(connect_strings(string_1, string_2, string_3, str(5), "12.5"))
