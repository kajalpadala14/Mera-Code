num = int(input())
arr = list(map(int,input().split()))
i = 0
found = False
while i <num:
    if arr[i] < 0:
        print("Yes")
        found = True 
        break
    i+=1
if not found:
    print("No")