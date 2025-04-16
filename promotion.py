from etudiant import Etudiant, e1
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

    # def sauvegarder_txt(self, fichier_txt):
    #     with open(fichier_txt, 'w') as file:
    #         for etudiant in self.liste_etudiant:
    #             file.write(f"Etudiant : {etudiant.nom} {etudiant.prenom}, Age: {etudiant.age}, Numero Etudiant: {etudiant.numero_etudiant}, Moyenne: {etudiant.moyenne}, Statut: {etudiant.statut()}\n")

    def afficher_promo(self):
        for etudiant in self.liste_etudiant:
            print(f"Etudiant : {etudiant.nom} {etudiant.prenom}, Age: {etudiant.age}, Numero Etudiant: {etudiant.numero_etudiant}, Moyenne: {etudiant.moyenne}, Statut: {etudiant.statut()}\n")
    
    
    def charger_json(self, fichier_json):
        # Ouvrir le fichier en lecture
        with open(fichier_json, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        # Recréer les objets Etudiant à partir des données
        self.liste_etudiant = []
        for etudiant_dict in data:
            # On suppose que etudiant_dict est un dictionnaire contenant les clés nécessaires
            etudiant = Etudiant(
                nom=etudiant_dict["nom"],
                prenom=etudiant_dict["prenom"],
                age=etudiant_dict["age"],
                numero_etudiant=etudiant_dict["numero_etudiant"]
            )
            # Recharger la liste des notes si nécessaire
            etudiant.notes = etudiant_dict.get("notes", [])
            etudiant.moyenne = etudiant_dict["moyenne"]  # ou directement à partir du fichier
            self.liste_etudiant.append(etudiant)


promo = Promotion()
promo.ajouter_etudiant(e1)
promo.ajouter_etudiant(Etudiant("Sergio","Ramos",22,681042000)) 
promo.ajouter_etudiant(Etudiant("Karim","Benzema",35,681042001))
promo.ajouter_etudiant(Etudiant("Vinicius","Junior",22,681042002))
promo.sauvegarder_json("promo.json")
print("promo")
promo.afficher_promo()
print("promo2")
promo.charger_json("promo2.json")
promo.afficher_promo()
# promo.sauvegarder_txt("promo.txt")

