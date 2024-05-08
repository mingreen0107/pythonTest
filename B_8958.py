# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점

def count(S):
    count = 0
    S = list(S)

    for i in S:
        if (i=='O'):
            count += 1

    print(count)

N = int(input())

for i in range(N):
    S = input()
    count(S)