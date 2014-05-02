#! /usr/bin/env python
# description : Euler project, problem 3: Largest prime factor
# author      : vincentliao
# date        : 20140502

import sys
import math

number = sys.argv[1] if len(sys.argv) > 1 else 600851475143
factors = sorted(set([x for x in [item for sublist in [[d, number/d] for d in range(1, int(math.sqrt(number))+1) if number%d == 0 ] for item in sublist] if x < number]))

def is_prime(number):
	for i in range(2, int(number**0.5+1)):
		if number % i == 0:
			return False
	return True

print max(filter(is_prime, factors))
