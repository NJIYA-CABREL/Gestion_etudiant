import json
from personne import Personne

class Etudiant(Personne):
    def __init__(self,nom,prenom,age,numero_etudiant):
        super().__init__(nom,prenom,age)
        self.numero_etudiant=numero_etudiant
        self.moyenne=0
        self.notes=[]
   
    def ajouter_note(self,note):
        self.notes.append(note)
        self.moyenne = float(sum(self.notes)/len(self.notes))

    def statut(self):
        if self.moyenne >= 10:
            return "Admis"
        else:
            return "Echoue"

    def se_presenter(self):
        print("Etudiant :",self.nom,self.prenom,
              "\nAge:",self.age, 
              "\nNumero Etudiant:",self.numero_etudiant, 
              "\nMoyenne:",self.moyenne, 
              "\nStatut:",self.statut()) 


e1 = Etudiant("FEDE", "VALVERDE", 23, 681042017)
e1.ajouter_note(10)
e1.ajouter_note(14)
# e1.se_presenter()

# print(json.dumps(e1.__dict__, sort_keys=False, indent=4))
# print(json.dumps(e1, sort_keys=True, indent=4))