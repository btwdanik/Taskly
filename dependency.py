from datetime import datetime
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Schema:
    description: str
    id: str = "0"
    status: str = 'In progress'
    createdAt: datetime = field(default_factory=datetime.now)
    updatedAt: datetime = field(default_factory=datetime.now)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt.replace(microsecond=0).isoformat(),
            "updatedAt": self.updatedAt.replace(microsecond=0).isoformat()
        }
