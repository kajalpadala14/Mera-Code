score = int(input("Enter the student score:"))

if score >=90 and score <= 100:
    print("A")
elif score >=80 and score <= 89:
    print("B")
elif score >=70 and score <=79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
elif score <60:
    print("F")
else:
      print("Invalid score, please enter a score between 0 and 100.")