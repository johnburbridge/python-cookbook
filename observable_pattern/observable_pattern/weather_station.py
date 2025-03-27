"""
Concrete Subject implementation for the weather monitoring system.
"""

from typing import List
from .subject import Subject
from .observer import Observer


class WeatherStation(Subject):
    """
    The WeatherStation class is a concrete subject that maintains weather data
    and notifies observers when the data changes.
    """

    def __init__(self) -> None:
        """
        Initialize the weather station with default values.
        """
        super().__init__()
        self._temperature: float = 0.0
        self._humidity: float = 0.0
        self._pressure: float = 0.0

    @property
    def temperature(self) -> float:
        """Get the current temperature."""
        return self._temperature

    @property
    def humidity(self) -> float:
        """Get the current humidity."""
        return self._humidity

    @property
    def pressure(self) -> float:
        """Get the current pressure."""
        return self._pressure

    def set_measurements(
        self,
        temperature: float,
        humidity: float,
        pressure: float,
    ) -> None:
        """
        Set new weather measurements.

        Args:
            temperature: The current temperature in Fahrenheit
            humidity: The current humidity percentage
            pressure: The current pressure in inches of mercury
        """
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify(
            temperature=self._temperature,
            humidity=self._humidity,
            pressure=self._pressure,
        )

    def measurements_changed(self) -> None:
        """
        Notify observers when measurements have changed.

        This demonstrates both push and pull models:
        - Push: We pass the data directly to the observers
        - Pull: Observers can use the provided reference to the subject
          to request specific data they need
        """
        self.notify(
            temperature=self._temperature,
            humidity=self._humidity,
            pressure=self._pressure,
        )
