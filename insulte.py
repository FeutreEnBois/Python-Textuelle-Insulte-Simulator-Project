from random import randint


#On stock les bouts de phrases  dans une classe pour pouvoir les récupérer plus tard, avec leur dégat et leur type si présent.
class insulte:
    def __init__(self):
        self.accroche = [Accroche("J'espere que", 2), Accroche("a un moment", 2), Accroche("imagine quand meme que", 3), Accroche("avoue au moins que", 3)]
        self.sujet = [Sujet("ton caniche", 6, "animaux"),Sujet("ton chat",6,"animaux"),Sujet("ta voiture",6,"argent"),Sujet("Ton job",4,"argent"),Sujet("Ton père",8,"famille"),Sujet("Ton descendant",6,"famille")]
        self.complement = [Complement("demain", 1), Complement("aujourd'hui", 1), Complement("rue", 2) , Complement("hopital", 1), Complement("ce matin",1),Complement("se soir",1) , Complement("dans un combat",2), Complement("ta chambre",1),  Complement("in the kitchen",3)]
        self.liaisons = [Liaisons("un", 1), Liaisons("est", 1), Liaisons("une", 1), Liaisons("du", 1),Liaisons("a peine plus", 1), Liaisons("que", 1), Liaisons("un peu comme", 1)]
        self.principal = [Principal("est si moche", 8, "argent"), Principal("jaune comme", 2, "famille"), Principal("tel une voiture", 3, "argent"), Principal("un déambulateur", 5, "famille"), Principal("sac a caca", 9, "animaux")]
        self.verb = [Verb("est",4), Verb("mange",3), Verb("se bat",2), Verb("marche",5),Verb("sleep",4),Verb("tombe",5),Verb("bouge",4), Verb("fuit", 4)]
        self.adjectif = [Adjectif("bleu",2), Adjectif("mort",4),Adjectif("grand",3),Adjectif("petit",3),Adjectif("égoïste",6),Adjectif("pas courageux", 3)]


#On récupère les bouts de phrases, leur dégat et leur type pour les "sujets" et "Principal"
class Accroche:
    def __init__(self, name, point):
        self.name = name
        self.point = point
    def __str__(self):
        return self.name

class Sujet:
    def __init__(self, name, point, tipe):
        self.name = name
        self.point = point
        self.type = tipe
    def __str__(self):
        return self.name

class Liaisons:
    def __init__(self, name, point):
        self.name = name
        self.point = point
    def __str__(self):
        return self.name

class Complement :
    def __init__(self, name, point):
        self.name = name
        self.point = point
    def __str__(self):
        return self.name

class Principal :
    def __init__(self, name, point, tipe):
        self.name = name
        self.point = point
        self.type = tipe
    def __str__(self):
        return self.name


class Verb:
    def __init__(self,name, point):
        self.name = name
        self.point = point
    def __str__(self):
        return self.name

class Adjectif:
    def __init__(self,name, point):
        self.name = name
        self.point = point
    def __str__(self):
        return self.name


#Cette fonction permet d'obtenir 3 bouts de phrases de chaque catégories grace au fonction "get" et les renvoyer.
def getPhrase():
    res = []
    for _ in range(3):
        res.append(getAccroche(insulte().accroche))
        res.append(getSujet(insulte().sujet))
        res.append(getPrincipal(insulte().principal))
        res.append(getLiaisons(insulte().liaisons))
        res.append(getComplement(insulte().complement))
        res.append(getAdjectif(insulte().adjectif))
        res.append(getVerb(insulte().verb))
    return res


#Ces fonctions vont récupérées aléatoirement un bout de phrase de leur catégorie 
def getAccroche(accroche):
    res = accroche[randint(0, len(accroche) -1)]
    return res
def getPrincipal(principal):
    res = principal[randint(0, len(principal) -1)]
    return res
def getSujet(sujet):
    res = sujet[randint(0, len(sujet)-1)]
    return res
def getLiaisons(liaisons):
    res = liaisons[randint(0, len(liaisons)-1)]
    return res
def getComplement(complement):
    res = complement[randint(0, len(complement)-1)]
    return res
def getAdjectif(Adjectif):
    res = Adjectif[randint(0, len(Adjectif)-1)]
    return res
def getVerb(verb):
    res = verb[randint(0, len(verb)-1)]
    return res