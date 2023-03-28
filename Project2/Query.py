class Query:
    # Constructor
    def __init__(self, lat, long, desired_num_locations):
        self.__lat = lat
        self.__long = long
        self.__desired_num_locations = desired_num_locations
        self.__results = []

    # Accessors
    def get_lat(self):
        return self.__lat

    def get_long(self):
        return self.__long

    def get_desired_num_locations(self):
        return self.__desired_num_locations

    def get_results(self):
        return self.__results

    # Mutators
    def set_lat(self, lat):
        self.__lat = lat

    def set_long(self, long):
        self.__long = long

    def set_desired_num_locations(self, desired_num_locations):
        self.__desired_num_locations = desired_num_locations

    def set_results(self, results):
        self.__results = results

    # Helper Methods
    def add_result(self, location):
        self.get_results().append(location)

    def remove_result(self, location):
        self.get_results().remove(location)

    def __str__(self):
        return f'Query - Latitude: {self.get_lat()}, Longitude: {self.get_long()}, Desired Number: {self.get_desired_num_locations()}'
