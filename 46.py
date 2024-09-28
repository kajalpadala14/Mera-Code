num = int(input())
arr = list(map(int,input().split()))
i = 0 
temp = arr[i]
while i < num:
    if arr[i]<temp:
        temp = arr[i]
    i+=1
print(temp)

