# Parent class
class Vehicule:
    def __init__(self, couleur):
        self.couleur = couleur

# Child class
class Voiture(Vehicule):
    def __init__(self, couleur, marque):

        # Call the parent class constructor
        super().__init__(couleur)

        # Initialize the brand attribute
        self.marque = marque


# Instantiate a car
ma_voiture = Voiture("Rouge", "Peugeot")

print(ma_voiture.couleur) 
print(ma_voiture.marque)