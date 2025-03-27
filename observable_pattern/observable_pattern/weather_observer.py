"""Weather observer interface."""

from abc import ABC, abstractmethod
from typing import Any, Optional
from .weather_station import WeatherStation


class WeatherObserver(ABC):
    """Abstract base class for weather observers."""

    def __init__(self) -> None:
        """Initialize the observer."""
        pass

    @abstractmethod
    def update(self, subject: Optional[WeatherStation] = None, **kwargs: Any) -> None:
        """
        Update the observer with new weather data.

        Args:
            subject: The subject that triggered the update
            **kwargs: Additional data from the subject
        """
        pass
