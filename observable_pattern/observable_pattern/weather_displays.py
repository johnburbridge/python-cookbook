"""Weather display implementations."""

from abc import ABC
from typing import List
from .observer import Observer
from .weather_station import WeatherStation


class WeatherObserver(Observer, ABC):
    """Base class for weather observers."""

    def __init__(self, weather_station: WeatherStation) -> None:
        """
        Initialize the weather observer.

        Args:
            weather_station: The weather station to observe
        """
        self._weather_station = weather_station
        self._weather_station.add_observer(self)

    def unregister(self) -> None:
        """Unregister this observer from the weather station."""
        self._weather_station.remove_observer(self)


class CurrentConditionsDisplay(WeatherObserver):
    """Display current weather conditions."""

    def update(self) -> None:
        """Update the display with current weather conditions."""
        temp = self._weather_station.temperature
        humidity = self._weather_station.humidity
        print(f"Current conditions: {temp}°F and {humidity}% humidity")


class StatisticsDisplay(WeatherObserver):
    """Display weather statistics."""

    def __init__(self, weather_station: WeatherStation) -> None:
        """Initialize the statistics display."""
        super().__init__(weather_station)
        self._temperatures: List[float] = []
        self._humidities: List[float] = []

    def update(self) -> None:
        """Update the display with weather statistics."""
        temp = self._weather_station.temperature
        humidity = self._weather_station.humidity

        self._temperatures.append(temp)
        self._humidities.append(humidity)

        avg_temp = sum(self._temperatures) / len(self._temperatures)
        avg_humidity = sum(self._humidities) / len(self._humidities)

        print(
            f"Avg/Current: Temperature {avg_temp:.1f}°F/{temp}°F, "
            f"Humidity {avg_humidity:.1f}%/{humidity}%"
        )


class ForecastDisplay(WeatherObserver):
    """Display weather forecast."""

    def __init__(self, weather_station: WeatherStation) -> None:
        """Initialize the forecast display."""
        super().__init__(weather_station)
        self._last_pressure = 0.0

    def update(self) -> None:
        """Update the display with weather forecast."""
        pressure = self._weather_station.pressure
        forecast = "Improving" if pressure > self._last_pressure else "Worsening"
        self._last_pressure = pressure
        print(f"Forecast: {forecast} weather ahead")


class HeatIndexDisplay(WeatherObserver):
    """Display heat index."""

    def update(self) -> None:
        """Update the display with heat index."""
        temp = self._weather_station.temperature
        humidity = self._weather_station.humidity
        heat_index = self._compute_heat_index(temp, humidity)
        print(f"Heat index: {heat_index:.1f}°F")

    def _compute_heat_index(self, t: float, rh: float) -> float:
        """
        Compute the heat index using temperature and relative humidity.

        Args:
            t: Temperature in Fahrenheit
            rh: Relative humidity percentage

        Returns:
            The heat index in Fahrenheit
        """
        return (
            (16.923 + (0.185212 * t))
            + (5.37941 * rh)
            - (0.100254 * t * rh)
            + (0.00941695 * (t * t))
            + (0.00728898 * (rh * rh))
            + (0.000345372 * (t * t * rh))
            - (0.000814971 * (t * rh * rh))
            + (0.0000102102 * (t * t * rh * rh))
            - (0.000038646 * (t * t * t))
            + (0.0000291583 * (rh * rh * rh))
            + (0.00000142721 * (t * t * t * rh))
            + (0.000000197483 * (t * rh * rh * rh))
            - (0.0000000218429 * (t * t * t * rh * rh))
            + 0.000000000843296 * (t * t * rh * rh * rh)
            - 0.0000000000481975 * (t * t * t * rh * rh * rh)
        )

    def display(self) -> str:
        """
        Format and display the heat index.

        Returns:
            Formatted string with the heat index
        """
        message = f"Heat Index is {self.heat_index}°F"
        print(message)
        return message
