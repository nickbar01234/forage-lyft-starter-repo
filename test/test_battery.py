import unittest
import datetime

from battery import Battery, SpindlerBattery, NubbinBattery

class TestSpindlerBaterry(unittest.TestCase):

    def test_is_battery(self):
        spindler = SpindlerBattery(None, None)
        self.assertIsInstance(spindler, Battery)
    
    def test_service_cycle_is_2_year(self):
        threshold = 2
        spindler = SpindlerBattery(None, None)
        self.assertEqual(spindler.threshold, threshold)
    
    def test_needs_service(self):
        spindler = SpindlerBattery(
            datetime.datetime.now(), datetime.datetime(2020, 1, 1)
        )
        self.assertTrue(spindler.needs_service(), "Expected service")
    
    def test_does_not_need_service(self):
        spindler = SpindlerBattery(
            datetime.datetime.now(), datetime.datetime.now()
        )
        self.assertFalse(spindler.needs_service(), "Does not need service")
    
    def test_missing_current_date_raise_error(self):
        with self.assertRaises(TypeError):
            spindler = SpindlerBattery(last_service_date = None)

    def test_missing_last_service_date_raise_error(self):
        with self.assertRaises(TypeError):
            spindler = SpindlerBattery(current_date = None)

class TestNubbinBattery(unittest.TestCase):

    def test_is_battery(self):
        nubbin = NubbinBattery(None, None)
        self.assertIsInstance(nubbin, Battery)
    
    def test_service_cycle_is_4_year(self):
        threshold = 4
        nubbin = NubbinBattery(None, None)
        self.assertEqual(nubbin.threshold, threshold)
    
    def test_needs_service(self):
        nubbin = NubbinBattery(
            datetime.datetime.now(), datetime.datetime(2018, 1, 1)
        )
        self.assertTrue(nubbin.needs_service(), "Expected service")
    
    def test_does_not_need_service(self):
        nubbin = NubbinBattery(
            datetime.datetime.now(), datetime.datetime.now()
        )
        self.assertFalse(nubbin.needs_service(), "Does not need service")
    
    def test_missing_current_date_raise_error(self):
        with self.assertRaises(TypeError):
            nubbin = NubbinBattery(last_service_date = None)

    def test_missing_last_service_date_raise_error(self):
        with self.assertRaises(TypeError):
            nubbin = NubbinBattery(current_date = None)
 
if __name__ == "__main__":
    unittest.main()