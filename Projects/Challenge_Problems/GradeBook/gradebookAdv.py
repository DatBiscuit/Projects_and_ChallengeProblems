score = int(input("What score did you recieve: "))

if score >= 90:
    if score >= 97:
        print("A+")
    elif score >= 94:
        print("A")
    else:
        print("A-")
elif score >= 80:
    if score >= 87:
        print("B+")
    elif score >= 84:
        print("B")
    else:
        print("B-")
elif score >= 70:
    if score >= 77:
        print("C+")
    elif score >= 74:
        print("C")
    else:
        print("C-")
elif score >= 60:
    if score >= 67:
        print("D+")
    elif score >= 64:
        print("D")
    else:
        print("D-")
else:
    print("F")