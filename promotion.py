from etudiant import Etudiant
class Promotion(Etudiant) :
    def __init__(self,nom,prenom,age,numero_etudiant):
        super().__init__(nom,prenom,age,numero_etudiant)
        self.liste_etudiant=[]

    def ajouter_etudiant(self,etudiant):
        self.liste_etudiant.append(etudiant)


