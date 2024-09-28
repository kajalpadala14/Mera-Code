num = int(input())
count=0
i = 2
while count<= num:
    divisor_count=0
    j = 1
    while j <= i:
        if i % j == 0:
            divisor_count+=1
        j+=1
    if divisor_count == 2:
        print(i,end=" ")
        count+=1
    i+=1     