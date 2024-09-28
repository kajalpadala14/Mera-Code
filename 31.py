num = int(input("Enter the number:-"))
count = 0
s = 1
while s <= num:
    if num % s == 0:
        count+=1
    s+=1
    
if count != 2:
    print("no")
else:
    print("yes")