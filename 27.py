num1 = int(input("Enter the number:"))
num2 = int(input("Enter the number:"))
if num1 > num2:
    max = num1
    min = num2
else:
    max = num2
    min = num1
r = max % min
while r !=0:
    max = min
    min = r
    r = max % min
print("HCF ",min)
