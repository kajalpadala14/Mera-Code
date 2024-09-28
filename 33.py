num = int(input("Enter the number:-"))
count =0
orgl_num=num
sum = 0

while num !=0:
    r = num % 10
    count+=1
    num = num // 10
num = orgl_num

while num !=0:
    r = num % 10
    sum = sum +(r**count)
    num = num // 10
    
if sum == orgl_num:
    print("yes")
else:
    print("No")
