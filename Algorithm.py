from MileageAddress import get_address_id, get_distance_between_points
import datetime
from Package import update_status


# algorithm created with help from the following document,
# C950 WGUPS Project Implementation Steps - Example - Nearest Neighbor
# this can be found in the supplemental resources in the course tips


# sort packages and deliver them.
def nearest_neighbor_and_delivery(truck, hash_table):
    # create a list of unsorted packages from the truck
    unsorted_list = []
    for package_id in truck.packages:
        # update package departure time to the truck's current time
        package_object = hash_table.find_package_from_hash_table(package_id)
        package_object.package_departure_time = truck.time
        # add package to unsorted list to be sorted
        unsorted_list.append(package_object)

    # determines what package has the next closest location from the current location
    while len(unsorted_list) != 0:
        # creates a dummy shortest distance to be replaced by the actual shortest distance
        shortest_distance = 1000
        # this is the package that will be delivered next
        # the value is None because nothing has been selected yet
        package_deliver_next = None
        for package in unsorted_list:
            # update package 9 to correct address if time is 10:20 AM or later
            time_variable = datetime.timedelta(hours=10, minutes=20)
            if package.package_id == 9 and truck.time >= time_variable:
                package.package_address = "410 S State St"
                package.package_zip = "84111"
            # takes the string address and returns a value to be used with the distance method
            current_location_id = get_address_id(truck.address)
            next_location_id = get_address_id(package.package_address)
            # gets the distance between the truck and the current package
            truck_to_address_distance = get_distance_between_points(current_location_id, next_location_id)
            # if the new package has the shortest distance, update the shortest distance and the package
            # to be delivered next
            if truck_to_address_distance <= shortest_distance:
                shortest_distance = truck_to_address_distance
                package_deliver_next = package

        # update the truck's data
        # mileage is the current mileage + the distance to the next location
        truck.mileage = truck.mileage + shortest_distance
        # truck address is updated to the location of the package it just delivered
        truck.address = package_deliver_next.package_address
        # distance divided by 18 mph = time
        added_time = shortest_distance / 18
        # truck time + the added time = new truck time
        truck.time = truck.time + datetime.timedelta(hours=added_time)

        # updates the package's data
        # the package arrival time is updated to the truck's current time
        package_deliver_next.package_arrival_time = truck.time
        # update the package status
        update_status(package_deliver_next, truck.time)

        # remove package from unsorted list so that the package is not used again in the greedy algorithm
        unsorted_list.remove(package_deliver_next)


def truck_return_to_hub(truck):
    current_location = get_address_id(truck.address)
    home_destination = get_address_id("4001 South 700 East")
    home_mileage = get_distance_between_points(current_location, home_destination)
    truck.mileage += home_mileage
    home_time = home_mileage/18
    truck.time += datetime.timedelta(hours=home_time)
