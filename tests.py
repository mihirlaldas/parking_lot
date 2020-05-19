import unittest
from utils import (create_parking_lot)
# test all the utils modules
class TestUtils(unittest.TestCase):
    """
    to test the util functions
    """
    def test_create_parking_lot(self):
        parkingLot = create_parking_lot(str(6))
        self.assertEqual(len(parkingLot.get_slots()),6)
        # slot size should be a number
        parkingLot = create_parking_lot(str('a'))
        self.assertEqual(parkingLot,None)
        




if __name__ == '__main__':
    unittest.main()