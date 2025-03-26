"""
Subject (Observable) interface and base class definition.
"""
from abc import ABC, abstractmethod
from typing import List, Set, Dict, Any

from observable_pattern.observer import Observer


class Subject(ABC):
    """
    The Subject interface declares methods for managing observers.
    """
    def __init__(self):
        """
        Initialize an empty list of observers.
        """
        self._observers: Set[Observer] = set()
    
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        
        Args:
            observer: The observer to attach
        """
        self._observers.add(observer)
    
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        
        Args:
            observer: The observer to detach
        """
        self._observers.discard(observer)
    
    def notify(self, **kwargs) -> None:
        """
        Notify all observers about an event.
        
        Args:
            **kwargs: Additional data to pass to observers
        """
        for observer in self._observers:
            observer.update(self, **kwargs) 