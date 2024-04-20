# досрок егэ. на кегэ №15329
import sys
sys.set_int_max_str_digits(100000)
counter = 0
num = 3 * 2187 ** 2020 + 3 * 729 ** 2021 - 2 * 81 ** 2022 + 27**2023 - 4*3**2024 - 2029
while num > 0:
    if num % 27>9:
        counter += 1
    num //= 27
print(counter)