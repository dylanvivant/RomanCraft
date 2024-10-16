import json
from models.roman import Roman
from models.chapitre import Chapitre
from models.personnage import Personnage
from models.idee import Idee

class RomanController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.roman = None

    def nouveau_roman(self, titre, auteur):
        self.roman = Roman(titre, auteur)
        self.mettre_a_jour_interface()

    def ouvrir_roman(self, chemin_fichier):
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.roman = Roman.from_dict(data)
            self.mettre_a_jour_interface()
            return True
        except Exception as e:
            print(f"Erreur lors de l'ouverture du roman : {e}")
            return False

    def sauvegarder_roman(self, chemin_fichier):
        if not self.roman:
            return False
        
        try:
            with open(chemin_fichier, 'w', encoding='utf-8') as f:
                json.dump(self.roman.to_dict(), f, ensure_ascii=False, indent=4)
            return True
        except Exception as e:
            print(f"Erreur lors de la sauvegarde du roman : {e}")
            return False

    def mettre_a_jour_interface(self):
        # Mettre à jour l'affichage du titre et de l'auteur
        self.main_window.roman_info.setText(f"{self.roman.titre}\n{self.roman.auteur}")
        
        # Mettre à jour les listes de chapitres, personnages et idées
        self.main_window.chapitre_controller.mettre_a_jour_liste()
        self.main_window.personnage_controller.mettre_a_jour_liste()
        self.main_window.idee_controller.mettre_a_jour_liste()

    def get_roman(self):
        return self.roman