num = int(input())
arr = list(map(int,input().split()))
i =0
sum = 0
while i < num:
    if arr[i] == 0:
        break
    else:
        sum+=arr[i]
    i+=1
print(sum)