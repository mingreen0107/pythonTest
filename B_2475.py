N = input().split()
sum = 0

for i in N[:]:
    i = int(i)
    sum += i*i

print(sum%10)