# main entry point 
import sys
from utils import (create_parking_lot,park_car,leave_parking,status, get_registration_numbers_by_color,get_slot_numbers_by_color, get_slot_number_for_registration_number)

def runCommand(parkingLot,command):
    if command[0] == 'create_parking_lot':
        parkingLot = create_parking_lot(command[1])
    elif command[0] == 'park':
        park_car(parkingLot,command[1],command[2])
    elif command[0] == 'leave':
        print(leave_parking(parkingLot,command[1]))
    elif command[0] == 'status':
        print(status(parkingLot).rstrip('\n'))
    elif command[0] == 'registration_numbers_for_cars_with_colour':
        print(get_registration_numbers_by_color(parkingLot,command[1]))
    elif command[0] == 'slot_numbers_for_cars_with_colour':
        print(get_slot_numbers_by_color(parkingLot,command[1]))
    elif command[0] == 'slot_number_for_registration_number':
        print(get_slot_number_for_registration_number(parkingLot,command[1]))
    else:
        print('command not applicable, please refer README file for valid interactive commands or execute using input_file.txt')
    return parkingLot




# take command from user until exit is typed
def interactive(parkingLot):
    """
    execute parking lot funcions interactively
    """
    try:
        command = input().split()
        while command[0] != 'exit':
            parkingLot = runCommand(parkingLot, command)
            command = input().split()
    except Exception as e:
        print(e)
        
#take command from input file
def automatic(parkingLot,fileInput):
    """
        execute parking lot functions automaticaly by reading comannds input file
        arguments: parkingLot, input file
    """
    try:
        with open(fileInput) as file:
            lines = file.readlines()
            for line in lines:
                command = line.split()
                # print(command)

                parkingLot = runCommand(parkingLot,command)
    except Exception as e:
        print(e)


def main():
    parkingLot = None
    if len(sys.argv) > 1:
        # file input mode
        automatic(parkingLot,sys.argv[1])
    else:
        # interactive mode
        interactive(parkingLot)


if __name__ == '__main__':
    main()