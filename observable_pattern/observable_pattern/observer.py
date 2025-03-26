"""
Observer Interface and abstract class definition.
"""
from abc import ABC, abstractmethod
from typing import Any


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects
    to notify observers of changes.
    """
    @abstractmethod
    def update(self, subject: Any = None, **kwargs) -> None:
        """
        Receive update from subject.
        
        Args:
            subject: Optional reference to the Subject that triggered the update
            **kwargs: Any additional data the subject may send
        """
        pass 