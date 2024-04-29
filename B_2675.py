# 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식

T = int(input())

for i in range(T):
    R, S = input().split()
    for j in S:
        print(j*int(R), end='')
    print()

'''
내가 쓴 코드
def re(R, S):
    S_list = []*len(S)*R
    for i in S:
        for j in range(R):
            S_list.append(i)
    return ''.join(S_list)

T = int(input())

for i in range(T):
    R = int(input())
    S = input()
    print(re(R, S))
'''