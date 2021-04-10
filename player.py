class player:
    def __init__(self,name):
        self.classe = ["La vieille", 'Famille', "Travail", "Mage"]
        self.name = name
        if self.name == "La vieille":
            self.pv = 60
            self.resistance = "Famille"
            self.weakness= "Animaux"
        elif self.name == "L'étudiant":
            self.pv = 50
            self.resistance = "Travail"
            self.weakness = "Argent"
        elif self.name == "Mage":
            self.pv = 40
            self.resistance = "Lieux"
            self.weakness = "Famille"
        