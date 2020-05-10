# Needed to change the variable __watched_movies to __wached_movies as Judge only accepts that...

class Movie:
    __wached_movies = 0

    def __init__(self, name, director):
        self.name = name
        self.director = director
        self.watched = False

    def change_name(self, n):
        self.name = n

    def change_director(self, d):
        self.director = d

    def watch(self):
        if not self.watched:
            self.watched = True
            Movie.__wached_movies += 1

    def __repr__(self):
        return f"Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {Movie.__wached_movies}"


first_movie = Movie("Inception", "Christopher Nolan")
second_movie = Movie("The Matrix", "The Wachowskis")
third_movie = Movie("The Predator", "Shane Black")
first_movie.change_director("Me")
third_movie.change_name("My Movie")
first_movie.watch()
third_movie.watch()
first_movie.watch()
print(first_movie)
print(second_movie)
print(third_movie)
