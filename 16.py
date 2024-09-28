num = int(input("Enter the number:-"))
i = 1
while i <= num:
    if num % i == 0:
        print(i,end=" ")
    i+=1
