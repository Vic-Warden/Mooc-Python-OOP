import random

# Data Cleaning Function
def clean_movie_data(raw_data):
    raw_title = raw_data[0]
    raw_type = raw_data[1].upper() 
    
    parts = raw_title.split(" (")
    name = parts[0].strip()
    year = parts[1].replace(")", "").strip()
    
    return name, year, raw_type

# Movie Classes: Base class and Subclasses
class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.location = "Library" 

class VHF(Movie):
    pass

class DVD(Movie):
    pass

# Friend Class
class Friend:
    def __init__(self, name):
        self.name = name
        self.borrowed_movie = None 

class Library:
    def __init__(self):
        self.movies = []
        self.friends = []

    def add_movie(self, movie):
        self.movies.append(movie)
        
    def add_friend(self, friend):
        self.friends.append(friend)

    def lend_movie(self, movie_name, friend_name):
        
        # Find the movie and the friend
        movie_to_lend = next((m for m in self.movies if m.name == movie_name), None)
        friend = next((f for f in self.friends if f.name == friend_name), None)
                
        if movie_to_lend and friend:
            movie_to_lend.location = friend.name
            friend.borrowed_movie = movie_to_lend

    def show_all_movies(self, sort_by="name"):
        print(f"\n--- Library (Sorted by {sort_by}) ---")
        
        # Sort logic
        if sort_by == "year":
            sorted_movies = sorted(self.movies, key=lambda x: x.year)
        else:
            sorted_movies = sorted(self.movies, key=lambda x: x.name)
            
        for m in sorted_movies:
            print(f"- {m.name} ({m.year}) [{type(m).__name__}] - Location: {m.location}")

    def get_random_movie(self):
        if self.movies:
            m = random.choice(self.movies)
            print(f"\n> Random pick for tonight: {m.name} ({m.year})")