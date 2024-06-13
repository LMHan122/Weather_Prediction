import unittest
from weather import Weather, Base, User

class Test_Weather(unittest.TestCase):

    def test_weather_defaults(self):
        weather = Weather()
        self.assertEqual(weather.lat, 32.7)
        self.assertEqual(weather.long, -97.3)
        self.assertEqual(weather.month, 7)
        self.assertEqual(weather.day, 7)
        self.assertEqual(weather.year, 2024)
        self.assertEqual(weather.avg_temp, 0.0)
        self.assertEqual(weather.min_temp, 0.0)
        self.assertEqual(weather.max_temp, 0.0)
        self.assertEqual(weather.avg_wind_speed, 0.0)
        self.assertEqual(weather.min_wind_speed, 0.0)
        self.assertEqual(weather.max_wind_speed, 0.0)
        self.assertEqual(weather.sum_precip, 0.0)
        self.assertEqual(weather.min_precip, 0.0)
        self.assertEqual(weather.max_precip, 0.0)

    def test_five_yr_temp(self):
        weather1 = Weather()

        weather1.temp_data = [23.0, 42.0, 108.0, 7.0, 18.0]

        weather1.avg_temp = round(sum(weather1.temp_data) / len(weather1.temp_data), 1)
        weather1.min_temp = min(weather1.temp_data)
        weather1.max_temp = max(weather1.temp_data)

        self.assertEqual(weather1.avg_temp, 39.6)
        self.assertEqual(weather1.min_temp, 7.0)
        self.assertEqual(weather1.max_temp, 108.0)

    def test_weather_params(self):
        weather = Weather(lat=4.0, long=-200.0, month=1, day=15, year=2020)
        self.assertEqual(weather.lat, 4.0)
        self.assertEqual(weather.long, -200.0)
        self.assertEqual(weather.month, 1)
        self.assertEqual(weather.day, 15)
        self.assertEqual(weather.year, 2020)

if __name__ == '__main__':
    unittest.main()

