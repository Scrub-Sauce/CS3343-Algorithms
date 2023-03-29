from Store import Store
from Query import Query
import random
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
                row_num = 0
                for row in rows:
                    line = row.strip('\n')
                    token = line.split(',')
                    if token[5] == 'AK':
                        print(f"{row_num}")
                    if token[5].lower() != 'latitude':
                        tmp_store = Store(token[0], token[1], token[2], token[3], token[4], float(token[5]), float(token[6]))
                        self.__locations.append(tmp_store)
                        row_num += 1
                    else:
                        row_num += 1
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

    def swap_elements(self, index_a, index_b):
        locations_list = self.get_locations()
        tmp = locations_list[index_a]
        locations_list[index_a] = locations_list[index_b]
        locations_list[index_b] = tmp

    def rand_select(self, left_bound, right_bound, desired_num_loc):
        locations_list = self.get_locations()
        desired_index = desired_num_loc - 1
        if left_bound == right_bound:
            return locations_list[left_bound]
        else:
            global_piv_index = self.rand_partition(left_bound, right_bound)

            if desired_index == global_piv_index:
                return locations_list[global_piv_index]
            elif desired_index > global_piv_index:
                return self.rand_select((global_piv_index + 1), right_bound, desired_num_loc)
            elif desired_index < global_piv_index:
                return self.rand_select(left_bound, (global_piv_index - 1), desired_num_loc)

    def rand_partition(self, left_index, right_index):
        locations_list = self.get_locations()

        randomise_pivot_index = random.randint(left_index, right_index)
        self.swap_elements(left_index, randomise_pivot_index)

        pivot = locations_list[left_index].get_distance()
        left_position = left_index

        for i in range(left_index + 1, right_index + 1):
            if locations_list[i].get_distance() <= pivot:
                left_position += 1
                self.swap_elements(left_position, i)

        self.swap_elements(left_index, left_position)

        return left_position

    def process_queries(self):
        queries = self.get_queries()
        locations = self.get_locations()
        output = []

        for query in queries:
            self.set_current_query(query)

            loc_num = query.get_desired_num_locations()

            self.rand_select(0, (len(locations) - 1), loc_num)

            for i in range(0, loc_num):
                query.add_result(locations[i])

            query.get_results().sort(key=lambda store: store.get_distance())

            output.append(f'{query}\n')

        out_file = open('Output.txt', 'w')
        out_file.writelines(output)
        out_file.close()

    def __str__(self):
        ret = f'''This map is constructed using the {self.get_location_file()}\n-------------------------------------------------------------------\n'''
        for location in self.get_locations():
            ret += f"{location}\n"

        ret += f'''This map is considering the queries from {self.get_query_file()}\n-------------------------------------------------------------------\n'''
        for query in self.get_queries():
            ret += f"{query}\n"

        return ret
