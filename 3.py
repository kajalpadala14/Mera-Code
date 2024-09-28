age = int(input("Enter the age: "))

if age >= 20 and age <= 65:
    print("Adult")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 3 and age <= 12:
    print("Child")
elif age >= 0 and age <= 2:
    print("Infant")
elif age > 65:
    print("Senior")
else:
    print("Invalid age entered")
