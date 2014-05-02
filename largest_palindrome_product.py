#! /usr/bin/env python
# description : Euler project, problem 4: Largest palindrome product
# author      : vincentliao
# date        : 20140503

from itertools import product

# palindromic number is like 121, 9009, etc.... 
def is_palindromic(number): 
	number_str = str(number)
	half_cnt = len(number_str) / 2
	if number_str[:half_cnt] == number_str[half_cnt:][::-1]:
		return True	
	return False

candidate = []
for num1, num2 in product(range(999, 99, -1), range(999, 99, -1)):
	p = num1 * num2
	if is_palindromic(p) == True:
		candidate.append(p)	

print max(candidate)
