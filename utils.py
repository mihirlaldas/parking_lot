# all the class logic

class Car:
    """ Class car
        props - registrationNumber(str), color(str), slotNumber(int)
        methods - getter for registratoinNumber and color. getter and setter for slotNumber.
               
    
    """

    def __init__(self,registrationNumber,color):
        """ 
        constructor to initialize registration and color of car
        arguments- <registrationNumber>,<color>
        """
        self.registratoinNumber = registrationNumber
        self.color = color
        # car slotNuber is initialze with None, to be later updated when car is parked
        self.slotNumber = None

    def get_registration_number(self):
        """ getter for registration number """
        return self.registratoinNumber

    def get_color(self):
        """ getter for color """
        return self.color

    def set_slot(self,slot):
        """ setter car slot
            argument - <slot>
        """
        self.slotNumber = slot

    def get_slot(self):
        """ getter car slot"""
        return self.slotNumber


class ParkingLot:
    """
    class Parking lot
    props - carsCount(int), slots(dict) . slots structure{1:car_object_1,2:car_object_2, 3: None, 4: NOne}
    methods - getters carsCount and slots, increment and decrement carsCount, setter for slots
    """
    def __init__(self,n):
        """ constructore to create slots of size n
        argument - <n>(int)
        """
        self.carsCount = 0
        # initialize slots as key value pair with key as slot number and value as None, later to be updated with car object
        self.slots = dict()
        for i in range(1,int(n+1)):
            self.slots[i]=None

    def get_cars_count(self):
        """ getter for parked cars count"""
        return self.carsCount

    def get_slots(self):
        """ getter for slots"""
        return self.slots

    def increment_cars_count(self):
        """
        increase parked cars count
        """
        self.carsCount += 1
    
    def decrement_cars_count(self):
        """
        decrement parked cars count
        """
        self.carsCount -= 1

    def set_slots(self,slot,car):
        """ setter for slots
            arguments - slot(int), car(object of type Car)
        """
        self.slots[slot]=car


def create_parking_lot(n):
    """ create a parking lot object with n slots 
        arguments - <n>(str)
    """
    # valid n is digit
    if n is not None and n.isdigit():
        parkingLot = ParkingLot(int(n))
        print('Created a parking lot with {} slots'.format(n))
        return parkingLot
    else:
        print('slot size sould be an integer')
        return None
# car = Car('wb-01-abc-09','white')
# parkingLot = ParkingLot(6)
# parkingLot.set_slots(1,car)
# parkingLot.increment_cars_count()
# print(parkingLot.get_cars_count(),parkingLot.get_slots())