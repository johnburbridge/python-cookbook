"""Base class for weather observers."""

from abc import ABC
from typing import Any
from .observer import Observer


class WeatherObserver(Observer, ABC):
    """Base class for weather observers."""

    def __init__(self, weather_station) -> None:
        """
        Initialize the weather observer.

        Args:
            weather_station: The weather station to observe
        """
        self._weather_station = weather_station
        self._weather_station.attach(self)

    def unregister(self) -> None:
        """Unregister this observer from the weather station."""
        self._weather_station.detach(self)

    def update(self, subject: Any = None, **kwargs) -> None:
        """
        Receive update from subject.

        Args:
            subject: Optional reference to the Subject that triggered the update
            **kwargs: Any additional data the subject may send
        """
        pass
