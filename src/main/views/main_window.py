import os
import sys
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QListWidget, QStackedWidget, QLabel, 
                             QFileDialog, QInputDialog, QMessageBox, QFrame)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt, QFile, QTextStream, QIODevice


from views.chapitre_view import ChapitreView
from views.personnage_view import PersonnageView
from views.idee_view import IdeeView
from controllers.chapitre_controller import ChapitreController
from controllers.personnage_controller import PersonnageController
from controllers.idee_controller import IdeeController
from controllers.roman_controller import RomanController


def load_stylesheet(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_dir))  # Remonte de deux niveaux pour atteindre la racine du projet
    style_file_path = os.path.join(project_root, 'resources', 'styles', file_name)
    
    try:
        with open(style_file_path, "r") as file:
            return file.read()
    except IOError:
        print(f"Impossible d'ouvrir le fichier de style: {style_file_path}")
        return ""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RomanCraft")
        self.setGeometry(100, 100, 1200, 800)

        self.roman_controller = RomanController(self)


        # Définir l'icône de l'application
        icon_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'resources', 'icons', 'book_icon.svg')
        self.setWindowIcon(QIcon(icon_path))

        # Appliquer le style
        self.setStyleSheet(load_stylesheet("style.qss"))

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal
        main_layout = QHBoxLayout(central_widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Panneau de navigation
        nav_panel = QFrame()
        nav_panel.setObjectName("nav_panel")
        nav_panel.setFixedWidth(250)  # Largeur fixe pour le panneau de navigation
        nav_layout = QVBoxLayout(nav_panel)
        nav_layout.setContentsMargins(10, 20, 10, 20)
        nav_layout.setSpacing(20)

        self.roman_info = QLabel("Titre du Roman\nAuteur")
        self.roman_info.setObjectName("roman_info")
        self.roman_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        nav_layout.addWidget(self.roman_info)

        self.nav_list = QListWidget()
        self.nav_list.setObjectName("nav_list")
        self.nav_list.addItems(["Chapitres", "Personnages", "Idées"])
        nav_layout.addWidget(self.nav_list)


        icon_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'resources', 'icons', 'new_book.svg')
        new_button = QPushButton("Nouveau Roman")
        new_button.setIcon(QIcon(icon_path))
        nav_layout.addWidget(new_button)

        nav_layout.addStretch()  # Ajoute un espace extensible en bas

        main_layout.addWidget(nav_panel)

        # Séparateur vertical
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.VLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        main_layout.addWidget(separator)

        # Panneau principal
        self.main_panel = QStackedWidget()
        main_layout.addWidget(self.main_panel)

        # Pages pour chaque section
        self.chapitres_page = ChapitreView()
        self.personnages_page = PersonnageView()
        self.idees_page = IdeeView()

        self.main_panel.addWidget(self.chapitres_page)
        self.main_panel.addWidget(self.personnages_page)
        self.main_panel.addWidget(self.idees_page)

        # Connecter la liste de navigation au panneau principal
        self.nav_list.currentRowChanged.connect(self.main_panel.setCurrentIndex)
        
        # Initialiser les contrôleurs
        self.chapitre_controller = ChapitreController(self.chapitres_page, self.roman_controller)
        self.personnage_controller = PersonnageController(self.personnages_page, self.roman_controller)
        self.idee_controller = IdeeController(self.idees_page, self.roman_controller)

        # Barre de menu
        self.create_menu_bar()

    def create_menu_bar(self):
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("Fichier")
        file_menu.addAction("Nouveau Roman", self.nouveau_roman)
        file_menu.addAction("Ouvrir Roman", self.ouvrir_roman)
        file_menu.addAction("Sauvegarder", self.sauvegarder_roman)
        file_menu.addAction("Sauvegarder Sous...", self.sauvegarder_roman_sous)
        file_menu.addSeparator()
        file_menu.addAction("Quitter", self.close)

        edit_menu = menu_bar.addMenu("Édition")
        edit_menu.addAction("Couper")
        edit_menu.addAction("Copier")
        edit_menu.addAction("Coller")

        help_menu = menu_bar.addMenu("Aide")
        help_menu.addAction("À propos", self.afficher_a_propos)

    def nouveau_roman(self):
        titre, ok = QInputDialog.getText(self, "Nouveau Roman", "Entrez le titre du roman:")
        if ok and titre:
            auteur, ok = QInputDialog.getText(self, "Nouveau Roman", "Entrez le nom de l'auteur:")
            if ok and auteur:
                self.roman_controller.nouveau_roman(titre, auteur)

    def ouvrir_roman(self):
        chemin_fichier, _ = QFileDialog.getOpenFileName(self, "Ouvrir Roman", "", "Fichiers JSON (*.json)")
        if chemin_fichier:
            if self.roman_controller.ouvrir_roman(chemin_fichier):
                QMessageBox.information(self, "Succès", "Roman ouvert avec succès.")
            else:
                QMessageBox.warning(self, "Erreur", "Impossible d'ouvrir le roman.")

    def sauvegarder_roman(self):
        if not self.roman_controller.get_roman():
            QMessageBox.warning(self, "Erreur", "Pas de roman ouvert à sauvegarder.")
            return
        
        chemin_fichier, _ = QFileDialog.getSaveFileName(self, "Sauvegarder Roman", "", "Fichiers JSON (*.json)")
        if chemin_fichier:
            if self.roman_controller.sauvegarder_roman(chemin_fichier):
                QMessageBox.information(self, "Succès", "Roman sauvegardé avec succès.")
            else:
                QMessageBox.warning(self, "Erreur", "Impossible de sauvegarder le roman.")

    def sauvegarder_roman_sous(self):
        self.sauvegarder_roman()

    def afficher_a_propos(self):
        QMessageBox.about(self, "À propos de RomanCraft", "RomanCraft est un outil d'aide à l'écriture de romans.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())