from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit, QTextEdit, QPushButton

class ChapitreView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()

        # Liste des chapitres
        self.chapitres_list = QListWidget()
        layout.addWidget(self.chapitres_list, 1)

        # Formulaire d'édition
        form_layout = QVBoxLayout()
        self.titre_edit = QLineEdit()
        self.titre_edit.setPlaceholderText("Titre du chapitre")
        self.resume_edit = QTextEdit()
        self.resume_edit.setPlaceholderText("Résumé du chapitre")
        self.contenu_edit = QTextEdit()
        self.contenu_edit.setPlaceholderText("Contenu du chapitre")

        form_layout.addWidget(self.titre_edit)
        form_layout.addWidget(self.resume_edit)
        form_layout.addWidget(self.contenu_edit)

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