score = 0
name = input("What is your name?")
print("Hello there " + name)
question1 = input("What is 2 + 2?")
if(question1 == "4" or question1 == "four" or question1.lower() == "fish") {
    print("Correct!")
    score += 1
} else {
    print("Wrong!")
}