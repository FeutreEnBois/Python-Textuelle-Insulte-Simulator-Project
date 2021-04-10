# class player:
#     def __init__(self,name,P):
#         self.classe = ["La vieille", "L'étudiant", "Mage"]
#         self.name = name
#         self.P = P
#         if self.name == "La vieille":
#             self.pv = 60
#             self.resistance = "Famille"
#             self.weakness= "Animaux"
#         elif self.name == "L'étudiant":
#             self.pv = 50
#             self.resistance = "Travail"
#             self.weakness = "Argent"
#         elif self.name == "Mage":
#             self.pv = 40
#             self.resistance = "Lieux"
#             self.weakness = "Famille"
class player:
    def __init__(self, P ,name = "échec"):
        self.name = name
        self.P = P
        if name == 1:
            self.name = "Mage"
            self.pv = 60
            self.resistance = "Lieux"
            self.weakness = "Famille"
        elif name == 2:
            self.name = "La vieille"
            self.pv = 60
            self.resistance = "Famille"
            self.weakness= "Animaux"
        elif name == 3:
            self.name = "L'étudiant"
            self.pv = 60
            self.resistance = ""
            self.weakness = "Argent"
        