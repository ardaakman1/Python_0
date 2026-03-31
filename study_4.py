# DICTIONARIES
# It is like hash table in C
# allowing you to specify list indicies with words or phrases
# we define dictionaries with {}
# keys and values
pizzas = {
    "cheese": 9,  # cheese = key and 9 = value
    "peperoni": 10,
    "vegetable": 15,
    "buffalo chicken": 12
}
pizzas["cheese"] = 8
if pizzas["vegetable"] < 12:
    print("False")

pizzas["bacons"] = 13  # we can add to dictionaries without doing anything
print(pizzas["bacons"])
# the for loop in python is extremely flexible
for pie in pizzas:
    # use pie in here as a stand-in for "i"
    print(pie) # this will print all of the keys in dictionary
print()
# OR
for pie, price in pizzas.items():  # so it can iterate over all of the  keys
    print(price)
print()
for pie, price in pizzas.items():
    print("a whole {} pizza costs ${}".format(pie, price))  # this time I did not need to put 0 and 1 in the {} because they are sorted
    # or print("a whole" + pie + "pizza costs $" + str(price))