import unittest
from datetime import date

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from battery.spindler_battery import Spindler
from battery.nubbin_battery import Nubbin

from tire.carrigan import Carrigan
from tire.octoprime import OctoPrime


class TestEngines(unittest.TestCase):

    def test_capulet_engine(self):
        engine_true = CapuletEngine(30000, 0)
        engine_false = CapuletEngine(20000, 0)

        self.assertTrue(engine_true.needs_service())
        self.assertFalse(engine_false.needs_service())

    def test_willoughby_engine(self):
        engine_true = WilloughbyEngine(60000, 0)
        engine_false = WilloughbyEngine(50000, 0)

        self.assertTrue(engine_true.needs_service())
        self.assertFalse(engine_false.needs_service())

    def test_sternman_engine(self):
        engine_true = SternmanEngine(True)
        engine_false = SternmanEngine(False)

        self.assertTrue(engine_true.needs_service())
        self.assertFalse(engine_false.needs_service())


class TestBatteries(unittest.TestCase):

    def test_spindler_battery(self):
        battery_true = Spindler(date(2020, date.today().month, date.today().day))
        battery_false = Spindler(date(2022, date.today().month, date.today().day))

        self.assertTrue(battery_true.needs_service())
        self.assertFalse(battery_false.needs_service())

    def test_nubbin_battery(self):
        battery_true = Nubbin(date(2019, date.today().month, date.today().day))
        battery_false = Nubbin(date(2020, date.today().month, date.today().day))

        self.assertTrue(battery_true.needs_service())
        self.assertFalse(battery_false.needs_service())


class TestTires(unittest.TestCase):

    def test_carrigan_tire(self):
        tire_true = Carrigan([0.1, 0.5, 0.6, 0.9])
        tire_false = Carrigan([0.1, 0.5, 0.3, 0.6])

        self.assertTrue(tire_true.needs_service())
        self.assertFalse(tire_false.needs_service())

    def test_octoprime_tire(self):
        tire_true = OctoPrime([0.9, 0.9, 0.9, 0.9])
        tire_false = OctoPrime([0.1, 0.1, 0.1, 0.1])

        self.assertTrue(tire_true.needs_service())
        self.assertFalse(tire_false.needs_service())


if __name__ == '__main__':
    unittest.main()
