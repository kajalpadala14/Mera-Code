num = int(input())
arr = list(map(int,input().split()))
i = 0
sum = 0
while i < num:
    sum = sum+arr[i]
    i+=1
print(sum)
    
