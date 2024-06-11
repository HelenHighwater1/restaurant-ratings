"""Restaurant rating lister."""


# Your job is to write a program named ratings.py that:
# Reads the ratings in from the file
# Stores them in a dictionary
# And finally, spits out the ratings in alphabetical order by restaurant

# Hint 1: Using .items() to get a list of your dictionary entries will help with sorting.
# Hint 2: Refer to the Python docs on the sorted() function if you need a reminder of how to sort.

# def print_ratings(ratings):
#     ratings = sorted(ratings.items())

#     for rating in ratings:
#         name, score = rating
#         print(f"{name} is rated at {score}")



# def restaurant_ratings(filename):
#     file = open(filename)
#     ratings_dict = {}

#     for line in file:
#         name, rating = line.split(":")
#         ratings_dict[name] = rating

#     print_ratings(ratings_dict)

#     while True:
#         if input("Do you want add a new restaurant y/n") == "n":
#             print("goodbye")
#             break
    
#         new_restaurant = input("input restaurant name: > ")
#         new_rating = input("input rating: > ")

#         ratings_dict[new_restaurant] = new_rating
        
#         print_ratings(ratings_dict)

# restaurant_ratings("scores.txt")

#______________________________
def process_ratings(filename):
    file = open(filename)
    ratings_dict = {}

    for line in file:
        name, rating = line.split(":")
        ratings_dict[name] = rating
    
    file.close()
    return ratings_dict


def print_ratings(file):
    ratings = process_ratings(file)
    ratings = sorted(ratings.items())

    for rating in ratings:
        name, score = rating
        print(f"{name} is rated at {score}")


def write_rating(filename, name, rating):
    file = open("scores.txt", "a")
    file.write(f"{name}:{str(rating)}\n")
    file.close()

def user_rating_interface(filename):
    print_ratings(filename)
    while True:
        user_input = input("Do you want add a new restaurant y/n > ")
        if user_input.lower() == "n":
            break
        else:
            new_restaurant = input("input restaurant name: > ")
            new_rating = input("input rating: > ")
            write_rating(filename, new_restaurant.capitalize(), new_rating)
            print_ratings(filename)


user_rating_interface("scores.txt")
