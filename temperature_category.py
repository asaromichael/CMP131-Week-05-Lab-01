temp = float(input("Please enter the temperature in fahrenheit"))

if (temp < 50):
    print("Your temperature: ", temp, "F is cold.")
elif (temp < 80):
    print("Your temperature: ", temp, "F is warm.")
else:
    print("Your temperature: ", temp, "F is hot.")