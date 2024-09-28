num = int(input())
arr = list(map(int,input().split()))
ascending = True
i = 1
while i < len(arr):
    if arr[i-1]> arr[i]:
        ascending = False
        break
    i += 1
if ascending:
    print("Yes")
else:
    print("No")




