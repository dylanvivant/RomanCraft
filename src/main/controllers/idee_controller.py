from models.idee import Idee

class IdeeController:
    def __init__(self, view, roman_controller):
        self.view = view
        self.roman_controller = roman_controller
        self.connecter_signaux()

    def connecter_signaux(self):
        self.view.ajouter_btn.clicked.connect(self.ajouter_idee)
        self.view.modifier_btn.clicked.connect(self.modifier_idee)
        self.view.supprimer_btn.clicked.connect(self.supprimer_idee)
        self.view.idees_list.currentItemChanged.connect(self.afficher_idee)

    def ajouter_idee(self):
        contenu = self.view.idee_edit.toPlainText()
        nouvelle_idee = Idee(contenu)
        roman = self.roman_controller.get_roman()
        if roman:
            roman.idees.append(nouvelle_idee)
            self.mettre_a_jour_liste()
            self.vider_champs()

    def modifier_idee(self):
        index = self.view.idees_list.currentRow()
        roman = self.roman_controller.get_roman()
        if roman and index >= 0:
            idee = roman.idees[index]
            idee.contenu = self.view.idee_edit.toPlainText()
            self.mettre_a_jour_liste()

    def supprimer_idee(self):
        index = self.view.idees_list.currentRow()
        roman = self.roman_controller.get_roman()
        if roman and index >= 0:
            del roman.idees[index]
            self.mettre_a_jour_liste()
            self.vider_champs()

    def afficher_idee(self, item):
        if item:
            index = self.view.idees_list.row(item)
            roman = self.roman_controller.get_roman()
            if roman:
                idee = roman.idees[index]
                self.view.idee_edit.setPlainText(idee.contenu)

    def mettre_a_jour_liste(self):
        self.view.idees_list.clear()
        roman = self.roman_controller.get_roman()
        if roman:
            for idee in roman.idees:
                self.view.idees_list.addItem(idee.contenu[:30] + "..." if len(idee.contenu) > 30 else idee.contenu)

    def vider_champs(self):
        self.view.idee_edit.clear()