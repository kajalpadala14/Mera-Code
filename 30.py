num = int(input("Enter a decimal number:-"))
binary_num =""

while num >0:
    r = num % 2
    binary_num=str(r)+binary_num
    num = num // 2
print(binary_num)