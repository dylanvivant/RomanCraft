from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QTextEdit, QPushButton

class IdeeView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()

        # Liste des idées
        self.idees_list = QListWidget()
        layout.addWidget(self.idees_list, 1)

        # Formulaire d'édition
        form_layout = QVBoxLayout()
        self.idee_edit = QTextEdit()
        self.idee_edit.setPlaceholderText("Nouvelle idée")

        form_layout.addWidget(self.idee_edit)

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