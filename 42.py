num = int(input())
k = int(input())
arr = list(map(int,input().split()))
i=0
count=0
while i < num:
    if arr[i]== k:
        count+=1
    i+=1
print(count)
    

