num = int(input())
arr = list(map(int,input().split()))
i = 0
sum =0
count=0
while i < num:
    sum +=arr[i]
    count+=1
    i+=1
print(sum/count)


