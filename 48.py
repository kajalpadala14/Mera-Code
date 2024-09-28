num = int(input())
arr = list(map(int,input().split()))
i = 0
sum = 0
temp = sum
while i < num-1:
    sum = arr[i] + arr[i+1]
    if temp<sum:
        temp = sum
    i+=1
print(temp)
    