# Napisz funkcję, która przyjmie dowolną liczbę argumentów nazwanych
# i wypisze sposób w jaki została wywołana, tzn. poszczególne nazwy argumentów,
# znak równa się i wartość (np. first_name=Mikołaj, age=134).


def print_self(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value, sep="")


print_self(first_name="Marcin", surname="Lika", age=35, email="marcin@lika.com")
