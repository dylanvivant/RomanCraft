from typing import Dict, Any

class Personnage:
    def __init__(self, nom: str, description: str):
        self.nom: str = nom
        self.description: str = description

    def to_dict(self) -> Dict[str, str]:
        return {
            "nom": self.nom,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> 'Personnage':
        return cls(data['nom'], data['description'])