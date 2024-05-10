# 가장 짧은 거리에 있는 방, 걷는 거리가 같을 때에는 아래층의 방

def roomnum(T):
    for i in range(T):
        H, W, N = map(int, input().split())

        floor = N % H * 100
        number = N // H + 1

        if (N % H == 0):
            floor = H * 100
            number = N // H

        print(floor + number)

T = int(input())

roomnum(T)

'''
참고할 코드

from sys import stdin
input = stdin.readline

T = int(input())
for t in range(T):
    H, W, N = map(int, input().split())

    print(((N-1)%H+1)*100+((N-1)//H+1))
'''