num = int(input())
arr = list(map(int,input().split()))
i = 0
temp = arr[i]
l = 0
while i < num:
    if arr[i] < temp:
        temp = arr[i]
        l = i
    i+=1
print(l)