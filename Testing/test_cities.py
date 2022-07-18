import unittest
from city_functions import locations

class CitiesTestCase(unittest.TestCase):
    """Test's for city_functions.py"""
    
    def test_city_country(self):
        city_country = locations('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')
    
    def test_city_country_population(self):
        city_country_population = locations('santiago', 'chile', 5000000)
        self.assertEqual(city_country_population, "Santiago, Chile - 5000000")

unittest.main()