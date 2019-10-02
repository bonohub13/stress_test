#!/usr/bin/env python3
from scripts.stress_test import PrimeNumberGenerator

if __name__ == "__main__":
    while True:
        print("Select level of stress:[1 ~ 10 (4 by default)]")
        level = input('input level(\"enter\" for default): ')
        if level == "":
            break
        else:
            try:
                level = int(level)
                if level > 0 and level < 11:
                    break
                else:
                    print('Not an acceptable number, enter again')
            except ValueError:
                print('Input not an number, input value again')
    if type(level) is int:
        stress_test = PrimeNumberGenerator(max_size=level)
    else:
        stress_test = PrimeNumberGenerator()
    stress_test.prime_num_gen()