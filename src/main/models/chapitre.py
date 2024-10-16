from datetime import datetime
from typing import Dict, Any

class Chapitre:
    """
    Represente un chapitre d'un roman.
    """
    def __init__(self, titre: str, resume: str):
        """
        Initialise un objet Chapitre.
        :param titre: titre du chapitre
        :param resume: resume du chapitre
        """
        self.titre: str = titre
        self.resume: str = resume
        self.contenu: str = ""
        self.date_creation: datetime = datetime.now()
        self.derniere_modification: datetime = self.date_creation

    def modifier_contenu(self, nouveau_contenu: str) -> None:
        """
        Modifie le contenu du chapitre.
        :param nouveau_contenu: nouveau contenu du chapitre
        """
        self.contenu = nouveau_contenu
        self.derniere_modification = datetime.now()

    def to_dict(self) -> Dict[str, Any]:
        """
        Retourne le chapitre sous forme de dictionnaire.
        """
        return {
            "titre": self.titre,
            "resume": self.resume,
            "contenu": self.contenu,
            "date_creation": self.date_creation.isoformat(),
            "derniere_modification": self.derniere_modification.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Chapitre':
        """
        Retourne un objet Chapitre a partir d'un dictionnaire.
        :param data: dictionnaire representant le chapitre
        """
        chapitre = cls(data['titre'], data['resume'])
        chapitre.contenu = data['contenu']
        chapitre.date_creation = datetime.fromisoformat(data['date_creation'])
        chapitre.derniere_modification = datetime.fromisoformat(data['derniere_modification'])
        return chapitre
