"""
Subject Interface and abstract class definition.
"""

from abc import ABC
from typing import List
from .observer import Observer


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing observers.
    """

    def __init__(self) -> None:
        """Initialize an empty list of observers."""
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.

        Args:
            observer: The observer to attach
        """
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.

        Args:
            observer: The observer to detach
        """
        self._observers.remove(observer)

    def notify(self, **kwargs) -> None:
        """
        Notify all observers about an event.

        Args:
            **kwargs: Data to pass to observers
        """
        for observer in self._observers:
            observer.update(self, **kwargs)
