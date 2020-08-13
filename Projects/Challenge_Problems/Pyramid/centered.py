#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# for loop

for k in range(1,6):
    for space in range(0,k-6):
        print(" ", end="")
    for l in range(k):
        print("* ", end="")
    print()

# while loop

i = 1
j = 0
while i < 6:
    j = 0
    space = 5 - j
    while space > 0:
        print(" ", end="")
        space -= 1
    while j < i:
        print("* ", end="")
        j += 1
    print()
    i += 1