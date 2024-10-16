from models.personnage import Personnage

class PersonnageController:
    def __init__(self, view, roman_controller):
        self.view = view
        self.roman_controller = roman_controller
        self.connecter_signaux()

    def connecter_signaux(self):
        self.view.ajouter_btn.clicked.connect(self.ajouter_personnage)
        self.view.modifier_btn.clicked.connect(self.modifier_personnage)
        self.view.supprimer_btn.clicked.connect(self.supprimer_personnage)
        self.view.personnages_list.currentItemChanged.connect(self.afficher_personnage)

    def ajouter_personnage(self):
        nom = self.view.nom_edit.text()
        description = self.view.description_edit.toPlainText()
        nouveau_personnage = Personnage(nom, description)
        roman = self.roman_controller.get_roman()
        if roman:
            roman.personnages.append(nouveau_personnage)
            self.mettre_a_jour_liste()
            self.vider_champs()

    def modifier_personnage(self):
        index = self.view.personnages_list.currentRow()
        roman = self.roman_controller.get_roman()
        if roman and index >= 0:
            personnage = roman.personnages[index]
            personnage.nom = self.view.nom_edit.text()
            personnage.description = self.view.description_edit.toPlainText()
            self.mettre_a_jour_liste()

    def supprimer_personnage(self):
        index = self.view.personnages_list.currentRow()
        roman = self.roman_controller.get_roman()
        if roman and index >= 0:
            del roman.personnages[index]
            self.mettre_a_jour_liste()
            self.vider_champs()

    def afficher_personnage(self, item):
        if item:
            index = self.view.personnages_list.row(item)
            roman = self.roman_controller.get_roman()
            if roman:
                personnage = roman.personnages[index]
                self.view.nom_edit.setText(personnage.nom)
                self.view.description_edit.setPlainText(personnage.description)

    def mettre_a_jour_liste(self):
        self.view.personnages_list.clear()
        roman = self.roman_controller.get_roman()
        if roman:
            for personnage in roman.personnages:
                self.view.personnages_list.addItem(personnage.nom)

    def vider_champs(self):
        self.view.nom_edit.clear()
        self.view.description_edit.clear()