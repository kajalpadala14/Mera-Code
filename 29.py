num = int(input("Enter binary number:-"))
sum = 0
p = 0

while num !=0:
    r = num %10
    sum =sum + (r * 2**p)
    num = num // 10
    p+=1
print(sum)
    
