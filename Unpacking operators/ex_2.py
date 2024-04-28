# Napisz funkcję, która przyjmie dowolną liczbę argumentów nazwanych
# i wypisze sposób w jaki została wywołana, tzn. poszczególne nazwy argumentów,
# znak równa się i wartość (np. first_name=Mikołaj, age=134).


def print_call_str(**kwargs):
    call_str= "print_call_str("
    for key, value in kwargs.items():
        call_str += f"{key}={value},"
    call_str = call_str[:-1] + ")"
    print(call_str)


print_call_str(first_name="Marcin", surname="Lika", age=35, email="marcin@lika.com")
