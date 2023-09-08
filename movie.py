movies = [];

MENU_OPTIONS = "\nEnter a to add movie, Enter l to get list of movie, Enter f to find movie by title, Enter q to quit: ";

# function to add movie
def add_movie():
    title = input("Enter the name of movie: ");
    year  = input("Enter the release data: ");
    director = input("Enter the director name: ");

    movies.append({
        "title": title,
        "year" : year,
        "director" : director,
    });


# get movie list
def list_movie():
    for movie in movies:
        show_movie_list(movie);


# show movie list
def show_movie_list(movie):
    print(f"Title: {movie['title']}");
    print(f"Year: {movie['year']}");
    print(f"Director: {movie['director']}");


# Find movie by title
def find_movie():
    search_movie = input("Enter the name of movie to find: ");

    for movie in movies:
        if movie["title"] == search_movie:
            show_movie_list(movie)


user_selections = {
    "a" : add_movie,
    "l" : list_movie,
    "f" : find_movie
}


# Select Menu
def select_menu():
    selection = input(MENU_OPTIONS);

    while selection != "q":
        if selection in user_selections:
            selected_option = user_selections[selection];
            selected_option();
        # if selection == "a":
        #     add_movie();
        # elif selection == "l":
        #     list_movie();
        # elif selection == "f":
        #     find_movie();
        else:
            print("\nUnknown Command Entered");

        selection = input(MENU_OPTIONS);


select_menu();