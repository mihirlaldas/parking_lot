# main entry point 
import sys
from utils import (create_parking_lot)

def runCommand(parkingLot,command):
    if command[0] == 'create_parking_lot':
        parkingLot = create_parking_lot(command[1])
    else:
        print('command not applicable, please refer README file for valid interactive commands or execute using input_file.txt')
    return parkingLot




# take command from user until exit is typed
def interactive(parkingLot):
    try:
        command = input().split()
        while command[0] != 'exit':
            parkingLot = runCommand(parkingLot, command)
            command = input().split()
    except Exception as e:
        print(e)
        

def main():
    parkingLot = None
    if len(sys.argv) > 1:
        # file input mode
        pass
    else:
        # interactive mode
        interactive(parkingLot)


if __name__ == '__main__':
    main()