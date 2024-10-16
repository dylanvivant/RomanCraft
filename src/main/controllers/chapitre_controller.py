from models.chapitre import Chapitre

class ChapitreController:
    def __init__(self, view, roman_controller):
        self.view = view
        self.roman_controller = roman_controller
        self.connecter_signaux()

    def connecter_signaux(self):
        self.view.ajouter_btn.clicked.connect(self.ajouter_chapitre)
        self.view.modifier_btn.clicked.connect(self.modifier_chapitre)
        self.view.supprimer_btn.clicked.connect(self.supprimer_chapitre)
        self.view.chapitres_list.currentItemChanged.connect(self.afficher_chapitre)

    def ajouter_chapitre(self):
        titre = self.view.titre_edit.text()
        resume = self.view.resume_edit.toPlainText()
        nouveau_chapitre = Chapitre(titre, resume)
        roman = self.roman_controller.get_roman()
        if roman:
            roman.chapitres.append(nouveau_chapitre)
            self.mettre_a_jour_liste()
            self.vider_champs()

    def modifier_chapitre(self):
        index = self.view.chapitres_list.currentRow()
        roman = self.roman_controller.get_roman()
        if roman and index >= 0:
            chapitre = roman.chapitres[index]
            chapitre.titre = self.view.titre_edit.text()
            chapitre.resume = self.view.resume_edit.toPlainText()
            chapitre.contenu = self.view.contenu_edit.toPlainText()
            self.mettre_a_jour_liste()

    def supprimer_chapitre(self):
        index = self.view.chapitres_list.currentRow()
        roman = self.roman_controller.get_roman()
        if roman and index >= 0:
            del roman.chapitres[index]
            self.mettre_a_jour_liste()
            self.vider_champs()

    def afficher_chapitre(self, item):
        if item:
            index = self.view.chapitres_list.row(item)
            roman = self.roman_controller.get_roman()
            if roman:
                chapitre = roman.chapitres[index]
                self.view.titre_edit.setText(chapitre.titre)
                self.view.resume_edit.setPlainText(chapitre.resume)
                self.view.contenu_edit.setPlainText(chapitre.contenu)

    def mettre_a_jour_liste(self):
        self.view.chapitres_list.clear()
        roman = self.roman_controller.get_roman()
        if roman:
            for chapitre in roman.chapitres:
                self.view.chapitres_list.addItem(chapitre.titre)

    def vider_champs(self):
        self.view.titre_edit.clear()
        self.view.resume_edit.clear()
        self.view.contenu_edit.clear()