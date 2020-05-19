# Parking lot CLI built using python ,OOPs, TDD

## To install all dependencies, compile and run tests:

`$ bin/setup`

## To run the code so it accepts input from a file:

`$ bin/parking_lot file_inputs.txt`

## Interactive

`$ bin/parking_lot`

### interactive commands

- `create_parking_lot <n>`  
  To create parking lot with 'n' slots

- `park <registration number of car> <color of car>`  
  To park the car in parking lot. Prints alloted slot number

- `leave <slot number>`  
  Car leaves the slot.

- `status`  
  Prints All the slots that are occupied with car's registration number and color.

- `registration_numbers_for_cars_with_colour <color>`  
  Prints Registration numbers of all cars of a particular colour.

- `slot_numbers_for_cars_with_colour <color>`  
  Prints Slot numbers of all slots where a car of a particular colour is parked.

- `slot_number_for_registration_number <registration number>`  
  Print Slot number in which a car with a given registration number is parked.

- `exit`  
  exit from the application
