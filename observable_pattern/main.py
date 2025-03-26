#!/usr/bin/env python3
"""
This script demonstrates the Observable Pattern using a weather station and various display elements.
It shows how observers can subscribe to changes from a subject and be notified automatically.
"""
from observable_pattern.weather_station import WeatherStation
from observable_pattern.weather_displays import (
    CurrentConditionsDisplay,
    StatisticsDisplay,
    ForecastDisplay,
    HeatIndexDisplay
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
    
    print("\n--- Initial Weather Update ---")
    # Weather data changes, observers are notified automatically
    weather_station.set_measurements(80, 65, 30.4)
    
    print("\n--- Second Weather Update ---")
    # Weather data changes again
    weather_station.set_measurements(82, 70, 29.2)
    
    print("\n--- Adding Heat Index Display ---")
    # Add a new observer at runtime
    heat_index_display = HeatIndexDisplay(weather_station)
    
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
    
    print("Push Model: CurrentConditionsDisplay receives data directly in update() method")
    print("Pull Model: StatisticsDisplay requests data directly from the subject\n")
    
    current_display = CurrentConditionsDisplay(weather_station)
    statistics_display = StatisticsDisplay(weather_station)
    
    print("--- Weather Update (Both Models) ---")
    weather_station.set_measurements(75, 60, 30.1)


def main():
    """
    Main function to demonstrate the Observable Pattern.
    """
    print("Observable Pattern Demo")
    print("======================")
    print("This demo shows how the Observable Pattern allows subjects to notify")
    print("multiple observers automatically when their state changes.")
    
    # Demonstrate the basic observable pattern
    demonstrate_observer_pattern()
    
    # Demonstrate push vs pull approaches
    demonstrate_push_vs_pull()
    
    print("\nObservable Pattern Benefits:")
    print("1. Loose coupling between subject and observers")
    print("2. Observers can be added and removed dynamically")
    print("3. One subject can update multiple observers simultaneously")
    print("4. New types of observers can be added without modifying the subject")


if __name__ == "__main__":
    main() 