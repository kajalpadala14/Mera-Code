arr = list(map(int, input().split()))  
found = False
for i in range(len(arr)):
    num = arr[i]
    sqrt = int(num ** 0.5)
    if sqrt * sqrt == num: 
        print(num)
        found = True
        break

if not found:
    print("No")
