# hash table created with help from:
# W-1_ChainingHashTable_zyBooks_Key-Value.py
# this can be found in the supplemental resources in the course tips


class HashTable:
    # method used to create a hash table with 1 bucket per package
    def __init__(self, num_of_buckets=40):
        # creates an empty list for the buckets
        self.list_of_buckets = []
        while num_of_buckets > 0:
            # insert a list inside a list
            self.list_of_buckets.append([])
            num_of_buckets = num_of_buckets - 1

    # method to insert a new value into the hash table
    def insert_key_value(self, key, value):
        # perform an operation to get the specific bucket number based on the key
        specific_bucket_number = hash(key) % len(self.list_of_buckets)
        # pull the bucket from the list of buckets
        specific_bucket_list = self.list_of_buckets[specific_bucket_number]
        # insert the key and value into the specific bucket
        key_value = [key, value]
        specific_bucket_list.append(key_value)

    # method that searches the hash table with a key and returns a value
    def find_package_from_hash_table(self, key):
        # perform an operation to get the specific bucket number based on the key
        specific_bucket_number = hash(key) % len(self.list_of_buckets)
        # pull the bucket from the list of buckets
        specific_bucket_list = self.list_of_buckets[specific_bucket_number]
        # searches the bucket for the key
        # if key is found, return the value
        # if no key is found, return string stating that no package is found
        for number in specific_bucket_list:
            if number[0] == key:
                return number[1]
            else:
                return "No Package Found"
