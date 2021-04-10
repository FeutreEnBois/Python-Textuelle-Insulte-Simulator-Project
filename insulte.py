from random import randint

class insulte:
    def __init__(self):
        self.font = ""
        self.accroche = []
        self.sujet = [Sujet("ton caniche", 5, "animaux")]
        self.complement = [[]]
        self.liaisons = []
        self.principal = []
        self.verb = []
        self.adjectif = []


class Sujet:
    def __init__(self, name, point, tipe):
        self.name = name
        self.point = point
        self.type = tipe
    def __str__(self):
        return self.name

def getPhrase():
    res = []
    for _ in range(3):
        res.append(getSujet(insulte().sujet))
    return res
        #   def __init__(self):
        # self.insultFinal=["you six piece chicken Mcnobody", "hope you get hit by a truck and survive", "like a gta character", "you meth-head", "you donut", "with your yeeyee *** haricut", "you man child", "you precious stuck up bi... du-dude", "and remember your poor bruh", "you absolute cretin", "you fool", "hope a creeper blow up your house", "hope you step on a lego"]
        # self.sujet=["your hair", "your dog", "you","your car", "your job", "your cat", "your MOM !", "your sister", "your brother", "your uncle", "your aunt", "your family", "your hat", "your outfit", "your face", "your bank account", "your beard"]
        # self.starter=["looks like", "should", "smells like", "act like", "you should know that"]
        # self.complement=["tomorow", "today", "street", "hospital", "this morning", "tonight", "in a fight", "your room", "in the kitchen", ""]
        # self.liaisons=["so","if","almost","then", "it"]
        # self.verb=["is", "will be", "eating", "eat", "fight","walking","walk","sleeping","sleep","fall","falling","move","moving"] 

def getSujet(sujet):
    res = sujet[randint(0, len(sujet)-1)]
    return res
