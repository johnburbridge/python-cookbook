"""Weather station implementation."""

from .subject import Subject


class WeatherStation(Subject):
    """Weather station that notifies observers of weather changes."""

    def __init__(self) -> None:
        """Initialize the weather station."""
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
        self,
        temperature: float,
        humidity: float,
        pressure: float
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
        self.notify(
            temperature=temperature,
            humidity=humidity,
            pressure=pressure
        )
