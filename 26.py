num = int(input("Enter the number"))
dbt = 0
while num !=0:
    r = num % 10
    dbt = dbt*10+r
    num = num // 10
print(dbt)

