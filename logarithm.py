# Compute log(n) using recursion
# Copyright by Smitha Dinesh Semwal
import math

def log2n(n):
	return 1 + log2n(n/2) if (n > 1) else 0


def div(b):
	eps = 1e-5
	n = eps
	d = b * eps
	count = 0
	while True:
		count += 1
		f = 2 - d
		n = n * f
		d = d * f
		if abs(d-1) < eps:
			break
	return count, n

def log2me(b):
	eps = 1e-5
	a = math.log(math.e, 2)			# 1/ln(2)
	b = b * a 						# b/ln(2)
	x1 = b * 0.001
	count = 0
	while True:
		x0 = x1
		count += 1
		print(count, x0)
		x1 = x0 - a + b * (math.pow(2, -x0))
		if abs(x1-x0) < eps:
			break
	return count, x1

n = 0.001
r0 = math.log(n, 2)
print(r0)

r1 = log2me(n)
print(r1)

