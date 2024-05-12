# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력

N, X = map(int, input().split())
numList = list(map(int, input().split()))

for i in range(N):
    if numList[i] < X:
        print(numList[i], end=" ")