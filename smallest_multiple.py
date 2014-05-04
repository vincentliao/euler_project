#! /usr/bin/env python
# encoding    : utf-8
# author      : vincentliao
# date        : 20140503 
# description : Euler Project, problem 5: smallest mulitple
#             : this programm have to spend 9 second to calculate. 

next_interval = 20
number = 20

divsor = [20, 19, 18, 17, 16, 14, 13, 11] # only check these divsor between 1 and 20.

while True:
	if all(number % d == 0 for d in divsor):
		print number
		break
	number += next_interval

