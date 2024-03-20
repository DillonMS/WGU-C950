# Student ID: 011045379
# Dillon Smith

from Truck import Truck
from Algorithm import truck_return_to_hub
from Package import insert_packages_into_hash_table
import datetime
from HashTable import HashTable
from Algorithm import nearest_neighbor_and_delivery
from Package import update_status

# Creates 3 trucks with packages manually loaded onto them
first_truck = Truck(0, "4001 South 700 East", datetime.timedelta(hours=8),
                    [1, 13, 14, 20, 34, 16, 15, 40, 31, 29, 30, 37, 39, 19])

second_truck = Truck(0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5),
                     [21, 26, 24, 17, 23, 38, 35, 27, 12, 3, 36, 18, 22, 6])

third_truck = Truck(0, "4001 South 700 East", datetime.timedelta(hours=10, minutes=20),
                    [2, 4, 5, 7, 8, 9, 10, 11, 25, 28, 32, 33])

# Creates a hash table
package_hash_table = HashTable()
# inserts packages and information into hash table
insert_packages_into_hash_table(package_hash_table)

# performs delivery on all 3 trucks
nearest_neighbor_and_delivery(first_truck, package_hash_table)
truck_return_to_hub(first_truck)
nearest_neighbor_and_delivery(second_truck, package_hash_table)
nearest_neighbor_and_delivery(third_truck, package_hash_table)

# user interface
print("Western Governor's United Parcel Service\nA program by Dillon Smith")
print("Truck 1 Miles: ", first_truck.mileage, "\nTruck 2 Miles: ", second_truck.mileage, "\nTruck 3 Miles: ",
      third_truck.mileage)
total_mileage = first_truck.mileage + second_truck.mileage + third_truck.mileage
print("The trucks drove for a total distance of", total_mileage, "Miles.")
try:
    # enter a time to check on package(s)
    user_input_time = input("Please enter a time(hh:mm:ss) to view packages.\n")
    # converts string of time into a form that the program can use
    user_time = datetime.datetime.strptime(user_input_time, '%H:%M:%S').time()
    user_time_delta = datetime.timedelta(hours=user_time.hour, minutes=user_time.minute, seconds=user_time.second)
    user_input_selection = input("Type '1' for All Packages.\nType '2' for Individual Package.\n")
    # check on all packages at chosen time
    if user_input_selection == "1":
        for x in range(1, 41):
            package = (package_hash_table.find_package_from_hash_table(x))
            update_status(package, user_time_delta)
            print(package_hash_table.find_package_from_hash_table(x))
        exit()
    # check on specific package at chosen time
    elif user_input_selection == "2":
        try:
            # enter package number for information
            user_input_package = int(input("Type the number of the package you wish to view.\n"))
            package = package_hash_table.find_package_from_hash_table(user_input_package)
            print(package_hash_table.find_package_from_hash_table(user_input_package))
            exit()
        except ValueError:
            print("Invalid Input")
            exit()
    else:
        print("Invalid Input")
        exit()
except ValueError:
    print("Invalid Input")
    exit()
