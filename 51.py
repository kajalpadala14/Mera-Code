num = int(input("Enter the number:-"))
arr = list(map(int,input().split()))
target = int(input("Enter the target number:-"))
i = 0
found = False
while i < num:
    if arr[i] == target:
        print("Yes")
        found = True
        break
    i += 1
if not found:
  print("No")