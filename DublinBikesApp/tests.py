import app
import unittest
import helpers
from datetime import datetime

# IDE sometimes says app stuff doesn't exist but works
# Run with python -m unittest tests


class RouteTester(unittest.TestCase):

    # Set up app for testing
    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    # Test status code response from home page
    def testHome(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)


class HelpersTester(unittest.TestCase):

    # Test that datetime converts to epoch correctly
    def testFormatDateTimeEpoch(self):
        t = (datetime(2019, 4, 21, 15, 15), 6)
        self.assertEqual(helpers.formatDateTime(t)[0], 1555856100)

    # Test that datetime formatter returns correct day
    def testFormatDateTimeDay(self):
        t = (datetime(2019, 4, 21, 15, 15), 6)
        self.assertEqual(helpers.formatDateTime(t)[1], 6)

    # Test that weatherinfo formatter returns correct data for mach learning
    def testFormatWeatherInfo(self):
        t = 1555856100
        d = 6
        w = {'dt': 1555858800, 'main': {'temp': 19.25, 'temp_min': 19.25, 'temp_max': 19.25, 'pressure': 1015.986, 'sea_level': 1015.986, 'grnd_level': 1006.732, 'humidity': 67, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 88}, 'wind': {'speed': 5.31, 'deg': 198.227}, 'sys': {'pod': 'd'}, 'dt_txt': '2019-04-21 15:00:00'}
        self.assertEqual(helpers.formatWeatherInfo(w, t, d), [1555856100, 6, 1, 17, 19.25, 5.31, 88])



if __name__ == "main":
    unittest.main()
