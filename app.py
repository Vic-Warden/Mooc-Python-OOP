from library import VHF, DVD, Friend, Library, clean_movie_data

# Raw Data
films = [
    ("Blade Runner (1982)", "vhf"),
    ("Alien : Le 8ème Passager (1979)", "vhf"),
    ("2001 : L'Odyssée de l'espace (1968)", "VhF"),
    ("Matrix (1999)", "DVD"),
    ("Interstellar (2014)", "dvD")
]

friends = [
    ("Paul", "Blade Runner"),
    ("Lucie",),
    ("Zoé", "Terminator 2 : Le Jugement dernier"),
]

# Setup the Library
my_lib = Library()

# Clean data and create Movie objects
for data in films:
    name, year, m_type = clean_movie_data(data)
    
    if m_type == "VHF":
        my_lib.add_movie(VHF(name, year))
    elif m_type == "DVD":
        my_lib.add_movie(DVD(name, year))

# Create Friend objects and lend movies
for data in friends:
    friend_name = data[0]
    my_lib.add_friend(Friend(friend_name))
    
    # If the tuple has a second item, it means they borrowed a movie
    if len(data) > 1:
        my_lib.lend_movie(data[1], friend_name)

# Test the features
my_lib.show_all_movies(sort_by="year")
my_lib.get_random_movie()