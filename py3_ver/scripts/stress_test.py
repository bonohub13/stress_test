#!/usr/bin/env python3
from time import time
from random import randint

class PrimeNumberGenerator:
    def __init__(self, max_size=4):
        self.prime_num_list = []
        self.init_prime_num = 2
        self.max_size = 10**max_size

    def prime_num_gen(self):
        time_a = time()
        prime_num = self.init_prime_num
        self.prime_num_list.append(prime_num)
        while len(self.prime_num_list) < self.max_size:
            prime_num += 1
            n = 0
            for i in self.prime_num_list:
                if prime_num%i != 0:
                    n += 1
            if n == len(self.prime_num_list):
                self.prime_num_list.append(prime_num)
        time_b = time()
        print("elapsed time: {}[s]".format(time_b-time_a))

class RandomNumberGenerator:
    def __init__(self, max_size=7):
        self.max_size = 10**(max_size)
        self.random_num_list = [0, 1]

    def rand_num_gen(self):
        time_a = time()
        while len(self.random_num_list) < self.max_size:
            rand_num = self.random_num_list[-1]+self.random_num_list[-2]
            if rand_num > 16:
                rand_num %= randint(1, 16)
            self.random_num_list.append(rand_num)
        time_b = time()
        print("elapsed time: {}[s]".format(time_b-time_a))

if __name__ == "__main__":
    """
    test_check_prime_num = PrimeNumberGenerator()
    test_check_prime_num.prime_num_gen()
    test_result = test_check_prime_num.prime_num_list
    print("amount of prime numbers: {}".format(len(test_result)))
    print("{} ... {}".format(test_result[:5], test_result[-5:]))
    """
    test_check_rand_num = RandomNumberGenerator()
    test_check_rand_num.rand_num_gen()
    print("generated numbers: {} ... {}".format(test_check_rand_num.random_num_list[:5], test_check_rand_num.random_num_list[-5:]))
