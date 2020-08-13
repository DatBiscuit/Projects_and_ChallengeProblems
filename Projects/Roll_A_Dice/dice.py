import random
import time

def six_sided():
    min = 1
    max = 6
    print("Rolling dice...")
    time.sleep(2)
    return random.randint(min,max)

def four_sided():
    min = 1
    max = 4
    print("Rolling dice...")
    time.sleep(2)
    return random.randint(min,max)

def eight_sided():
    min = 1
    max = 8
    print("Rolling dice...")
    time.sleep(2)
    return random.randint(min,max)

def ten_sided():
    min = 1
    max = 10
    print("Rolling dice...")
    time.sleep(2)
    return random.randint(min,max)

def twelve_sided():
    min = 1
    max = 12
    print("Rolling dice...")
    time.sleep(2)
    return random.randint(min,max)

def twenty_sided():
    min = 1
    max = 20
    print("Rolling dice...")
    time.sleep(2)
    return random.randint(min,max)

print(four_sided())