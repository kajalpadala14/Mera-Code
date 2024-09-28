num = int(input())
arr = list (map(int,input().split()))
i = 0
mul = 1
while i < num:
    mul *=arr[i]
    i+=1
print(mul)

