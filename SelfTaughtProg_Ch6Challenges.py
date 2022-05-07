# 'The Self-taught Programmer' Ch 6: String Manipulation Challenges
# C1: Print every character in the string "Camus"
print("Challenge 1")
author = "Camus"
for i in author:
    print(i)

# C2: Write a program that collects two strings from a user, inserts
# them into the string "Yesterday I wrote a [response_one]. I sent it
# to [response_two]!" and prints a new string.
print("\nChallenge 2")
documentType = input("Input a document type (e.g. book): ")
personName = input("Input a person to send document to: ")
myString = "Yesterday I wrote a {}. I sent it to {}!".format(documentType,personName)
print(myString)

# C3: Use a method to make the string "aldous Huxley was born in 1894."
# gramatically correct by capitalizing the first letter in the sentence.
print("\nChallenge 3")
str1 = "aldous Huxley was born in 1894."
str2 = str1.split(" ")
str2[0] = str2[0].capitalize()
str3 = " ".join(str2)
print(str3)

# C4: Take the string "Where now? Who now? When now?" and call a method
# that returns a list that looks like: ["Where now?", "Who now?", "When now?"]
print("\nChallenge 4")
myStr = "Where now? Who now? When now?"
myStrList = myStr.split("? ")
myStrList[0] = myStrList[0] + "?"
myStrList[1] = myStrList[1] + "?"
print(myStrList)

# C5: Take the list ["The", "fox", "jumped", "over", "the", "fence", "."]
# and turn it into a grammatically correct string. There should be a space
# between each word, but no space between the word fence and the period that
# follows it.
print("\nChallenge 5")
wordList = ["The", "fox", "jumped", "over", "the", "fence", "."]
newWordList = " ".join(wordList[0:len(wordList)-1])
newWordList = newWordList + "."
print(newWordList)

# C6: Replace every instance of "s" in "A screaming comes across the sky."
# with a dollar sign ($)
print("\nChallenge 6")
print("A screaming comes across the sky.".replace("s","$"))

# C7: Use a method to find the first index of the character "m" in the string
# "Hemingway"
print("\nChallenge 7")
print("The 1st index of 'm' in \"Hemingway\" is " + str("Hemingway".index("m")))

# C8: Print a string containing quotes
print("\nChallenge 8")
print("Hello \"super cool\" world!")

# C9: Create the string "three three three" using concatenation, and then again
# using multiplication
str1 = "three " + "three " + "three "
str2 = "three " * 3
print(str1)
print(str2)

# C10: Slice the string "It was a bright cold day in April, and the clocks were
# striking thirteen." to only include the characters before the comma.
print("\nChallenge 10")
strList = "It was a bright cold day in April, and the clocks were striking thirteen.".split(",")
print(strList[0])




