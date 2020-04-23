import math
cycle = input()
result = []
for i in range(int(cycle)):
	x1, y1, r1, x2, y2, r2 = input().split(' ')
	x1, y1, r1, x2, y2, r2 = int(x1), int(y1), int(r1), int(x2), int(y2), int(r2)
	dist = math.sqrt(pow(x1-x2,2) + pow(y1-y2,2))
	# 중심이 같은경우
	if dist == 0 and r1 == r2:
		result.append(-1)
	elif dist == 0 and r1 != r2:
		result.append(0)
	# 중심이 다른 경우 
	else:
		if dist < r1+r2 and dist > abs(r1-r2):
			result.append(2)
		elif dist == r1+r2 or dist == abs(r1-r2):
			result.append(1)
		elif dist > r1+r2 or dist < abs(r1-r2):
			result.append(0)
for output in result:
	print(output)
