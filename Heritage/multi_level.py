# Grandparent
class Film:
    def play(self):
        print("Playing film...")

# Parent
class FilmCassette(Film):
    def rewind(self):
        print("Rewinding tape...")

# Child 
class VHS(FilmCassette):
    def display_format(self):
        print("Format: VHS")

# Instantiate a VHS object
my_movie = VHS()

my_movie.play()             
my_movie.rewind()           
my_movie.display_format()   