# 'The Self-taught Programmer' Ch 7: Loops Challenges
# Bradley Canty, 2022-04-04

# C1: Print each item in the following list: ["The Walking Dead", "Entourage",
# "The Sopranos", "The Vampire Diraries"]
print("Challenge 1")
myList = ["The Walking Dead","The Sopranos","The Vampire Diaries"]

i = 0
for show in myList:
    print(myList[i])
    i += 1

# C2: Print all the numbers from 25 to 50
print("Challenge 2")
for i in range(25,51):
    print(i)

# C3: Print each item in the list from the first challenge and their indxes
print("Challenge 3")
for i, show in enumerate(myList):
    myStr = "Index: {}, Show: {}".format(i, show)
    print(myStr)

# C4: Write a program with an infinite loop (with the option to type q to quit)
# and a list of numbers. Each time through the loop ask the user to guess a
# number in the list and tell them whether or not they guessed correctly.
print("Challenge 4")
num_list = [1, 2, 3]
correct_flag = False
guess = input("Guess an integer number. Type 'q' to quit: ")
while guess != "q":
    for num in num_list:
        if int(guess) == num:
            correct_flag = True
    if correct_flag:
        print("Your guess {} is in the list!".format(guess))
    else:
        print("Your guess {} is NOT in the list".format(guess))
    guess = input("Guess a number. Type 'q' to quit: ")

# C5: Multipy all the number in the list [8, 19, 148, 4] with all the numbers
# in the list [9, 1, 33, 83], and append each result to a third list
print("Challenge 5")
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
cartesian_product = []
for i in list1:
    for j in list2:
        cartesian_product.append(i*j)
for i in cartesian_product:
    print(i)








