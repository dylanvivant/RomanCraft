from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit, QTextEdit, QPushButton

class PersonnageView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()

        # Liste des personnages
        self.personnages_list = QListWidget()
        layout.addWidget(self.personnages_list, 1)

        # Formulaire d'édition
        form_layout = QVBoxLayout()
        self.nom_edit = QLineEdit()
        self.nom_edit.setPlaceholderText("Nom du personnage")
        self.description_edit = QTextEdit()
        self.description_edit.setPlaceholderText("Description du personnage")

        form_layout.addWidget(self.nom_edit)
        form_layout.addWidget(self.description_edit)

        # Boutons
        buttons_layout = QHBoxLayout()
        self.ajouter_btn = QPushButton("Ajouter")
        self.modifier_btn = QPushButton("Modifier")
        self.supprimer_btn = QPushButton("Supprimer")

        buttons_layout.addWidget(self.ajouter_btn)
        buttons_layout.addWidget(self.modifier_btn)
        buttons_layout.addWidget(self.supprimer_btn)

        form_layout.addLayout(buttons_layout)

        layout.addLayout(form_layout, 2)

        self.setLayout(layout)