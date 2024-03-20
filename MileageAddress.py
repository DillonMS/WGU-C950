import csv


# Method that returns a value for an address to be used in the "get_distance" Method
def get_address_id(address):
    # opens the address file and turns it into something the program can read
    with open("csv/Address_File.csv") as csv_address_file:
        address_file = csv.reader(csv_address_file)
        # searches each row of the file
        # if the address that was provided matches the address in that row,
        # return the id number as an integer
        for row in address_file:
            if address in row[2]:
                return int(row[0])


# method that returns the mileage between two locations
def get_distance_between_points(current_location, next_destination):
    # opens the address file and turns it into something the program can read
    with open("csv/Distance_File.csv") as file2:
        distance_csv = csv.reader(file2)
        distance_chart = list(distance_csv)
        # selecting a value based on the rows and columns
        distance = distance_chart[current_location][next_destination]
        # sometimes searching this way results in a blank space
        # if the coordinates are flipped, then a blank space should not occur
        if distance == "":
            distance = distance_chart[next_destination][current_location]
        # return the distance as a float value because the decimal points matter
        return float(distance)
