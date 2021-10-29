# Get beat per minute
bpm = int(input("BPM: "))
# Get age
age = int(input("age(+18): "))

# Check if user is at least 18 years old
if age < 18:
    print("Must be at least 18 years old")
    exit()

# Get sex
sex = ""
while not (sex == "m" or sex == 'f'):
    sex = input("sex(m ou f): ")

# Calculate bpm for males
if sex == 'm':
    if age <= 25:
        if bpm < 70:
            print("Lower")
        elif bpm > 73:
            print("Higher")
        else:
            print("Good")

    elif age <= 35:
        if bpm < 71:
            print("Lower")
        elif bpm > 74:
            print("Higher")
        else:
            print("Good")

    elif age <= 45:
        if bpm < 71:
            print("Lower")
        elif bpm > 75:
            print("Higher")
        else:
            print("Good")

    elif age <= 55:
        if bpm < 72:
            print("Lower")
        elif bpm > 76:
            print("Higher")
        else:
            print("Good")

    elif age <= 65:
        if bpm < 72:
            print("Lower")
        elif bpm > 75:
            print("Higher")
        else:
            print("Good")

    else:
        if bpm < 70:
            print("Lower")
        elif bpm > 73:
            print("Higher")
        else:
            print("Good")

# Calculate bpm for females
elif sex == 'f':
    if age <= 25:
        if bpm < 74:
            print("Lower")
        elif bpm > 78:
            print("Higher")
        else:
            print("Good")

    elif age <= 35:
        if bpm < 73:
            print("Lower")
        elif bpm > 76:
            print("Higher")
        else:
            print("Good")

    elif age <= 45:
        if bpm < 74:
            print("Lower")
        elif bpm > 78:
            print("Higher")
        else:
            print("Good")

    elif age <= 55:
        if bpm < 74:
            print("Lower")
        elif bpm > 77:
            print("Higher")
        else:
            print("Good")

    elif age <= 65:
        if bpm < 74:
            print("Lower")
        elif bpm > 77:
            print("Higher")
        else:
            print("Good")

    else:
        if bpm < 73:
            print("Lower")
        elif bpm > 76:
            print("Higher")
        else:
            print("Good")