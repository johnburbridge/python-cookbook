#!/usr/bin/env python3
"""
This script demonstrates the Observable Pattern using a weather station and
various display elements. It shows how observers can subscribe to changes
from a subject and be notified automatically.
"""
from observable_pattern.weather_station import WeatherStation
from observable_pattern.weather_displays import (
    CurrentConditionsDisplay,
    StatisticsDisplay,
    ForecastDisplay,
    HeatIndexDisplay,
)


def demonstrate_observer_pattern():
    """
    Demonstrate the Observable Pattern with a weather monitoring system.
    """
    print("\n=== OBSERVABLE PATTERN DEMONSTRATION ===\n")

    # Create the subject (the weather station)
    weather_station = WeatherStation()

    # Create the displays (observers)
    current_display = CurrentConditionsDisplay(weather_station)
    statistics_display = StatisticsDisplay(weather_station)
    forecast_display = ForecastDisplay(weather_station)
    print(f"Created displays: {current_display.__class__.__name__}, "
          f"{statistics_display.__class__.__name__}, "
          f"{forecast_display.__class__.__name__}")

    print("\n--- Initial Weather Update ---")
    # Weather data changes, observers are notified automatically
    weather_station.set_measurements(80, 65, 30.4)

    print("\n--- Second Weather Update ---")
    # Weather data changes again
    weather_station.set_measurements(82, 70, 29.2)

    print("\n--- Adding Heat Index Display ---")
    # Add a new observer at runtime
    heat_index_display = HeatIndexDisplay(weather_station)
    print(f"Added {heat_index_display.__class__.__name__}")

    print("\n--- Third Weather Update (All Displays) ---")
    # Now all four displays will update
    weather_station.set_measurements(78, 90, 29.2)

    print("\n--- Removing Forecast Display ---")
    # Dynamically remove an observer
    weather_station.detach(forecast_display)

    print("\n--- Fourth Weather Update (Without Forecast) ---")
    # Now only three displays will update
    weather_station.set_measurements(62, 45, 29.4)


def demonstrate_push_vs_pull():
    """
    Demonstrate the push versus pull approaches in the Observable Pattern.
    """
    print("\n=== PUSH VS PULL MODEL DEMONSTRATION ===\n")

    weather_station = WeatherStation()

    print(
        "Push Model: CurrentConditionsDisplay receives data directly in "
        "update() method"
    )
    print(
        "Pull Model: StatisticsDisplay requests data directly from the "
        "subject\n"
    )

    current_display = CurrentConditionsDisplay(weather_station)
    statistics_display = StatisticsDisplay(weather_station)
    print(f"Created displays: {current_display.__class__.__name__}, "
          f"{statistics_display.__class__.__name__}")

    print("--- Weather Update (Both Models) ---")
    weather_station.set_measurements(75, 60, 30.1)


def main() -> None:
    """Run the weather station demo."""
    print("=== Weather Station Demo ===\n")

    # Create the WeatherStation (the Subject)
    weather_station = WeatherStation()

    # Create and register the display elements (the Observers)
    CurrentConditionsDisplay(weather_station)
    StatisticsDisplay(weather_station)
    forecast_display = ForecastDisplay(weather_station)
    HeatIndexDisplay(weather_station)

    print("Initial weather measurements:")
    weather_station.set_measurements(80, 65, 30.4)

    print("\nWeather update 1:")
    weather_station.set_measurements(82, 70, 29.2)

    print("\nWeather update 2:")
    weather_station.set_measurements(78, 90, 29.2)

    # Demonstrate unregistering observers
    print("\nUnregistering forecast display...")
    forecast_display.unregister()

    print("\nFinal weather update:")
    weather_station.set_measurements(62, 90, 28.1)


if __name__ == "__main__":
    main()
