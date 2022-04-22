import unittest
from datetime import datetime

from battery.battery import SpindlerBattery, NubbinBattery
from engine.engine import CapuletEngine, SternmanEngine, WilloughbyEngine

# Batteries Test
class Test_spindlerBattery(unittest.TestCase):
    def test_needs_serviceTrue(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)

        Battery = SpindlerBattery(last_service_date.year, current_date.year)
        self.assertTrue(Battery.needs_service())

    def test_needs_service_false(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)

        Battery = SpindlerBattery(last_service_date.year, current_date.year)
        self.assertFalse(Battery.needs_service())

class Test_nubbinBattery(unittest.TestCase):
    def test_needs_service_True(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)

        Battery = NubbinBattery(last_service_date.year, current_date.year)
        self.assertTrue(Battery.needs_service())
        
    def test_needs_service_false(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        
        Battery = NubbinBattery(last_service_date.year, current_date.year)
        self.assertFalse(Battery.needs_service())

# Engines Test
class Test_capuletEngine(unittest.TestCase):
    def test_needs_service_True(self):
        current_mileage = 30001
        last_service_mileage = 0

        Engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(Engine.needs_service())
    
    def test_needs_service_false(self):
        current_mileage = 30000
        last_service_mileage = 0

        Engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(Engine.needs_service())

class Test_sternmanEngine(unittest.TestCase):
    def test_needs_service_True(self):
        warning_light_is_on = True

        Engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(Engine.needs_service())
    
    def test_needs_service_false(self):
        warning_light_is_on = False

        Engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(Engine.needs_service())

class Test_willoughbyEngine(unittest.TestCase):
    def test_needs_service_True(self):
        current_mileage = 60001
        last_service_mileage = 0

        Engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(Engine.needs_service())
    
    def test_needs_service_false(self):
        current_mileage = 60000
        last_service_mileage = 0

        Engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(Engine.needs_service())

if __name__ == '__main__':
    unittest.main()
