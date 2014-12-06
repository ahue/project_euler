# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math

def solve():

	z = float(600851475143)
	eps = 1e-5

	if 3**round(math.log(z, 3)) == z:
		return z

	comps = list()

	k = 1
	while True:
		cand = 4*k + 1
		quot = z/cand
		if(quot - int(quot) < eps):



def greatest_div(x):




def is_prime():