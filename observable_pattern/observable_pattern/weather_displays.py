"""
Concrete Observers for the weather monitoring system.
"""

from abc import ABC
from typing import List, Optional, Any

from observable_pattern.observer import Observer
from observable_pattern.weather_station import WeatherStation


class WeatherDisplay(Observer, ABC):
    """
    Base class for all weather displays.
    """

    def __init__(self, weather_station: WeatherStation):
        """
        Initialize the display and register it as an observer.

        Args:
            weather_station: The WeatherStation subject to observe
        """
        self.weather_station = weather_station
        self.weather_station.attach(self)


class CurrentConditionsDisplay(WeatherDisplay):
    """
    Display for showing current weather conditions.
    """

    def __init__(self, weather_station: WeatherStation):
        """
        Initialize with default values.
        """
        super().__init__(weather_station)
        self.temperature = 0.0
        self.humidity = 0.0

    def update(self, subject: Any = None, **kwargs) -> None:
        """
        Update the display with new weather data.

        This implementation uses the push model, accepting temperature and humidity
        as direct arguments from the subject's notification.

        Args:
            subject: The subject that triggered the update (optional)
            **kwargs: Data from the subject notification
        """
        if "temperature" in kwargs and "humidity" in kwargs:
            self.temperature = kwargs["temperature"]
            self.humidity = kwargs["humidity"]
            self.display()

    def display(self) -> str:
        """
        Format and display the current conditions.

        Returns:
            Formatted string with the current conditions
        """
        message = (
            f"Current conditions: {self.temperature}°F and {self.humidity}% humidity"
        )
        print(message)
        return message


class StatisticsDisplay(WeatherDisplay):
    """
    Display for showing statistical data about temperature readings.
    """

    def __init__(self, weather_station: WeatherStation):
        """
        Initialize with default values.
        """
        super().__init__(weather_station)
        self.temperature_readings: List[float] = []
        self.min_temp = float("inf")
        self.max_temp = float("-inf")
        self.sum_temp = 0.0
        self.num_readings = 0

    def update(self, subject: Any = None, **kwargs) -> None:
        """
        Update the statistics with new temperature data.

        This implementation demonstrates the pull model - it uses the subject reference
        to get the temperature directly, rather than relying on data passed in kwargs.

        Args:
            subject: The subject that triggered the update
            **kwargs: Data from the subject notification (not used in this implementation)
        """
        if isinstance(subject, WeatherStation):
            temp = subject.temperature
            self.temperature_readings.append(temp)
            self.num_readings += 1
            self.sum_temp += temp

            if temp < self.min_temp:
                self.min_temp = temp
            if temp > self.max_temp:
                self.max_temp = temp

            self.display()

    def display(self) -> str:
        """
        Format and display the temperature statistics.

        Returns:
            Formatted string with the temperature statistics
        """
        if self.num_readings == 0:
            message = "No temperature readings recorded yet"
        else:
            avg = self.sum_temp / self.num_readings
            message = (
                f"Temperature Statistics: Avg/Max/Min = {avg:.1f}°F/"
                f"{self.max_temp}°F/{self.min_temp}°F"
            )
        print(message)
        return message


class ForecastDisplay(WeatherDisplay):
    """
    Display for showing weather forecast based on barometric pressure.
    """

    def __init__(self, weather_station: WeatherStation):
        """
        Initialize with default values.
        """
        super().__init__(weather_station)
        self.current_pressure = 29.92  # Default pressure
        self.last_pressure: Optional[float] = None

    def update(self, subject: Any = None, **kwargs) -> None:
        """
        Update the forecast based on pressure changes.

        Args:
            subject: The subject that triggered the update (optional)
            **kwargs: Data from the subject notification
        """
        if "pressure" in kwargs:
            self.last_pressure = self.current_pressure
            self.current_pressure = kwargs["pressure"]
            self.display()

    def display(self) -> str:
        """
        Format and display the weather forecast.

        Returns:
            Formatted string with the weather forecast
        """
        forecast = "Forecast: "
        if self.last_pressure is None:
            forecast += "Not enough data for forecast"
        elif self.current_pressure > self.last_pressure:
            forecast += "Improving weather on the way!"
        elif self.current_pressure == self.last_pressure:
            forecast += "More of the same"
        else:
            forecast += "Watch out for cooler, rainy weather"

        print(forecast)
        return forecast


class HeatIndexDisplay(WeatherDisplay):
    """
    Display for showing the heat index (feels-like temperature).
    """

    def __init__(self, weather_station: WeatherStation):
        """
        Initialize with default values.
        """
        super().__init__(weather_station)
        self.heat_index = 0.0

    def update(self, subject: Any = None, **kwargs) -> None:
        """
        Update the heat index based on temperature and humidity.

        Args:
            subject: The subject that triggered the update (optional)
            **kwargs: Data from the subject notification
        """
        if "temperature" in kwargs and "humidity" in kwargs:
            temp = kwargs["temperature"]
            humidity = kwargs["humidity"]

            # Calculate heat index using the formula from the National Weather Service
            self.heat_index = self.compute_heat_index(temp, humidity)
            self.display()

    def compute_heat_index(self, t: float, rh: float) -> float:
        """
        Compute the heat index using the NWS formula.

        Args:
            t: Temperature in Fahrenheit
            rh: Relative humidity (percentage)

        Returns:
            Heat index value
        """
        index = (
            16.923
            + (0.185212 * t)
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
            + (0.000000000843296 * (t * t * rh * rh * rh))
            - (0.0000000000481975 * (t * t * t * rh * rh * rh))
        )
        return round(index, 1)

    def display(self) -> str:
        """
        Format and display the heat index.

        Returns:
            Formatted string with the heat index
        """
        message = f"Heat Index is {self.heat_index}°F"
        print(message)
        return message
