# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력

listNum, maxNum = map(int, input().split())
list = []

for i in range(listNum):
    list.append(int(input().split()))

for i in list:
    if (i < maxNum):
        print(i)