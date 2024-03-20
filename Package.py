import csv
import datetime


class Package:
    # method to create package
    def __init__(self, package_id, package_address, package_city, package_zip, package_state, package_deadline,
                 package_weight):
        self.package_file = None
        self.package_id = package_id
        self.package_address = package_address
        self.package_city = package_city
        self.package_state = package_state
        self.package_zip = package_zip
        self.package_weight = package_weight
        self.package_deadline = package_deadline
        self.package_status = "At Hub"
        self.package_departure_time = datetime.timedelta(hours=0)
        self.package_arrival_time = datetime.timedelta(hours=23, minutes=59, seconds=59)

    # method to print package information
    def __str__(self):
        return f'{self.package_id} Address: {self.package_address}, {self.package_state} {self.package_zip} ' \
               f'Package Weight: {self.package_weight} Deadline: {self.package_deadline} Status:' \
               f' {self.package_status} Departure Time: {self.package_departure_time} Arrival Time:' \
               f' {self.package_arrival_time}'


# method that creates the package object and inserts it into the hash table
def insert_packages_into_hash_table(hash_table):
    # opens the csv package file and uses it to create package objects
    with open("csv/Package_File.csv") as file:
        package_file = csv.reader(file)
        # each row is a new object.
        for row in package_file:
            # creates a "package" object from each row in the file
            # loads it into the hash table
            hash_table.insert_key_value(int(row[0]), Package(int(row[0]), row[1], row[2],
                                                             row[3], row[4], row[5], row[6]))


# Method to update package status
def update_status(package, current_time):
    # departure time is later than current time
    if package.package_departure_time > current_time:
        package.package_status = "At Hub"
        package.package_departure_time = None
        package.package_arrival_time = None
    # after departure time but before delivery time
    elif package.package_departure_time <= current_time < package.package_arrival_time:
        package.package_status = "In Transit"
        package.package_arrival_time = None
    # if neither, then package is delivered
    else:
        package.package_status = "Delivered"

    # if time is before 10:20, package 9 has original address
    time_variable = datetime.timedelta(hours=10, minutes=20)
    if package.package_id == 9 and current_time < time_variable:
        package.package_address = "300 State St"
        package.package_zip = "84103"
