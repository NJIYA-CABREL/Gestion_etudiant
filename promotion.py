from etudiant import Etudiant, e1
from fpdf import FPDF, FontFace, XPos, YPos
import json

class Promotion() :
    def __init__(self):
        self.liste_etudiant = []
        
    def ajouter_etudiant(self, etudiant):
        self.liste_etudiant.append(etudiant)

    def sauvegarder_json(self, fichier_json):
        with open(fichier_json, 'w') as f:  #w: write, r: read, a: append
            data = []
            for etudiant in self.liste_etudiant:
                data.append(etudiant.__dict__)
            f.write(json.dumps(data, sort_keys=False, indent=4))

    def sauvegarder_txt(self, fichier_txt):
        with open(fichier_txt, 'w') as file:
            for etudiant in self.liste_etudiant:
                file.write(f"Etudiant : {etudiant.nom} {etudiant.prenom}, Age: {etudiant.age}, Numero Etudiant: {etudiant.numero_etudiant}, Moyenne: {etudiant.moyenne}, Statut: {etudiant.statut()}\n")



promo = Promotion()
promo.ajouter_etudiant(e1)
promo.ajouter_etudiant(Etudiant("Sergio","Ramos",22,681042000)) 
promo.ajouter_etudiant(Etudiant("Karim","Benzema",35,681042001))
promo.ajouter_etudiant(Etudiant("Vinicius","Junior",22,681042002))
promo.sauvegarder_json("promo.json")
promo.sauvegarder_txt("promo.txt")

