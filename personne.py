class Personne:
    def __init__(self,nom,prenom,age):
        self.nom=nom
        self.prenom=prenom
        self.age=age
    
    def se_presenter(self):
        print("je m'appelle",self.nom,self.prenom,",j'ai ",self.age) 


p1 = Personne("Sergio","Ramos",22)
