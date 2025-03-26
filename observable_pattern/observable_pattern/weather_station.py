"""
Concrete Subject implementation for the weather monitoring system.
"""

from typing import Dict, Any

from .subject import Subject
from observable_pattern.observer import Observer


class WeatherStation(Subject):
    """
    The WeatherStation class is a concrete subject that maintains weather data
    and notifies observers when the data changes.
    """

    def __init__(self):
        """
        Initialize the weather station with default values.
        """
        super().__init__()
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 0.0

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
        self, temperature: float, humidity: float, pressure: float
    ) -> None:
        """
        Update weather measurements and notify all observers.

        Args:
            temperature: The new temperature in degrees Fahrenheit
            humidity: The new humidity percentage
            pressure: The new barometric pressure
        """
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure

        # Notify observers of the change with the new data
        self.measurements_changed()

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
