import unittest
from weather import process_weather_data

class TestWeatherDataProcessing(unittest.TestCase):
    
    def test_process_weather_data_valid(self):
        # Simulate a valid API response
        sample_data = {
            'main': {'temp': 300.15, 'feels_like': 303.15},
            'weather': [{'main': 'Clear'}],
            'name': 'TestCity',
            'dt': 1632991212
        }
        result = process_weather_data(sample_data)
        self.assertEqual(result['city'], 'TestCity')
        self.assertAlmostEqual(result['temperature'], 27.0, places=1)
        self.assertEqual(result['condition'], 'Clear')

    def test_process_weather_data_missing_data(self):
        # Simulate an API response with missing data
        sample_data = {
            'main': {},
            'weather': [{}],
            'name': 'TestCity',
            'dt': 1632991212
        }
        result = process_weather_data(sample_data)
        self.assertIsNone(result)  # Should return None if data is missing

if __name__ == '__main__':
    unittest.main()
