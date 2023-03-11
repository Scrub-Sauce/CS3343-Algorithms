import math


class Store:
    # Constructor
    def __init__(self, store_id, address, city, state, zip_code, long, lat):
        self.__store_id = store_id
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__long = long
        self.__lat = lat
        self.__distance = -1

    # Accessors
    def get_store_id(self):
        return self.__store_id

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip_code(self):
        return self.__zip_code

    def get_long(self):
        return self.__long

    def get_lat(self):
        return self.__lat

    def get_distance(self):
        return self.__distance

    # Mutators
    def set_store_id(self, store_id):
        self.__store_id = store_id

    def set_address(self, address):
        self.__address = address

    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
        self.__state = state

    def set_zip_code(self, zip_code):
        self.__zip_code = zip_code

    def set_long(self, long):
        self.__long = long

    def set_lat(self, lat):
        self.__lat = lat

    def set_distance(self, distance):
        self.__distance = distance

    # Helper Methods
    def computer_distance(self, from_long, from_lat):
        radius_of_earth_miles = 3958.8

        # Convert long and lat to radians for store
        store_long_rad = math.radians(self.get_long())
        store_lat_rad = math.radians(self.get_lat())

        # Convert long and lat to radians for our location
        from_long_rad = math.radians(from_long)
        from_lat_rad = math.radians(from_lat)

        # User the Haversine Formula to get the distance in miles.
        a = pow(math.sin((from_lat_rad - store_lat_rad)/2), 2) + math.cos(store_lat_rad) * math.cos(from_lat_rad) * pow(math.sin((from_long_rad - store_long_rad) / 2), 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        self.set_distance(radius_of_earth_miles * c)

    # String Override
    def __str__(self):
        ret = f"""\nStore\n
            -----------------------------------\n
            Store ID: {self.get_store_id()}\n
            Address: {self.get_address()}\n
            City: {self.get_city()}\n
            State: {self.get_state()}\n
            Zip: {self.get_zip_code()}\n
            Longitude: {self.get_long()}\n
            Latitude: {self.get_lat()}\n
            Distance: {self.get_distance()}\n"""
        return ret
