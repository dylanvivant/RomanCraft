from datetime import datetime
from typing import Dict, Any

class Idee:
    def __init__(self, contenu: str):
        self.contenu: str = contenu
        self.date_creation: datetime = datetime.now()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "contenu": self.contenu,
            "date_creation": self.date_creation.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Idee':
        idee = cls(data['contenu'])
        idee.date_creation = datetime.fromisoformat(data['date_creation'])
        return idee