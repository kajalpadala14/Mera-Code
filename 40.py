n = int(input())
arr= list(map(int, input().split())) 
i =0
while i < n:
    if arr[i]%2==0:
        print("Even")
    else:
        print("Odd")
    i+=1