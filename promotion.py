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

    def charger_json(self, fichier_json):
        with open(fichier_json, 'r') as f:
            data = json.load(f)

            self.liste_etudiant = []
            for etudiant_data in data:
                etudiant = Etudiant(
                    etudiant_data["nom"],
                    etudiant_data["prenom"],
                    etudiant_data["age"],
                    etudiant_data["numero_etudiant"],
                )
                etudiant.moyenne = etudiant_data["moyenne"]
                etudiant.notes = etudiant_data.get("notes", [])
                self.ajouter_etudiant(etudiant)

    def afficher_liste_etudiants(self):
        for etudiant in self.liste_etudiant:
            print(f"Etudiant : {etudiant.nom} {etudiant.prenom}, Age: {etudiant.age}, Numero Etudiant: {etudiant.numero_etudiant}, Moyenne: {etudiant.moyenne}, Statut: {etudiant.statut()}")

    def generer_pdf(self, fichier_pdf):
        pdf = FPDF(orientation="portrait", format="A4")

        pdf.add_font("DejaVuSans", style="", fname="DejaVuSans-Bold.ttf", uni=True)

        pdf.add_page()
        pdf.set_font("Arial", size=16)
        pdf.cell(200, 10, txt="Liste des Etudiants", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        pdf.ln(10)

        grey = (128, 128, 128)
        headings_style = FontFace(fill_color=grey)
        with pdf.table(text_align="CENTER", headings_style=headings_style) as table:
            table.row(["Nom", "Prenom", "Age", "Numero Etudiant", "Moyenne", "Statut"])
            for etudiant in self.liste_etudiant:
                table.row([etudiant.nom, 
                           etudiant.prenom, 
                           str(etudiant.age), 
                           str(etudiant.numero_etudiant), 
                           str(etudiant.moyenne), 
                           etudiant.statut()])
        pdf.set_y(-30)
        pdf.set_font("DejaVuSans", size=12)
        pdf.multi_cell(0, 10, f"PDF bien imprimé par JuaniPhet à partir du projet Gestion d'étudiant 😉", align='C')
        pdf.output(fichier_pdf)


promo = Promotion()
promo.ajouter_etudiant(e1)
promo.ajouter_etudiant(Etudiant("Sergio","Ramos",22,681042000)) 
promo.ajouter_etudiant(Etudiant("Karim","Benzema",35,681042001))
promo.ajouter_etudiant(Etudiant("Vinicius","Junior",22,681042002))
promo.sauvegarder_json("promo.json")
promo.sauvegarder_txt("promo.txt")
promo.afficher_liste_etudiants()
promo.charger_json("promo2.json")
print("***************")
promo.afficher_liste_etudiants()
promo.generer_pdf("promo.pdf")