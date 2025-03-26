"""
Unit tests for the Observable Pattern implementation in the weather monitoring system.
"""
import unittest
from unittest.mock import patch, MagicMock

from observable_pattern.weather_station import WeatherStation
from observable_pattern.weather_displays import (
    CurrentConditionsDisplay,
    StatisticsDisplay,
    ForecastDisplay,
    HeatIndexDisplay
)


class TestWeatherStation(unittest.TestCase):
    """
    Test cases for the WeatherStation class.
    """
    def setUp(self):
        """
        Set up a fresh weather station for each test.
        """
        self.weather_station = WeatherStation()
    
    def test_initial_values(self):
        """
        Test that the weather station initializes with default values.
        """
        self.assertEqual(self.weather_station.temperature, 0.0)
        self.assertEqual(self.weather_station.humidity, 0.0)
        self.assertEqual(self.weather_station.pressure, 0.0)
    
    def test_set_measurements(self):
        """
        Test that set_measurements updates the weather station properties.
        """
        self.weather_station.set_measurements(70.0, 60.0, 30.0)
        
        self.assertEqual(self.weather_station.temperature, 70.0)
        self.assertEqual(self.weather_station.humidity, 60.0)
        self.assertEqual(self.weather_station.pressure, 30.0)
    
    def test_observer_notified(self):
        """
        Test that observers are notified when measurements change.
        """
        # Create a mock observer
        mock_observer = MagicMock()
        
        # Attach the mock observer to the weather station
        self.weather_station.attach(mock_observer)
        
        # Change the measurements
        self.weather_station.set_measurements(75.0, 65.0, 30.5)
        
        # Verify the observer was called with the correct arguments
        mock_observer.update.assert_called_once_with(
            self.weather_station,
            temperature=75.0,
            humidity=65.0,
            pressure=30.5
        )
    
    def test_observer_detached(self):
        """
        Test that detached observers are not notified.
        """
        # Create a mock observer
        mock_observer = MagicMock()
        
        # Attach the mock observer to the weather station
        self.weather_station.attach(mock_observer)
        
        # Detach the observer
        self.weather_station.detach(mock_observer)
        
        # Change the measurements
        self.weather_station.set_measurements(75.0, 65.0, 30.5)
        
        # Verify the observer was not called
        mock_observer.update.assert_not_called()


class TestCurrentConditionsDisplay(unittest.TestCase):
    """
    Test cases for the CurrentConditionsDisplay class.
    """
    def setUp(self):
        """
        Set up a fresh weather station and display for each test.
        """
        self.weather_station = WeatherStation()
        self.display = CurrentConditionsDisplay(self.weather_station)
    
    @patch('builtins.print')
    def test_update(self, mock_print):
        """
        Test that the display updates correctly when notified.
        """
        # Update the weather station
        self.weather_station.set_measurements(70.0, 60.0, 30.0)
        
        # Check the display has been updated
        self.assertEqual(self.display.temperature, 70.0)
        self.assertEqual(self.display.humidity, 60.0)
        
        # Check that display() was called and printed correctly
        expected_output = "Current conditions: 70.0°F and 60.0% humidity"
        mock_print.assert_called_with(expected_output)


class TestStatisticsDisplay(unittest.TestCase):
    """
    Test cases for the StatisticsDisplay class.
    """
    def setUp(self):
        """
        Set up a fresh weather station and display for each test.
        """
        self.weather_station = WeatherStation()
        self.display = StatisticsDisplay(self.weather_station)
    
    def test_update_statistics(self):
        """
        Test that statistics are calculated correctly.
        """
        # Update with different temperatures
        self.weather_station.set_measurements(70.0, 60.0, 30.0)
        self.weather_station.set_measurements(75.0, 65.0, 30.5)
        self.weather_station.set_measurements(80.0, 70.0, 31.0)
        
        # Check statistics
        self.assertEqual(self.display.num_readings, 3)
        self.assertEqual(self.display.min_temp, 70.0)
        self.assertEqual(self.display.max_temp, 80.0)
        self.assertEqual(self.display.sum_temp, 225.0)
        self.assertEqual(self.display.temperature_readings, [70.0, 75.0, 80.0])


class TestForecastDisplay(unittest.TestCase):
    """
    Test cases for the ForecastDisplay class.
    """
    def setUp(self):
        """
        Set up a fresh weather station and display for each test.
        """
        self.weather_station = WeatherStation()
        self.display = ForecastDisplay(self.weather_station)
    
    @patch('builtins.print')
    def test_pressure_increasing(self, mock_print):
        """
        Test forecast when pressure is increasing.
        """
        # First update establishes baseline
        self.weather_station.set_measurements(70.0, 60.0, 30.0)
        mock_print.reset_mock()
        
        # Increase pressure
        self.weather_station.set_measurements(70.0, 60.0, 30.5)
        
        # Check forecast
        mock_print.assert_called_with("Forecast: Improving weather on the way!")
    
    @patch('builtins.print')
    def test_pressure_decreasing(self, mock_print):
        """
        Test forecast when pressure is decreasing.
        """
        # First update establishes baseline
        self.weather_station.set_measurements(70.0, 60.0, 30.0)
        mock_print.reset_mock()
        
        # Decrease pressure
        self.weather_station.set_measurements(70.0, 60.0, 29.5)
        
        # Check forecast
        mock_print.assert_called_with("Forecast: Watch out for cooler, rainy weather")


class TestHeatIndexDisplay(unittest.TestCase):
    """
    Test cases for the HeatIndexDisplay class.
    """
    def setUp(self):
        """
        Set up a fresh weather station and display for each test.
        """
        self.weather_station = WeatherStation()
        self.display = HeatIndexDisplay(self.weather_station)
    
    def test_heat_index_calculation(self):
        """
        Test heat index calculation.
        """
        # Update weather data
        self.weather_station.set_measurements(80.0, 65.0, 30.0)
        
        # Check heat index is calculated correctly
        # This is an approximation, may need to adjust epsilon
        self.assertAlmostEqual(self.display.heat_index, 83.0, places=1)
    
    @patch('builtins.print')
    def test_display_output(self, mock_print):
        """
        Test display output.
        """
        # Update weather data
        self.weather_station.set_measurements(80.0, 65.0, 30.0)
        
        # Check display output
        expected_output = f"Heat Index is {self.display.heat_index}°F"
        mock_print.assert_called_with(expected_output)


if __name__ == '__main__':
    unittest.main() 