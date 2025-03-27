"""Weather display implementations."""

from typing import List
from .weather_observer import WeatherObserver
from .weather_station import WeatherStation


class CurrentConditionsDisplay(WeatherObserver):
    """Display current weather conditions."""

    def __init__(self, weather_station: WeatherStation) -> None:
        """Initialize the current conditions display."""
        super().__init__(weather_station)
        self.temperature = 0.0
        self.humidity = 0.0

    def update(self, subject: WeatherStation = None, **kwargs) -> None:
        """Update the display with current weather conditions."""
        self.temperature = kwargs.get('temperature', 0.0)
        self.humidity = kwargs.get('humidity', 0.0)
        print(f"Current conditions: {self.temperature}°F and {self.humidity}% humidity")


class StatisticsDisplay(WeatherObserver):
    """Display weather statistics."""

    def __init__(self, weather_station: WeatherStation) -> None:
        """Initialize the statistics display."""
        super().__init__(weather_station)
        self.temperatures = []
        self.humidities = []
        self.num_readings = 0
        self.min_temp = float('inf')
        self.max_temp = float('-inf')
        self.sum_temp = 0.0
        self.temperature_readings = []

    def update(self, subject: WeatherStation = None, **kwargs) -> None:
        """Update the display with weather statistics."""
        temp = kwargs.get('temperature')
        humidity = kwargs.get('humidity')

        self.temperatures.append(temp)
        self.humidities.append(humidity)
        self.num_readings += 1

        self.min_temp = min(self.min_temp, temp)
        self.max_temp = max(self.max_temp, temp)
        self.sum_temp += temp
        self.temperature_readings.append(temp)

        avg_temp = sum(self.temperatures) / len(self.temperatures)
        avg_humidity = sum(self.humidities) / len(self.humidities)

        print(
            f"Avg/Current: Temperature {avg_temp}°F/{temp}°F, Humidity {avg_humidity}%/{humidity}%")


class ForecastDisplay(WeatherObserver):
    """Display weather forecast."""

    def __init__(self, weather_station: WeatherStation) -> None:
        """Initialize the forecast display."""
        super().__init__(weather_station)
        self._last_pressure = 0.0

    def update(self, subject: WeatherStation = None, **kwargs) -> None:
        """Update the display with weather forecast."""
        pressure = kwargs.get('pressure', 0.0)
        if self._last_pressure == 0.0:
            self._last_pressure = pressure
            print("Forecast: Waiting for more data")
            return

        if pressure > self._last_pressure:
            print("Forecast: Improving weather on the way!")
        else:
            print("Forecast: Watch out for cooler, rainy weather")
        self._last_pressure = pressure


class HeatIndexDisplay(WeatherObserver):
    """Display heat index."""

    def __init__(self, weather_station: WeatherStation) -> None:
        """Initialize the heat index display."""
        super().__init__(weather_station)
        self.heat_index = 0.0

    def update(self, subject: WeatherStation = None, **kwargs) -> None:
        """Update the display with heat index."""
        temp = kwargs.get('temperature')
        humidity = kwargs.get('humidity')

        # Calculate heat index using the formula
        self.heat_index = self._compute_heat_index(temp, humidity)
        print(f"Heat Index is {self.heat_index}°F")

    def _compute_heat_index(self, t, rh):
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
