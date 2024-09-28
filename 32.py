num = int(input("Enter the number:-"))
orl_num = num
sum = 0
count =1

while count < num:
    if num % count ==0:
        sum+=count
    count+=1
if orl_num == sum:
    print("Yes")
else:
    print("No")