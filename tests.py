import unittest
import sys
from utils import (create_parking_lot,parking_available,registration_number_is_repeated,park_car,leave_parking, status)
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

    def test_leave_isdigit(self):
        testParkingLot = create_parking_lot(str(2))
        result = leave_parking(testParkingLot,'a')
        self.assertEqual(result,'Slot number should be a digit')


    def test_leave_empty_parking_slot(self):
        testParkingLot = create_parking_lot(str(2))
        result = leave_parking(testParkingLot,str(2))
        self.assertEqual(result,'Slot is already empty')

    def test_leave_slot(self):
        testParkingLot = create_parking_lot(str(2))
        park_car(testParkingLot,'KA-01-HH-1234', 'White')
        result = leave_parking(testParkingLot,str(1))
        self.assertEqual(result,'Slot number 1 is free')

    def test_leave_slot_not_present_in_parking(self):
        testParkingLot = create_parking_lot(str(6))
        park_car(testParkingLot,'KA-01-HH-1234', 'White')
        result = leave_parking(testParkingLot,str(7))
        self.assertEqual(result,'Slot number not in parking lot')

    def test_status(self):
        testParkingLot = create_parking_lot(str(6))
        park_car(testParkingLot,'KA-01-HH-1234', 'White')
        park_car(testParkingLot,'KA-01-HH-9999', 'White')
        park_car(testParkingLot,'KA-01-BB-0001', 'Black')
        park_car(testParkingLot,'KA-01-HH-7777', 'Red')
        park_car(testParkingLot,'KA-01-HH-2701', 'Blue')
        park_car(testParkingLot,'KA-01-HH-3141', 'Black')
        leave_parking(testParkingLot,str(4))
        result = status(testParkingLot)
        self.assertEqual(result,'Slot No.    Registration No    Colour\n1           KA-01-HH-1234      White\n2           KA-01-HH-9999      White\n3           KA-01-BB-0001      Black\n5           KA-01-HH-2701      Blue\n6           KA-01-HH-3141      Black\n')











        




if __name__ == '__main__':
    unittest.main()