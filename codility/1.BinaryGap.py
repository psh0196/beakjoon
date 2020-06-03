# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
'''
내가 작성한 코드 
문제점: 시간 복잡도가 길어서 큰 숫자는 런타임 에러가 난다. 
def solution(N):
    # write your code in Python 3.6
    binary_num = ''
    while N > 1:
        namege = N%2
        N = N//2
        binary_num = binary_num+str(namege)
        if N == 1:
            binary_num = binary_num+str(N)
            break
    binary_num = binary_num[::-1]
    ## 2진법 표현 완료
    binary_0 = binary_num.split('1')
    if binary_num[0] != '1':
    	del binary_0[0]
    if binary_num[-1] != '1':
    	del binary_0[-1]
    max_0 = 0

    for i in range(len(binary_0)):
    	if len(binary_0[i]) > max_0:
    		max_0 = len(binary_0[i])
    return max_0
# test
# print(solution(32))

'''
# 가장 최적화 된 코드 
def solution(N):
	return len(max(bin(N)[2:].strip('0').strip('1').split('1')))
	# bin은 10진수를 2진수로 바꾸어주는 함수
	# 앞에 0b가 붙으므로 인덱스 2부터 가져온다.
	# 1로 둘러 싸여있지 않은 양 끝의 숫자 0을 strip으로 제거한다.
	# 양끝의 1을 제거한다.
	# 1을 기준으로 문자열을 리스트에 저장한다.
	# 가장 긴 숫자를 return 한다.

# test
# print(solution(529))