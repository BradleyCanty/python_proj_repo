# 'The Self-taught Programmer' Ch 5: Containers Challenges
# C1: Create list of healthy food
heatlhy_food = ["eggs","bananas","walnuts","blueberries","salmon"]
print(heatlhy_food)

# C2: Create a list of tuples, with each tuple containing the
# longitude and latitude of of somewhere you've lived or visited
location_list = [(39.01, -77.43),(34.08, -118.47),(24.55, -81.78)]
print(location_list)

# C3: Create a dictionary that conains different attributes
# about you: height, favorite color, favorite author
bradley_facts = {"height, ft": 5.8, "favorite color": "blue","favorite author":"Jordan Peterson"}
print(bradley_facts)

# C4: Write a program that lets the user ask your height, favorite
# color, or favorite author, and returns the result from the dictionary you
# create in Challenge 3
user_input = input("Enter 'height', 'color', or 'author'")
if user_input == "height":
    print("Bradley's height is " + str(bradley_facts["height, ft"]))
elif user_input == "color":
    print("Bradley's favorite color is " + bradley_facts["favorite color"])
elif user_input == "author":
    print("Bradley's favorite author is " + bradley_facts["favorite author"])
else:
    print("Not valid input, exiting program")

# C5: Create a dictionary mapping states to cities
state_cities = {"California":["Los Angeles","San Diego","San Jose"],
              "Virginia":["Fairfax","Herndon","Richmond","Blacksburg"],
              "Texas":["Dallas","Houston","Austin"]}
print(state_cities)

# C6: Python set is a container such that items are unordered,
# repetitions are unimportant, items are immutable, and is unindexed
my_set = {'a','b','c','a'}
print(my_set)
