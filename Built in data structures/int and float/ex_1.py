# Wylosuj 6 liczb typu float z przedziału od -20 do 20 oraz 3 liczby całkowite z przedziału od 1 do 10.
# Następnie na pierwszych trzech liczbach typu float zastosuj zaokrąglanie (kolejno round, ceil oraz floor).
# Kolejne trzy liczby typu float podnieś do potęgi o wartości odpowiednio pierwszej,
# drugiej i trzeciej wylosowanej liczby całkowitej.

import random
import math


def print_formatted_list_of_numbers(numbers: list) -> None:
    for index, number in enumerate(numbers):
        print("float_number_" + str(index + 1) + ":", number)


def run_ex_1():
    print("ex_1\n")

    float_numbers = []
    for _ in range(6):
        float_numbers.append(random.uniform(-20, 20))

    print_formatted_list_of_numbers(float_numbers)

    print()

    integers = []
    for _ in range(3):
        integers.append(random.randint(1, 10))

    print_formatted_list_of_numbers(integers)

    print()

    float_1_round = round(float_numbers[0])
    float_2_ceil = math.ceil(float_numbers[1])
    float_3_floor = math.floor(float_numbers[2])

    print("float_1_round: ", float_1_round)
    print("float_2_ceil: ", float_2_ceil)
    print("float_3_floor: ", float_3_floor, "\n")

    float_4_pow = (float_numbers[3] ** integers[0])
    float_5_pow = pow(float_numbers[4], integers[1])
    float_6_pow = math.pow(float_numbers[5], integers[2])

    print("float_4_pow: ", float_4_pow)
    print("float_5_pow: ", float_5_pow)
    print("float_6_pow: ", float_6_pow)


if __name__ == "__main__":
    run_ex_1()
