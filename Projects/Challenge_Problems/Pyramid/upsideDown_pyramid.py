# *****
# ****
# ***
# **
# *

# for loop
for k in range(1,6):
    for l in range(k,6):
        print("*", end="")
    print()

# while loop
i = 5
j = 0
while i > 0:
    j = i
    while j > 0:
        print("*", end="")
        j -= 1
    print()
    i -= 1