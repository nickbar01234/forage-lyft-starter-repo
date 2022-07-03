from typing import Type
import unittest

from engine import Engine, CapuletEngine, SternmanEngine, WilloughbyEngine

class TestCapuletEngine(unittest.TestCase):
    def test_is_engine(self):
        capulet = CapuletEngine(0, 0)
        self.assertIsInstance(capulet, Engine)

    def test_threshold(self):
        threshold = 30000
        capulet = CapuletEngine(0, 0)
        self.assertEqual(capulet.threshold, threshold)
    
    def test_needs_service(self):
        capulet = CapuletEngine(50000, 0)
        self.assertTrue(capulet.needs_service(), "Expected service")
    
    def test_does_not_need_service(self):
        capulet = CapuletEngine(25000, 100)
        self.assertFalse(capulet.needs_service(), "Does not need service")
    
    def test_missing_current_mileage_raise_type_error(self):
        with self.assertRaises(TypeError):
            capulet = CapuletEngine(last_service_mileage = 0)

    def test_missing_last_service_mileage_raise_type_error(self):
        with self.assertRaises(TypeError):
            capulet = CapuletEngine(current_mileage = 0)

class TestSternmanEngine(unittest.TestCase):

    def test_is_engine(self):
        sternman = SternmanEngine(False) 
        self.assertIsInstance(sternman, Engine)

    def test_needs_service(self):
        sternman = SternmanEngine(True)
        self.assertTrue(sternman.needs_service(), "Expected service")


    def test_does_not_need_service(self):
        sternman = SternmanEngine(False)
        self.assertFalse(sternman.needs_service(), "Does not need service")

    def test_missing_warning_light_raise_type_error(self):
        with self.assertRaises(TypeError):
            sternman = SternmanEngine()

class TestWilloughbyEngine(unittest.TestCase):

    def test_is_engine(self):
        willoughby = WilloughbyEngine(0, 0)
        self.assertIsInstance(willoughby, Engine)

    def test_threshold(self):
        threshold = 60000
        willoughby = WilloughbyEngine(0, 0)
        self.assertEqual(
            willoughby.threshold,
            threshold,
            f"Expected threshold to be {threshold} but found {willoughby.threshold}"
        )
    
    def test_needs_service(self):
        willoughby = WilloughbyEngine(70000, 0)
        self.assertTrue(willoughby.needs_service(), "Expected service")
    
    def test_does_not_need_service(self):
        willoughby = WilloughbyEngine(55000, 1000)
        self.assertFalse(willoughby.needs_service(), "Does not need service")
    
    def test_missing_current_mileage_raise_type_error(self):
        with self.assertRaises(TypeError):
            willoughby = WilloughbyEngine(last_service_mileage = 0)

    def test_missing_last_service_mileage_raise_type_error(self):
        with self.assertRaises(TypeError):
            willoughby = WilloughbyEngine(current_mileage = 0)

if __name__ == "__main__":
    unittest.main()