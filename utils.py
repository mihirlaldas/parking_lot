# all the class logic

class Car:
    """ Class car
        props - registrationNumber(str), color(str), slotNumber(int)
        methods - getter for registrationNumber and color. getter and setter for slotNumber.
               
    
    """

    def __init__(self,registrationNumber,color):
        """ 
        constructor to initialize registration and color of car
        arguments- <registrationNumber>,<color>
        """
        self.registrationNumber = registrationNumber
        self.color = color
        # car slotNuber is initialze with None, to be later updated when car is parked
        self.slotNumber = None

    def get_registration_number(self):
        """ getter for registration number """
        return self.registrationNumber

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


def parking_available(parkingLot):
    """ check if parking lot is full or not. returns boolean
    argument - <parkingLot> (object)
    """
    return parkingLot.get_cars_count() < len(parkingLot.get_slots())

def registration_number_is_repeated(parkingLot,registrationNumber):
    """
    check for duplicate registration number. retun boolean
    arguments- <parkingLot>(object),<registrationNumber>(str)
    """
    slots = parkingLot.get_slots()
    for i in slots.keys():
        if slots[i] is not None:
            if slots[i].registrationNumber == registrationNumber:
                return True
    return False

def park_car(parkingLot,registrationNumber,color):
    """park a car to the slot of parkingLot
        arguments - <parkingLot> (object), <registrationNumber>(str), <color>(str)
        return True if car is parked, else return false
    """
    # check if parking lot is defined
    if parkingLot:
        # check if parking lot has available space
        if parking_available(parkingLot):
            # check for duplicate registrationNumber.
            if not registration_number_is_repeated(parkingLot,registrationNumber):
                slots = parkingLot.get_slots()
                for i in slots.keys():
                    if slots[i] is None:
                        # create new car object
                        car = Car(registrationNumber,color)
                        car.set_slot(i)
                        parkingLot.set_slots(i,car)
                        parkingLot.increment_cars_count()
                        print('Allocated slot number: {}'.format(i))
                        return True
            else:
                print("Sorry, this car is already parked")
                return False
        else:
            print('Sorry, parking lot is full')
            return False
    else:
        print('sorry, parking lot not defined')
        return False

def leave_parking(parkingLot,slot):
    """
        car is checking out of parking so make the slot empty
        arguments - <parkingLot>(object), <slot>(str)
    """
    result = ""
    if parkingLot:
        if slot.isdigit():
            slots = parkingLot.get_slots()
            slot = int(slot)
            if slot not in slots.keys():
                result = "Slot number not in parking lot"
            elif slots[slot] is not None:
                parkingLot.set_slots(slot,None)
                parkingLot.decrement_cars_count()
                result = 'Slot number ' + str(slot) + ' is free'
            else:
                result = 'Slot is already empty'
        else:
            result = 'Slot number should be a digit'
    else:
        result = 'sorry, parking lot not defined'
    return result

def status(parkingLot):
    """
    returns status of the parkingLot with slot no., registration no., color.
    """           
    result = '' 
    if parkingLot:
        result = "Slot No.    Registration No    Colour\n"
        slots = parkingLot.get_slots()
        for key in slots.keys():
            if slots[key] is not None:
                result += str(key) + "           " + slots[key].registrationNumber + "      " + slots[key].color + '\n'
    else:
        result = "sorry, parking lot not defined"
    return result
