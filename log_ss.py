import math
import numpy as np

def TripGen(nrow):							# random value generation
	l = 3
	trip = np.random.randint(0, 2**(l-2), (6, nrow))
	trip[5] = (trip[0]+trip[3]) * (trip[1]+trip[4]) - trip[2]
	return trip[0], trip[1], trip[2], trip[3], trip[4], trip[5]

def MulMat(u1, u2, v1, v2, trip):			# element-wise multiplication
	ua = u1 - trip[0] + u2 - trip[3]
	vb = v1 - trip[1] + v2 - trip[4]
	z1 = trip[2] + ua * trip[1] + vb * trip[0]
	z2 = trip[5] + ua * trip[4] + vb * trip[3] + ua * vb
	return z1, z2

def NumMul(u1, u2, v1, v2):					# single number multiplication
	trip = TripGen(1)
	z1, z2 = MulMat(u1, u2, v1, v2, trip)
	return z1, z2

def divss(b1, b2):
	if abs(b1+b2) < 1e-4:
		n1 = 0
		n2 = 0
		count = 0
	else:
		eps = 1e-6
		if abs(b1+b2)>1e5:
			eps = 1e-10
		n1 = 0.5 * eps
		n2 = 0.5 * eps
		d1 = b1 * eps
		d2 = b2 * eps
		count = 0
		while True:
			count += 1
			f1 = 1 - d1
			f2 = 1 - d2
			n1, n2 = NumMul(f1, f2, n1, n2)
			d1, d2 = NumMul(f1, f2, d1, d2)
			if abs(d1+d2-1) < 1e-5:
				break
	return n1, n2

def Log2(b1, b2):
	eps = 1e-4
	a = math.log(math.e, 2)			# 1/ln(2)
	b1 = b1 * a 					# b/ln(2)
	b2 = b2 * a
	x11 = b1 * 0.001
	x12 = b2 * 0.001
	count = 0
	while True:
		x01 = x11
		x02 = x12
		count += 1
		print(count, x01+x02)
		# x1 = x0 - a + b * (math.pow(2, -x0))
		# if x01 > 0:
		temp1 = math.pow(2, -x01)
		# else:
			# temp1 = 1/math.pow(2, x01)
		# if x02 > 0:
		temp2 = math.pow(2, -x02)
		# else:
		# 	temp2 = 1/math.pow(2, x02)
		temp3, temp4 = NumMul(temp1, temp2, temp1, temp2)
		temp3 = (temp3 - temp1*temp1) * 0.5
		temp4 = (temp4 - temp2*temp2) * 0.5
		temp3, temp4 = NumMul(b1, b2, temp3, temp4)
		x11 = x01 + temp3 - 0.5 * a
		x12 = x02 + temp4 - 0.5 * a
		if abs(x11+x12-x01-x02) < eps:
			break
	return count, x11, x12

# n1 = np.random.random() * 10
# n2 = np.random.random() * 10
n1 = 5
n2 = 5
r0 = math.log(n1+n2, 2)
print(r0)

count, r1, r2 = Log2(n1, n2)
print(count, r1+r2)