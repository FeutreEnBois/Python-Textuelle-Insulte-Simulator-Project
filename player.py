# class for the player
# 3 personnage, avec leur résistance / faiblesse respective
class player:
    def __init__(self, P ,name = "échec"):
        self.name = name
        self.P = P
        if name == 1:
            self.name = "Mage"
            self.pv = 60
            self.resistance = "Argent"
            self.weakness = "Famille"
        elif name == 2:
            self.name = "La vieille"
            self.pv = 60
            self.resistance = "Famille"
            self.weakness= "Animaux"
        elif name == 3:
            self.name = "L'étudiant"
            self.pv = 60
            self.resistance = "Animaux"
            self.weakness = "Argent"
        