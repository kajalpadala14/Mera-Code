temp = int(input("Enter the temperature:"))
if temp >= 30:
    print("It's hot.Let's go swimming!")
elif temp > 20 and temp >30:
    print("Perfect for a picnic.")
elif temp >10 and temp < 19:
    print("Maybe wear a jacket?")
else:
    print("Too cold! Best to stay indoors.")