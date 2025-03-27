"""Weather station implementation."""

from .subject import Subject


class WeatherStation(Subject):
    """Weather station that notifies observers of weather changes."""

    def __init__(self) -> None:
        """Initialize the weather station."""
        super().__init__()
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 29.92

    def set_measurements(
        self, temperature: float, humidity: float, pressure: float
    ) -> None:
        """
        Update weather measurements and notify observers.

        Args:
            temperature: Temperature in Fahrenheit
            humidity: Relative humidity percentage
            pressure: Barometric pressure
        """
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify(temperature=temperature, humidity=humidity, pressure=pressure)
