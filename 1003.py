import sys

test_case = int(input())

cnt_0 = [1,0,1]
cnt_1 = [0,1,1]

for test_num in range(test_case):
	n = int(input())
	if n > 40 or n < 0:
		sys.exit()
	elif n > len(cnt_0)-1:
		size = len(cnt_0)-1
		while n > size:
			cnt_0.append(int(cnt_0[-1])+int(cnt_0[-2]))
			cnt_1.append(int(cnt_1[-1])+int(cnt_1[-2]))
			size = size+1
		print(str(cnt_0[n])+" "+str(cnt_1[n]))
	else:
		print(str(cnt_0[n])+" "+str(cnt_1[n]))


		