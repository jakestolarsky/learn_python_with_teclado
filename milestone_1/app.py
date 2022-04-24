# Incomplete app!

from re import A


MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


# You may want to create a function for this code

def input_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
    'title': title,
    'director': director,
    'year': year })


def print_list():
    for i in movies:
        print("\ntitle: " + i["title"] + "\ndirector: " + i["director"] + "\nyear: " + i["year"])


def find_movie():
    pass


# Create other functions for:
#   - listing movies
#   - finding movies


# And another function here for the user menu
selection = input(MENU_PROMPT)
while selection != 'q':
    if selection == "a":
        input_movie()
    elif selection == "l":
        print_list()
    elif selection == "f":
        find_movie()
    else:
        print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)


# Remember to run the user menu function at the end!
