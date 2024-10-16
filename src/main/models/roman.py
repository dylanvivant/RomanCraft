from datetime import datetime
from typing import List, Dict, Any
from .chapitre import Chapitre
from .personnage import Personnage
from .idee import Idee

class Roman:
    """
    Represente un roman.
    """
    def __init__(self, titre: str, auteur: str):
        """
        Initialise un objet Roman.
        :param titre: titre du roman
        :param auteur: auteur du roman
        """
        self.titre: str = titre
        self.auteur: str = auteur
        self.date_creation: datetime = datetime.now()
        self.derniere_modification: datetime = self.date_creation
        self.chapitres: List[Chapitre] = []
        self.personnages: List[Personnage] = []
        self.idees: List[Idee] = []

    def ajouter_chapitre(self, titre: str, resume: str) -> None:
        """
        Ajoute un chapitre au roman.
        :param titre: titre du chapitre
        :param resume: resume du chapitre
        """
        self.chapitres.append(Chapitre(titre, resume))
        self.derniere_modification = datetime.now()

    def ajouter_personnage(self, nom: str, description: str) -> None:
        """
        Ajoute un personnage au roman.
        :param nom: nom du personnage
        :param description: description du personnage
        """
        self.personnages.append(Personnage(nom, description))
        self.derniere_modification = datetime.now()

    def ajouter_idee(self, contenu: str) -> None:
        """
        Ajoute une idee au roman.
        :param contenu: contenu de l'idee
        """
        self.idees.append(Idee(contenu))
        self.derniere_modification = datetime.now()

    def to_dict(self) -> Dict[str, Any]:
        """
        Retourne le roman sous forme de dictionnaire.
        """
        return {
            "titre": self.titre,
            "auteur": self.auteur,
            "date_creation": self.date_creation.isoformat(),
            "derniere_modification": self.derniere_modification.isoformat(),
            "chapitres": [chapitre.to_dict() for chapitre in self.chapitres],
            "personnages": [personnage.to_dict() for personnage in self.personnages],
            "idees": [idee.to_dict() for idee in self.idees]
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Roman':
        """
        Retourne un objet Roman a partir d'un dictionnaire.
        :param data: dictionnaire representant le roman
        """
        roman = cls(data['titre'], data['auteur'])
        roman.date_creation = datetime.fromisoformat(data['date_creation'])
        roman.derniere_modification = datetime.fromisoformat(data['derniere_modification'])
        roman.chapitres = [Chapitre.from_dict(c) for c in data['chapitres']]
        roman.personnages = [Personnage.from_dict(p) for p in data['personnages']]
        roman.idees = [Idee.from_dict(i) for i in data['idees']]
        return roman
