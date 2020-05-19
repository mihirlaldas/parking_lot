import unittest
import sys
from utils import (create_parking_lot,parking_available,registration_number_is_repeated,park_car)
# test all the utils modules
class TestUtils(unittest.TestCase):
    """
    to test the util functions
    """
    def test_create_parking_lot(self):
        testParkingLot = create_parking_lot(str(6))
        self.assertEqual(len(testParkingLot.get_slots()),6)
        # slot size should be a number
        testParkingLot = create_parking_lot(str('a'))
        self.assertEqual(testParkingLot,None)

    def test_parking_available(self):
        testParkingLot = create_parking_lot(str(6))
        result = parking_available(testParkingLot)
        self.assertTrue(result)

    def test_registration_number_is_repeated(self):
        testParkingLot = create_parking_lot(str(6))
        result = park_car(testParkingLot,'KA-01-HH-1234', 'White')
        result = registration_number_is_repeated(testParkingLot,'KA-01-HH-1234')
        self.assertTrue(result)

    def test_park_car(self):
        testParkingLot = create_parking_lot(str(6))
        result = park_car(testParkingLot,'KA-01-HH-1234', 'White')
        self.assertTrue(result)
        result = park_car(testParkingLot,'KA-01-HH-1234', 'White')
        self.assertFalse(result)
    
    def test_nearest_allocation(self):
        testParkingLot = create_parking_lot(str(6))
        park_car(testParkingLot,'KA-01-HH-1234', 'White')
        park_car(testParkingLot,'KA-02-HH-1234', 'White')
        park_car(testParkingLot,'KA-03-aH-5234', 'White')
        assignedSlot = testParkingLot.get_slots()[3].get_slot()
        self.assertEqual(assignedSlot,3)

    def test_parking_full(self):
        testParkingLot = create_parking_lot(str(2))
        park_car(testParkingLot,'KA-01-HH-1234', 'White')
        park_car(testParkingLot,'KA-02-HH-1234', 'White')
        result = park_car(testParkingLot,'KA-03-aH-5234', 'White')
        self.assertFalse(result)





        




if __name__ == '__main__':
    unittest.main()