from Store import Store
from Query import Query
import sys


class Map:
    # Singleton instance
    __instance = None

    def __init__(self):
        self.__location_file = ''
        self.__query_file = ''
        self.__locations = []
        self.__queries = []
        if Map.__instance is not None:
            raise Exception("Map is a singleton and can only be instantiated once.")
        Map.__instance = self
        self.__current_query = None

    # Singleton Accessor
    @staticmethod
    def get_map_instance():
        if Map.__instance is None:
            Map.__instance = Map()
        return Map.__instance

    def get_location_file(self):
        return self.__location_file

    def get_query_file(self):
        return self.__query_file

    def get_locations(self):
        return self.__locations

    def get_queries(self):
        return self.__queries

    def get_current_query(self):
        return self.__current_query

    def set_location_file(self, location_file):
        self.__location_file = location_file

    def set_query_file(self, query_file):
        self.__query_file = query_file

    def set_locations(self, locations):
        self.__locations = locations

    def set_queries(self, queries):
        self.__queries = queries

    def set_current_query(self, query):
        self.__current_query = query
        self.update_distance(query)

    def load_locations(self, location_file):
        self.set_location_file(location_file)
        try:
            with open(location_file) as infile:
                rows = infile.readlines()
                for row in rows:
                    line = row.strip('\n')
                    token = line.split(',')
                    if token[5].lower() != 'latitude':
                        tmp_store = Store(token[0], token[1], token[2], token[3], token[4], float(token[5]), float(token[6]))
                        self.__locations.append(tmp_store)
                    else:
                        continue

        except FileNotFoundError:
            sys.stderr.write('''Store Locations file not found. Please verify the filename is correct and it is in the same directory as main.py''')
            exit(1)

    def load_queries(self, queries_file):
        self.set_query_file(queries_file)
        try:
            with open(queries_file) as infile:
                rows = infile.readlines()
                for row in rows:
                    line = row.strip('\n')
                    token = line.split(',')
                    if token[0].lower() == 'latitude':
                        continue
                    else:
                        tmp_query = Query(float(token[0]), float(token[1]), int(token[2]))
                        self.get_queries().append(tmp_query)
        except FileNotFoundError:
            sys.stderr.write('''Query file not found. Please verify the filename is correct and it is in the same directory as main.py''')
            exit(1)

    def update_distance(self, query):
        for location in self.get_locations():
            location.compute_distance(query.get_lat(), query.get_long())

    def __str__(self):
        ret = f'''This map is constructed using the {self.get_location_file()}\n-------------------------------------------------------------------\n'''
        for location in self.get_locations():
            ret += f"{location}\n"

        ret += f'''This map is considering the queries from {self.get_query_file()}\n-------------------------------------------------------------------\n'''
        for query in self.get_queries():
            ret += f"{query}\n"

        return ret
