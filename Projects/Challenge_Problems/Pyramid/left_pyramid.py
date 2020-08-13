# *
# **
# ***
# ****
# *****


# for loop version
star = "*"

for i in range(0,5):
    print(star)
    star += "*"

# OR

for k in range(1,6):
    for l in range(k):
        print("*", end="")
    print()

# while loop version
star = "*"

i = 0
while i < 5:
    print(star)
    star += "*"
    i += 1

# OR

i = 1
j = 0
while i < 6:
    j = 0
    while j < i:
        print("*", end="")
        j += 1
    print()
    i += 1