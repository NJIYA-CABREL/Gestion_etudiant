from personne import Personne
class Etudiant(Personne):
    def __init__(self,nom,prenom,age,numero_etudiant):
        super().__init__(nom,prenom,age)
        self.numero_etudiant=numero_etudiant
        self.moyenne=0
        self.liste=[]
        self.nbre_note=0
   
    def ajouter_note(self,note):
        self.liste.append(note)
        self.nbre_note = self.nbre_note + 1
        self.moyenne = float(sum(self.liste)/self.nbre_note)
        # self.moyenne = float(sum(self.liste)/len(self.liste))

    def statut(self):
        if self.moyenne >= 10:
            print("Etudiant",self.nom,self.prenom ,"a pour moyenne :",self.moyenne)
            print("Admis")
        else:
            print("Etudiant",self.nom,self.prenom ,"a pour moyenne :",self.moyenne)
            print("Redoublant")

e1=Etudiant("FEDE","VALVERDE",23,681042017)
e1.ajouter_note(10)
e1.ajouter_note(14)
e1.statut()