import unittest
from city_functions import locations

class CitiesTestCase(unittest.TestCase):
    """Test's for city_functions.py"""
    
    def test_city_country(self):
        city_country = locations('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')
    

unittest.main()