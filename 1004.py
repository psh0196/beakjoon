import sys

def distance(x, y, r_x, r_y):
	dist = ((x-r_x)**2+(y-r_y)**2)**0.5
	return dist

test_case = int(input())
while test_case > 0:
	x1, y1, x2, y2 = input().split(" ")
	x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
	cycle_num = int(input())
	inside_1 = 0
	inside_2 = 0
	while cycle_num > 0:
		r_x, r_y, r_length = input().split(" ")
		r_x, r_y, r_length = int(r_x), int(r_y), int(r_length)
		if distance(x1,y1,r_x,r_y) < r_length and distance(x2,y2,r_x,r_y) < r_length:
			cycle_num = cycle_num-1
			continue
		elif distance(x1,y1,r_x,r_y) == r_length or distance(x2,y2,r_x,r_y) == r_length:
			sys.exit()
		elif distance(x1,y1,r_x,r_y) < r_length:
			inside_1 = inside_1+1
		elif distance(x2,y2,r_x,r_y) < r_length:
			inside_2 = inside_2+1

		cycle_num = cycle_num-1
	print(str(inside_1+inside_2))

	test_case = test_case-1